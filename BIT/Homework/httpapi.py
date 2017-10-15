import urllib.request
import http.cookiejar
import json

ip1  = '123.207.255.131'
ip2  = '127.0.0.1'
ip = ip1
#加入对cookies的支持
cookieJarInMemory = http.cookiejar.CookieJar();
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookieJarInMemory));
urllib.request.install_opener(opener);


param ={'username':'test',
        'password':'test',
        }
post_data_code= urllib.parse.urlencode(param).encode(encoding='UTF8')
url='http://'+ip+':8000/login'
request = urllib.request.Request(url)
request.add_header('Accept', '*/*')
request.add_header('Content-Type',' application/x-www-form-urlencoded')
response = urllib.request.urlopen(request,data=post_data_code)
context = response.read().decode('utf-8')
print(context)


url='http://'+ip+':8000/book_list'
request = urllib.request.Request(url)
request.add_header('Accept', '*/*')
request.add_header('Content-Type',' application/x-www-form-urlencoded')
response = urllib.request.urlopen(request)
context = response.read().decode('utf-8')
print(context)


param ={'book_id':4,
        'times':1,
        }
post_data_code= urllib.parse.urlencode(param).encode(encoding='UTF8')
url='http://'+ip+':8000/purchase'
request = urllib.request.Request(url)
request.add_header('Accept', '*/*')
request.add_header('Content-Type',' application/x-www-form-urlencoded')
response = urllib.request.urlopen(request,data=post_data_code)
context = response.read().decode('utf-8')
print(context)



param ={'book_id':4,
        }
post_data_code= urllib.parse.urlencode(param).encode(encoding='UTF8')
url='http://'+ip+':8000/download'
request = urllib.request.Request(url)
request.add_header('Accept', '*/*')
request.add_header('Content-Type',' application/x-www-form-urlencoded')
response = urllib.request.urlopen(request,data=post_data_code)
context = response.read().decode('utf-8')
print(context)





    
