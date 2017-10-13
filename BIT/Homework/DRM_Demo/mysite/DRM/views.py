from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse,FileResponse,Http404
import json
from .models import Book,PurchaseCase
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.files import File
from nt import times


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
            list.append({'book_name':b.book_name,'book_id':b.id,'isavailable':isavailable,'count':count,'url':b.ebook.url})
        json_obj['book_list'] = list
        json_obj['state'] = 'success'
        return JsonResponse(json_obj)
    else:
        json_obj['state'] = 'fail'
        json_obj['msg'] = 'Please login first'
        return JsonResponse(json_obj)

def book_detail(request,book_id):
    json_obj = {}
    try:
        book = Book.objects.get(pk=book_id)
        json_obj['state'] = 'success'
        json_obj['book_name'] = book.book_name
    except Book.DoesNotExist:
        json_obj['state'] = 'fail'
        json_obj['msg'] = 'Book does not exist'
    return HttpResponse(json.dumps(json_obj))

def userlogin(request):
    json_obj = {}
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        # A backend authenticated the credentials
        login(request, user)
        json_obj['state'] = 'success'
        #json_obj['msg'] = 'Book does not exist'
    else:
        json_obj['state'] = 'fail'
        #json_obj['msg'] = 'Book does not exist'
    return HttpResponse(json.dumps(json_obj))

def userlogout(request):
    json_obj = {}
    logout(request)
    json_obj['state'] = 'success'
    json_obj['msg'] = '注销成功'
    #return HttpResponse(json.dumps(json_obj))
    return JsonResponse(json_obj)
def download(request):
    try:
        case = PurchaseCase.objects.get(user=request.user,book_id=request.POST['book_id'])
        return FileResponse(open(case.book.ebook.name,'rb'))
    except PurchaseCase.DoesNotExist:
        raise Http404("File does not exist")
    '''   
    try:
        return FileResponse(open('ebook/'+filename,'rb'))
        #with open('ebook/'+filename,'rb') as f:
            
    except FileNotFoundError :
         raise Http404("File does not exist")
    '''  

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
        return JsonResponse({'state':'fail','msg':'Please login first'})
    
def tt(request):
    if request.user.is_authenticated:
    # Do something for authenticated users.
        return HttpResponse("测试通过")
    else:
    # Do something for anonymous users.
        return HttpResponse("请先登录")
        
    