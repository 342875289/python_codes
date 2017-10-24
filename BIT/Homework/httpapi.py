import urllib.request
import http.cookiejar
import json
import ssl

ip1  = '123.207.255.131'
ip2  = '127.0.0.1'
ip = ip1
#加入对cookies的支持
cookieJarInMemory = http.cookiejar.CookieJar();
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookieJarInMemory));
urllib.request.install_opener(opener);

ssl._create_default_https_context = ssl._create_unverified_context
param ={'username':'test',
        'password':'test',
        }
post_data_code= urllib.parse.urlencode(param).encode(encoding='UTF8')
url='https://'+ip+'/login'
request = urllib.request.Request(url)
request.add_header('Accept', '*/*')
request.add_header('Content-Type',' application/x-www-form-urlencoded')
response = urllib.request.urlopen(request,data=post_data_code)
context = response.read().decode('utf-8')
print(context)

'''
url='https://'+ip+'/book_list'
request = urllib.request.Request(url)
request.add_header('Accept', '*/*')
request.add_header('Content-Type',' application/x-www-form-urlencoded')
response = urllib.request.urlopen(request)
context = response.read().decode('utf-8')
print(context)
'''
'''
param ={'book_id':4,
        'times':1,
        }
post_data_code= urllib.parse.urlencode(param).encode(encoding='UTF8')
url='https://'+ip+'/purchase'
request = urllib.request.Request(url)
request.add_header('Accept', '*/*')
request.add_header('Content-Type',' application/x-www-form-urlencoded')
response = urllib.request.urlopen(request,data=post_data_code)
context = response.read().decode('utf-8')
print(context)
'''

'''
param ={'book_id':4,
        }
post_data_code= urllib.parse.urlencode(param).encode(encoding='UTF8')
url='http://'+ip+'/download'
request = urllib.request.Request(url)
request.add_header('Accept', '*/*')
request.add_header('Content-Type',' application/x-www-form-urlencoded')
response = urllib.request.urlopen(request,data=post_data_code)
context = response.read().decode('utf-8')
print(context)

'''
'''
param ={'book_id':4,
        'mac':'91-90-96-D9-9B-07'
        }
post_data_code= urllib.parse.urlencode(param).encode(encoding='UTF8')
url='http://'+ip+'/key'
request = urllib.request.Request(url)
request.add_header('Accept', '*/*')
request.add_header('Content-Type',' application/x-www-form-urlencoded')
response = urllib.request.urlopen(request,data=post_data_code)
context = response.read().decode('utf-8')
print(context)
'''

'''
param ={'book_id':6,
        }
post_data_code= urllib.parse.urlencode(param).encode(encoding='UTF8')
url='https://'+ip+'/getcode'
request = urllib.request.Request(url)
request.add_header('Accept', '*/*')
request.add_header('Content-Type',' application/x-www-form-urlencoded')
response = urllib.request.urlopen(request,data=post_data_code)
context = response.read().decode('unicode_escape')
print(context)
'''
'''
param ={'code':'l5W0qBwHftcTzZnjVMI3JYXUyDvrORp7',
        }
post_data_code= urllib.parse.urlencode(param).encode(encoding='UTF8')
url='https://'+ip+'/usecode'
request = urllib.request.Request(url)
request.add_header('Accept', '*/*')
request.add_header('Content-Type',' application/x-www-form-urlencoded')
response = urllib.request.urlopen(request,data=post_data_code)
context = response.read().decode('unicode_escape')
print(context)
'''
'''
data = open('test.txt','rb').read()
param ={'book_name':'111',
        'key':'J2TXVRPX0NV4H0N0Z8282R00F8D8T84H',
        'ebook':data}
post_data_code= urllib.parse.urlencode(param).encode(encoding='UTF8')
url='https://'+ip+'/upload'
request = urllib.request.Request(url)
request.add_header('Accept', '*/*')
request.add_header('Content-Type',' application/x-www-form-urlencoded')
response = urllib.request.urlopen(request,data=post_data_code)
context = response.read().decode('unicode_escape')
print(context)
'''