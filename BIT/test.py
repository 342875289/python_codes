import urllib.request
import http.cookiejar
import json

#加入对cookies的支持
cookieJarInMemory = http.cookiejar.CookieJar();
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookieJarInMemory));
urllib.request.install_opener(opener);

url_login='http://lxh-global.bjmanya.com:9009/user/login'
#创建Request对象
request = urllib.request.Request(url_login)
#添加数据
#添加http header
request.add_header('Host', ' lxh-global.bjmanya.com:9009')
request.add_header('Accept', '*/*')
request.add_header('Content-Type',' application/x-www-form-urlencoded')


#POST_Data
post_data = {
'account': 'qq342875289',
'appid': '100000',
'check_code': '',
'device': 'iphone',
'device_uuid': '1965FBA4-13AA-49C7-BC00-B6356627C74B',
'os': 'IOS',
'os_vers': '10.3.3',
'password': '000000',
'source': '',
'sign': 'cd8929990165f5644f1c66c969efd300'
}

post_data_code= urllib.parse.urlencode(post_data).encode(encoding='UTF8')
#发送请求
response = urllib.request.urlopen(request,data=post_data_code,timeout=60)
#保存网页内容
context = response.read().decode('unicode_escape')
#输出网页内容
print(context)
context_json = json.loads(context)
print("登录状态:"+context_json['message'])

#输出数据--userid,token,expire
userdata = context_json['data']




#获取ticket
url='http://lxh-global.bjmanya.com:9002/index.php'+'?'+'ChannelId=70001&Token='+str(userdata['userid'])+';'+str(userdata['token'])
#创建Request对象
request = urllib.request.Request(url)
#添加数据
#添加http header
request.add_header('Host', ' lxh-global.bjmanya.com:9002')
request.add_header('Accept', '*/*')
request.add_header('Content-Type',' application/x-www-form-urlencoded')


#POST_Data
post_data = {
'appid': '100000',
'check_code': '',
'device': 'iphone',
'device_uuid': '1965FBA4-13AA-49C7-BC00-B6356627C74B',
'os': 'IOS',
'os_vers': '10.3.3',
'password': '000000',
'source': '',
'sign': 'cd8929990165f5644f1c66c969efd300'
}

post_data_code= urllib.parse.urlencode(post_data).encode(encoding='UTF8')
#发送请求
response = urllib.request.urlopen(request,data=post_data_code,timeout=60)
#保存网页内容
context = response.read().decode('unicode_escape')
#输出网页内容
print(context)
token = json.loads(context)['Msg']['Ticket']
print('token:'+token)



#获取通知，服务器列表-40001
verson = '\"4.0.23(4.11316.11984)\"'
url='http://lxh-global.bjmanya.com:9001/?data={"Header":{"MsgID":40001},"Msg":{"Platform":12,"Version":'+verson+',"Channel":70001,"AccountId":'+'"'+str(userdata['userid'])+'","Account":"'+userdata['bind_name']+'"}}'
#创建Request对象
request = urllib.request.Request(url)
#添加数据
#添加http header
request.add_header('Host', 'lxh-global.bjmanya.com:9001')
request.add_header('Accept', '*/*')
request.add_header('Content-Type',' application/x-www-form-urlencoded')
#POST_Data
post_data = {}
post_data_code= urllib.parse.urlencode(post_data).encode(encoding='UTF8')
#发送请求
response = urllib.request.urlopen(request,data=post_data_code,timeout=60)
#保存网页内容
context = response.read().decode('utf-8')
#输出网页内容
print(context)


#获取公告-40003
url='http://lxh-global.bjmanya.com:9001/?data={"Header":{"MsgID":40003},"Msg":{"Platform":12,"ServerId":120010,"Channel":70001}}'
#创建Request对象
request = urllib.request.Request(url)
#添加数据
#添加http header
request.add_header('Host', 'lxh-global.bjmanya.com:9001')
request.add_header('Accept', '*/*')
request.add_header('Content-Type',' application/x-www-form-urlencoded')
#POST_Data
post_data = {}
post_data_code= urllib.parse.urlencode(post_data).encode(encoding='UTF8')
#发送请求
response = urllib.request.urlopen(request,data=post_data_code,timeout=60)
#保存网页内容
context = response.read().decode('utf-8')
#输出网页内容
print(context)


#获取账号信息-40005
url='http://lxh-global.bjmanya.com:9001/?data={"Header":{"MsgID":40005},"Msg":{"Platform":12,"AccountId":'+'"'+str(userdata['userid'])+'","Channel":70001}}'
#创建Request对象
request = urllib.request.Request(url)
#添加数据
#添加http header
request.add_header('Host', 'lxh-global.bjmanya.com:9001')
request.add_header('Accept', '*/*')
request.add_header('Content-Type',' application/x-www-form-urlencoded')
#POST_Data
post_data = {}
post_data_code= urllib.parse.urlencode(post_data).encode(encoding='UTF8')
#发送请求
response = urllib.request.urlopen(request,data=post_data_code,timeout=60)
#保存网页内容
context = response.read().decode('utf-8')
#输出网页内容
print(context)



#未知-40009
url='http://lxh-global.bjmanya.com:9001/?data={"Header":{"MsgID":40009},"Msg":{"Platform":12,"AccountId":'+'"'+str(userdata['userid'])+'","Channel":70001}}'
#创建Request对象
request = urllib.request.Request(url)
#添加数据
#添加http header
request.add_header('Host', 'lxh-global.bjmanya.com:9001')
request.add_header('Accept', '*/*')
request.add_header('Content-Type',' application/x-www-form-urlencoded')
#POST_Data
post_data = {}
post_data_code= urllib.parse.urlencode(post_data).encode(encoding='UTF8')
#发送请求
response = urllib.request.urlopen(request,data=post_data_code,timeout=60)
#保存网页内容
context = response.read().decode('utf-8')
#输出网页内容
print(context)

