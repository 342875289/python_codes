import urllib.request
import json

#HTTPCookiesProcessor
#HTTPRedirectHandler
url='http://www.pocketuni.net/index.php'

#POST /index.php?app=event&mod=Front&act=vote HTTP/1.1
#对data加入url编码
data_values = {'app' : 'event','mod' : 'Front','act' : 'vote '}
data = urllib.parse.urlencode(data_values)
#创建Request对象
request = urllib.request.Request(url+'?'+data)
#添加数据
#request.adddata('username','123456')
#添加http header
request.add_header('Host', 'sytu.pocketuni.net')
request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.8.2000 Chrome/30.0.1599.101 Safari/537.36')
request.add_header('Connection', 'keep-alive')
request.add_header('Content-Length','19')
request.add_header('Accept', '*/*')
request.add_header('Origin','http://sytu.pocketuni.net')
request.add_header('Content-Type','application/x-www-form-urlencoded')
request.add_header('DNT','1')
#！
#！
#！
request.add_header('Referer','http://sytu.pocketuni.net/index.php?app=event&mod=Front&act=index&id=167394&uid=2540412')

request.add_header('X-Requested-With','XMLHttpRequest')
request.add_header('Accept-Language','zh-CN')
request.add_header('Cookie', 'PHPSESSID=4adcb2a5571b6b6724600; TS_think_language=zh-CN;TS_LOGGED_USER=fQkWi20ie94JrnxRpBXxIIX88;Hm_lvt_dd3ea352543392a029ccf9da1be54a50=1461215406,1461300191,1461414536,1461417954;Hm_lpvt_dd3ea352543392a029ccf9da1b')

#POST_Data
post_data = {'id' : '167394',
'pid' : '37089'
}
post_data_code= urllib.parse.urlencode(post_data).encode(encoding='UTF8')

#发送请求
response = urllib.request.urlopen(request,data=post_data_code)
the_page = response.read()
print(the_page.decode('UTF8'))

status_vote=json.loads(the_page.decode('UTF8'))
#判断投票是否成功
if(status_vote['status']=='1'):print('投票成功')                         
else:print('投票失败')  
