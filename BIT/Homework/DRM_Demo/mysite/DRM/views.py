from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse,FileResponse,Http404
import json
from .models import Book,PurchaseCase,GiftCode
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.files import File
from nt import times
import random
import string


def book_list(request):
    list =[]
    json_obj = {}
    if request.user.is_authenticated:
        book_list = Book.objects.all()
        for b in book_list:
            try:
                case = PurchaseCase.objects.get(user=request.user,book_id=b.id)
                isavailable = 1
                count = case.count
            except PurchaseCase.DoesNotExist:
                isavailable = 0
                count = 0
            list.append({'book_name':b.book_name,'book_id':b.id,'isavailable':isavailable,'count':count})
        json_obj['book_list'] = list
        json_obj['state'] = 'success'
        return JsonResponse(json_obj)
    else:
        json_obj['state'] = 'fail'
        json_obj['msg'] = '还未登陆,请先登录'
        return JsonResponse(json_obj)

def userlogin(request):
    json_obj = {}
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        json_obj['state'] = 'success'
        json_obj['msg'] = '登陆成功'
    else:
        json_obj['state'] = 'fail'
        json_obj['msg'] = '登陆失败'
    return HttpResponse(json.dumps(json_obj))

def userlogout(request):
    json_obj = {}
    logout(request)
    json_obj['state'] = 'success'
    json_obj['msg'] = '注销成功'
    return JsonResponse(json_obj)
def download(request):
    if request.user.is_authenticated:
        try:
            case = PurchaseCase.objects.get(user=request.user,book_id=request.POST['book_id'])
            return FileResponse(open(case.book.ebook.name,'rb'))
        except PurchaseCase.DoesNotExist:
            raise Http404("File does not exist")
    else:
        return JsonResponse({'state':'fail','msg':'还未登陆,请先登录'})
def getkey(request):
    if request.user.is_authenticated:
        book_id=request.POST['book_id']
        mac = request.POST['mac']
        try:
            case = PurchaseCase.objects.get(user=request.user,book_id=book_id)
            mac_list = case.mac_list
            count = case.count
            if mac_list:
                mac_list = mac_list.split(',')
            else:
                mac_list = []
            if mac in mac_list:
                return  JsonResponse({'state':'success','msg':'此mac已经在许可列表中,秘钥放行','key':case.book.key})
            elif count:
                mac_list.append(mac)
                case.mac_list = ','.join(mac_list)
                case.count = count - 1
                case.save()
                return  JsonResponse({'state':'success','msg':'此mac不在在许可列表中,消耗一次拷贝次数,秘钥放行','key':case.book.key})
            else:
                return  JsonResponse({'state':'fail','msg':'账号无可用拷贝数'})
        except PurchaseCase.DoesNotExist:
            return  JsonResponse({'state':'fail','msg':'没有权限,请先购买'})
    else:
        return JsonResponse({'state':'fail','msg':'还未登陆,请先登录'})
def purchase(request):
    if request.user.is_authenticated:
        times = int(request.POST['times'])
        book_id=request.POST['book_id']
        try:
            case = PurchaseCase.objects.get(user=request.user,book_id=book_id)
            case.count = case.count + times
            case.save()
            return JsonResponse({'state':'success','msg':'购买成功'})
        except BaseException:
            case = PurchaseCase.objects.create(user=request.user,book = Book.objects.get(pk=book_id),count = times)
            return JsonResponse({'state':'success','msg':'购买成功'})
    else:
        return JsonResponse({'state':'fail','msg':'还未登陆,请先登录'})
 
def getcode(request):
    if request.user.is_authenticated:
        book_id=request.POST['book_id']
        try:
            case = PurchaseCase.objects.get(user=request.user,book_id=book_id)
            count = case.count
            if count:
                case.count = count - 1
                case.save()
                code = ''.join(random.sample(string.ascii_letters + string.digits,32))
                GiftCode.objects.create(book = Book.objects.get(pk=book_id),code = code)
                return  JsonResponse({'state':'success','msg':'生成兑换码成功,消耗一次拷贝次数','code':code})
            else:
                return  JsonResponse({'state':'fail','msg':'生成兑换码失败,账号无可用拷贝数'})
        except PurchaseCase.DoesNotExist:
            return  JsonResponse({'state':'fail','msg':'生成兑换码失败,没有权限,请先购买'})
    else:
        return JsonResponse({'state':'fail','msg':'还未登陆,请先登录'})

def usecode(request):
    if request.user.is_authenticated:
        code=request.POST['code']
        try:
            giftcode = GiftCode.objects.get(code=code)
            book_id=giftcode.book.id
            try:
                case = PurchaseCase.objects.get(user=request.user,book_id=book_id)
                case.count = case.count + 1
                case.save()
            except BaseException:
                case = PurchaseCase.objects.create(user=request.user,book = Book.objects.get(pk=book_id),count = 1)
            GiftCode.objects.get(code=code).delete()
            return JsonResponse({'state':'success','msg':'兑换%s成功'%giftcode.book.book_name})
        except GiftCode.DoesNotExist:
            return  JsonResponse({'state':'fail','msg':'兑换失败,原因:兑换码错误'})
    else:
        return JsonResponse({'state':'fail','msg':'还未登陆,请先登录'})
        
def upload(request):
    if request.user.is_authenticated:
        book_name=request.POST['book_name']
        key=request.POST['key']
        ebook=request.POST['ebook']
        with open('ebook/'+book_name+'.txt','w') as f: 
            f.write(ebook)
        book = Book.objects.create(book_name=book_name,key = key,ebook = 'ebook/'+book_name+'.txt')
        return JsonResponse({'state':'success','msg':'上传成功'})
        
    else:
        return JsonResponse({'state':'fail','msg':'还未登陆,请先登录'})