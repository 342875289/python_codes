import urllib.request
import http.cookiejar
import json

def puVote(username,userpassword,id,votepid,isVote=1):
#加入对cookies的支持
    cookieJarInMemory = http.cookiejar.CookieJar();
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookieJarInMemory));
    urllib.request.install_opener(opener);
    
    url_login='http://www.pocketuni.net/index.php'
#http://www.pocketuni.net/index.php?app=home&mod=Public&act=doLogin
#对data加入url编码
    data_values = {'app' : 'home','mod' : 'Public','act' : 'doLogin'}
    data = urllib.parse.urlencode(data_values)
#创建Request对象
    request = urllib.request.Request(url_login+'?'+data)
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
    'number' : username,
    'password' : userpassword,
    'login' : '登 录',
    '__hash__' : '0619e28f8d69e86729324c6d2c21698e',
    }
    post_data_code= urllib.parse.urlencode(post_data).encode(encoding='UTF8')
    
#发送请求
    response = urllib.request.urlopen(request,data=post_data_code,timeout=60)
#保存网页内容
    context = response.read().decode('UTF8')
#输出网页内容
#print(context)
    
#找到title部分
    title_begin=context.find('<title>')
#print(title_begin)
    title_end=context.find('</title>')
#print(title_end)
#通过title部分的不同判断是否登陆成功
    login_state=context.find('我',title_begin,title_end)
    if(login_state!=-1):
       # print('登陆成功')
        login_state=1
    else:
       # print('登陆失败')
        login_state=0
    #print ("显示cookies",cookieJarInMemory)
    
    
    if((isVote==1) and (login_state==1) ):
    #投票
        
    #投票的url
        url_vote='http://www.pocketuni.net/index.php'
    #对data加入url编码
    #投票的url参数
    #POST /index.php?app=event&mod=Front&act=vote HTTP/1.1
        data_values = {'app' : 'event','mod' : 'Front','act' : 'vote '}
        data = urllib.parse.urlencode(data_values)
    #创建Request对象
        request = urllib.request.Request(url_vote+'?'+data)
    #添加http header
        request.add_header('Host', 'sytu.pocketuni.net')
        request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.8.2000 Chrome/30.0.1599.101 Safari/537.36')
        request.add_header('Connection', 'keep-alive')
        request.add_header('Content-Length','19')
        request.add_header('Accept', '*/*')
        request.add_header('Origin','http://sytu.pocketuni.net')
        request.add_header('Content-Type','application/x-www-form-urlencoded')
        request.add_header('DNT','1')
        
    #request.add_header('Referer','http://sytu.pocketuni.net/index.php?app=event&mod=Front&act=index&id=167394&uid=2540412')
        request.add_header('X-Requested-With','XMLHttpRequest')
        request.add_header('Accept-Language','zh-CN')
        
    #request.add_header('Cookie', 'PHPSESSID=4adcb2a5571b6b6724600; TS_think_language=zh-CN;TS_LOGGED_USER=fQkWi20ie94JrnxRpBXxIIX88;Hm_lvt_dd3ea352543392a029ccf9da1be54a50=1461215406,1461300191,1461414536,1461417954;Hm_lpvt_dd3ea352543392a029ccf9da1b')
        
    #POST_Data
        post_data = {'id' : id,#167451
        'pid' : votepid
        }
        post_data_code= urllib.parse.urlencode(post_data).encode(encoding='UTF8')
        
    #发送请求
        response = urllib.request.urlopen(request,data=post_data_code,timeout=60)#timeout单位是秒
        voteResult = response.read().decode('UTF8')
       # print(voteResult)
        
        status_vote=json.loads(voteResult)
    #判断投票是否成功
        if(status_vote['status']==1):
           # print('投票成功')   
            vote_state=1
        else:
           # print('投票失败')  
            vote_state=0
    else:
        vote_state=-1    return {'login_state' : login_state,'vote_state' : vote_state};

    




