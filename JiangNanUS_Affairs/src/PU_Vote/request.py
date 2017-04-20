import urllib.request

#HTTPCookiesProcessor
#HTTPRedirectHandler
url='http://www.pocketuni.net/index.php'


#http://www.pocketuni.net/index.php?app=home&mod=Public&act=doLogin

#对data加入url编码
data_values = {'app' : 'home','mod' : 'Public','act' : 'doLogin'}
data = urllib.parse.urlencode(data_values)
#创建Request对象
request = urllib.request.Request(url+'?'+data)
#添加数据
#request.adddata('username','123456')
#添加http header
#request.add_header('User-Agent','Mozilla/5.0')
request.add_header('Host', 'www.pocketuni.net')
request.add_header('Connection', 'keep-alive')
request.add_header('Content-Length','161')
request.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.8.2000 Chrome/30.0.1599.101 Safari/537.36')
request.add_header('Origin','http://www.pocketuni.net')
request.add_header('Content-Type','application/x-www-form-urlencoded')
request.add_header('DNT','1')
request.add_header('Referer','http://www.pocketuni.net/')

#还需要解码
#request.add_header('Accept-Encoding','gzip,deflate')
request.add_header('Accept-Language','zh-CN')

request.add_header('Cookie', 'PHPSESSID=4adcb2a5571b6b6724600; TS_think_language=zh-CN; Hm_lvt_dd3ea352543392a029ccf9da1be54a50=1461215406,1461300191,1461414536,1461417954; Hm_lpvt_dd3ea352543392a029ccf9da1be54a50=1461419866')

#POST_Data
post_data = {'school' : '江南大学',
'sid' : '526',
'number' : '1030615434',
'password' : '150016',
'login' : '登 录',
'__hash__' : '0619e28f8d69e86729324c6d2c21698e',
}
post_data_code= urllib.parse.urlencode(post_data).encode(encoding='UTF8')

#发送请求
response = urllib.request.urlopen(request,data=post_data_code)
the_page = response.read()
print(the_page.decode('UTF8'))