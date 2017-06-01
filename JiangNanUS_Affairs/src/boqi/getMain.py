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
print(get_vcode_num)



#url和数据编码
url='http://www.boqii.com/user/images/vcode/vcode.php'
data_values = {'update' : get_vcode_num }
url_data = urllib.parse.urlencode(data_values)
#HTTP头部
http_headers = {'Host':'www.boqii.com',
'Connection':'keep-alive',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.8.2000 Chrome/30.0.1599.101 Safari/537.36',
'Content-Type':'application/x-www-form-urlencoded',
'Accept-Language':'zh-CN',
'Referer':'http://www.boqii.com/',
'DNT':'1'
}

#创建Request对象
request = urllib.request.Request(url = url+'?'+url_data,
                                 headers= http_headers)
#发送请求
response = urllib.request.urlopen(request)

im_data = response.read()
file = io.BytesIO(im_data)
img=Image.open(file)
plt.imshow(img)
plt.show()

#人工输入验证码
vcode = input()
print("验证码是"+vcode)


url_login='http://www.boqii.com/site/User/usercenter'
#HTTP头部
http_headers = {'Host':'www.boqii.com',
'Connection':'keep-alive',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.8.2000 Chrome/30.0.1599.101 Safari/537.36',
'Content-Type':'application/x-www-form-urlencoded',
'Accept-Language':'zh-CN',
'Referer':'http://www.boqii.com/',
'DNT':'1'
}
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
print(context)

