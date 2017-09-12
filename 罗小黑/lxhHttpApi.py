import urllib.request
import http.cookiejar
import json
import time
import hashlib

#加入对cookies的支持
cookieJarInMemory = http.cookiejar.CookieJar();
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookieJarInMemory));
urllib.request.install_opener(opener);

def getToken(username,device_uuid,sign,isdebug = 0):
    
    version_str = "4.0.25(4.11316.12262)"
    version = '\"4.0.25(4.11316.12262)\"'
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
    'account': username,
    'appid': '100000',
    'check_code': '',
    'device': 'iphone',
    'device_uuid': device_uuid,
    'os': 'IOS',
    'os_vers': '10.3.3',
    'password': '000000',
    'source': '',
    'sign': sign
    }
    
    post_data_code= urllib.parse.urlencode(post_data).encode(encoding='UTF8')
    #发送请求
    response = urllib.request.urlopen(request,data=post_data_code,timeout=60)
    #保存网页内容
    context = response.read().decode('unicode_escape')
    context_json = json.loads(context)
    print(username+",登录状态: "+context_json['message'])
    #输出数据--userid,token,expire
    userdata = context_json['data']
    if isdebug == 1:
        #输出内容
        print(context)
    
    
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
    'device_uuid': device_uuid,
    'os': 'IOS',
    'os_vers': '10.3.3',
    'password': '000000',
    'source': '',
    'sign': sign
    }
    
    post_data_code= urllib.parse.urlencode(post_data).encode(encoding='UTF8')
    #发送请求
    response = urllib.request.urlopen(request,data=post_data_code,timeout=60)
    #保存网页内容
    context = response.read().decode('unicode_escape')
    ticket = json.loads(context)['Msg']['Ticket']
    print('获取的token为:'+ticket)
    
    if isdebug == 1:
        #输出网页内容
        print(context)
    
    #获取通知，服务器列表-40001
    url='http://lxh-global.bjmanya.com:9001/?data={"Header":{"MsgID":40001},"Msg":{"Platform":12,"Version":'+version+',"Channel":70001,"AccountId":'+'"'+str(userdata['userid'])+'","Account":"'+userdata['bind_name']+'"}}'
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
    if isdebug == 1:
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
    if isdebug == 1:
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
    #print(context)
    
    
    
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
    #print(context)
    
    account_data = {'ticket':ticket,'account_id':str(userdata['userid']),'version_str':version_str}
    return account_data

def report(username,device_uuid,sign,server_num,isdebug = 0):
    #获取账号信息-40005
    url='http://lxh-global.bjmanya.com:9006/report'
    #创建Request对象
    request = urllib.request.Request(url)
    #添加数据
    #添加http header
    request.add_header('Host', 'lxh-global.bjmanya.com:9006')
    request.add_header('Accept', '*/*')
    request.add_header('Content-Type',' application/x-www-form-urlencoded')
    #POST_Data
    post_data = {
        'channel':'70001',
        'device':'iphone',
        'deviceuuid':device_uuid,
        'dtype':'3',
        'fun':'PostData',
        'groupid':120000+server_num,
        'os':'IOS',
        'osvers':'10.3.3',
        'time':str(int(time.time())),
        'sign':sign
        }
    post_data_code= urllib.parse.urlencode(post_data).encode(encoding='UTF8')
    #发送请求
    response = urllib.request.urlopen(request,data=post_data_code,timeout=60)
    #保存网页内容
    context = response.read().decode('utf-8')
    #输出网页内容
    print(context)

def ttt():
    #获取账号信息-40005
    url='http://lxh-global.bjmanya.com:9006/report'
    #创建Request对象
    request = urllib.request.Request(url)
    #添加数据
    #添加http header
    request.add_header('Host', 'lxh-global.bjmanya.com:9006')
    request.add_header('Accept', '*/*')
    request.add_header('Content-Type',' application/x-www-form-urlencoded')
    #POST_Data
    post_data = {
        'channel':'70001',
        'device':'iphone',
        'deviceuuid':'C4BAAFE8-C98D-49C2-B30F-1A7EA5364BAE',
        'dtype':'3',
        'fun':'PostData',
        'groupid':'120010',
        'os':'IOS',
        'osvers':'10.3.3',
        'time':'1503074367',
        'sign':'c74151bc7cb75ebe8b0acc8d2fdac44e'
        }
    post_data_code= urllib.parse.urlencode(post_data).encode(encoding='UTF8')
    #发送请求
    response = urllib.request.urlopen(request,data=post_data_code,timeout=60)
    #保存网页内容
    context = response.read().decode('utf-8')
    #输出网页内容
    print(context)
    
def getLoginSign(account):
    #appsecret=f01fbef4ed9b1061cb4aaebd60f54657
    m2 = hashlib.md5()   
    str = 'account='+account+'#appid=100000#check_code=#device=iphone#device_uuid=1965FBA4-13AA-49C7-BC00-B6356627C74B#os=IOS#os_vers=10.3.3#password=000000#source=#f01fbef4ed9b1061cb4aaebd60f54657'
    m2.update(str.encode(encoding='utf_8', errors='strict'))   
    return  m2.hexdigest()


def getRegisterSign(account):
    #appsecret=f01fbef4ed9b1061cb4aaebd60f54657
    m2 = hashlib.md5()   
    str = 'account='+account+'#account_type=1#appid=100000#check_code=#device=iphone#device_uuid=1965FBA4-13AA-49C7-BC00-B6356627C74B#os=IOS#os_vers=10.3.3#password=000000#source=#f01fbef4ed9b1061cb4aaebd60f54657'
    m2.update(str.encode(encoding='utf_8', errors='strict'))   
    return  m2.hexdigest()


def RegisterAccount(account):
    #注册账户
    url='http://lxh-global.bjmanya.com:9009/user/register'
    #创建Request对象
    request = urllib.request.Request(url)
    #添加数据
    #添加http header
    request.add_header('Host', 'lxh-global.bjmanya.com:9009')
    request.add_header('Accept', '*/*')
    request.add_header('Content-Type',' application/x-www-form-urlencoded')
    #POST_Data
    post_data = {
        'account':account,
        'account_type':'1',
        'appid':'100000',
        'check_code':'',
        'device':'iphone',
        'device_uuid':'1965FBA4-13AA-49C7-BC00-B6356627C74B',
        'os':'IOS',
        'os_vers':'10.3.3',
        'password':'000000',
        'source':'',
        'sign': getRegisterSign(account)
        }
    post_data_code= urllib.parse.urlencode(post_data).encode(encoding='UTF8')
    #发送请求
    response = urllib.request.urlopen(request,data=post_data_code,timeout=60)
    #保存网页内容
    context = response.read().decode('unicode_escape')
    #输出网页内容
    #print(context)
    context_json = json.loads(context)
    if context_json['status']==0 :
        #print("新账号"+account+"注册成功")
        return True
    else:
        #print("注册失败,原因为:"+context_json['message'])
        return False

if __name__ == "__main__":
    count_success = 0
    count_failed = 0
    for i in range( 1 , 2   +1):
        account = 'minggttttt'+str(i)
        if(RegisterAccount(account)) :
            context_json = json.loads('{"account_name":"mingg1","device_id":"1965FBA4-13AA-49C7-BC00-B6356627C74B","sign":"3ec7cce0b2274e4f3311aa00ccaf0ecf"}')
            context_json['account_name'] = account
            context_json['sign'] = getLoginSign(account)
            print(context_json)
            count_success = count_success + 1
        else:
            count_failed = count_failed + 1 
    print("注册完成,"+"成功:"+str(count_success)+"个,失败:"+str(count_failed))