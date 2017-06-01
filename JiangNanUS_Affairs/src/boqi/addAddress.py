import urllib.request
import http.cookiejar
import json
import re
from PIL import Image
import io
import matplotlib.pyplot as plt

#加入对cookies的支持
cookieJarInMemory = http.cookiejar.CookieJar();
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookieJarInMemory));
urllib.request.install_opener(opener);

while True:
#获取登录验证码ID
    url_login='http://www.boqii.com/user/login'
    #添加http header
    #HTTP头部
    http_headers = {'Host':'www.boqii.com',
    'Connection':'keep-alive',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.8.2000 Chrome/30.0.1599.101 Safari/537.36',
    'Content-Type':'application/x-www-form-urlencoded',
    'Accept-Language':'zh-CN',
    'DNT':'1',
    'Referer':'http://www.boqii.com/'
    }
    #创建Request对象
    request = urllib.request.Request(url = url_login,
                                     headers= http_headers)
    #发送请求
    response = urllib.request.urlopen(request)
    #保存网页内容
    context = response.read().decode('UTF8')
    #输出网页内容
    #print(context)
    re_vcode = re.compile(r'update=((\d){3})"')
    get_vcode_num = re_vcode.search(context).group(1)
    #print(get_vcode_num)
    

#获取验证码
    url='http://www.boqii.com/user/images/vcode/vcode.php'
    data_values = {'update' : get_vcode_num }
    url_data = urllib.parse.urlencode(data_values)
    #创建Request对象
    request = urllib.request.Request(url = url+'?'+url_data,
                                     headers= http_headers)
    #发送请求
    response = urllib.request.urlopen(request)
    #显示验证码图片
    im_data = response.read()
    file = io.BytesIO(im_data)
    img=Image.open(file)
    plt.imshow(img)
    plt.show()
    #人工输入验证码
    vcode = input()
    print("验证码是"+vcode)
    
#登录
    url_login='http://www.boqii.com/site/User/usercenter'
    #创建Request对象
    request = urllib.request.Request(url_login,headers=http_headers)
    #POST_Data
    post_data = {'action' : 'login',
    'username' : '18861823199',
    'password' : 'woaiwojia',
    'remember' : '0',
    'verify' : vcode
    }
    post_data_code= urllib.parse.urlencode(post_data).encode(encoding='UTF8')
    #发送请求
    response = urllib.request.urlopen(request,data=post_data_code,timeout=5)
    #保存网页内容
    context = response.read().decode('UTF8')
    #输出网页内容
    #print(context)
    context = eval(context)
    if context['status']=='ok':
        print("登陆成功")
        break
    else:
        print(context)
    


#获取用于添加收货地址的ID
url_login='http://www.boqii.com/userinfo/User/addAddress'
#HTTP头部
http_headers['Referer']='http://www.boqii.com/userinfo/User/address'
#创建Request对象
request = urllib.request.Request(url_login,headers=http_headers)
#发送请求
response = urllib.request.urlopen(request)
#保存网页内容
context = response.read().decode('UTF8')
#输出网页内容
#print(context)
#找出用于添加收货地址的ID
re_uniq = re.compile(r'name="uniq" value="(\w+)"')
get_uniq_num = re_uniq.search(context).group(1)
#print(get_uniq_num)


#添加收货地址
url_login='http://www.boqii.com/userinfo/User/editAddress'
#HTTP头部
http_headers['Referer']='http://www.boqii.com/userinfo/User/addAddress'
#创建Request对象
request = urllib.request.Request(url_login,headers=http_headers)
#POST_Data
post_data = {'uniq':get_uniq_num,
'name':'明坤',
'province':'32',
'city':'3202',
'street':'滨湖区蠡湖大道融创星光广场171栋-3004',
'mobile':'18861823199',
'telephone':'',
'zipcode':'214122',
'isDefault':'1'
}
post_data_code= urllib.parse.urlencode(post_data).encode(encoding='UTF8')
#发送请求
response = urllib.request.urlopen(request,data=post_data_code,timeout=5)
#保存网页内容
context = response.read().decode('UTF8')
#输出网页内容
#print(context)
context = eval(context)
if context['status']=='ok':
    print("添加地址成功")
else:
    print("添加地址失败")
    print(context)
