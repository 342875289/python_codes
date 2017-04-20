import urllib.request
import json
import re

#投票页面ID
id="42047"
#投票项目总页数
page_num=8
allpid_list = ""

for p in range(1,page_num+1):
    url_login='http://sytu.pocketuni.net/index.php'
    #http://www.pocketuni.net/index.php?app=home&mod=Public&act=doLogin
    #对data加入url编码
    data_values = {'app' : 'event','mod' : 'Front','act' : 'player','id':'42047','p':p}
    data = urllib.parse.urlencode(data_values)
    #创建Request对象
    request = urllib.request.Request(url_login+'?'+data)
    #添加数据
    #request.adddata('username','123456')
    #添加http header
    #request.add_header('User-Agent','Mozilla/5.0')
    request.add_header('Host', 'sytu.pocketuni.net')
    request.add_header('Connection', 'keep-alive')
    request.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.8.2000 Chrome/30.0.1599.101 Safari/537.36')
    request.add_header('Content-Type','application/x-www-form-urlencoded')
    request.add_header('DNT','1')
    request.add_header('Referer','http://sytu.pocketuni.net/index.php?app=event&mod=Front&act=player&id=42047')
    
    #还需要解码
    #request.add_header('Accept-Encoding','gzip,deflate')
    request.add_header('Accept-Language','zh-CN')
    
    request.add_header('Cookie', 'PHPSESSID=4b4b00a05802f3d4d2d41; TS_think_language=zh-CN; route=630b8b083685b9dab3a71e45df49954b; Hm_lvt_dd3ea352543392a029ccf9da1be54a50=1476588503; Hm_lpvt_dd3ea352543392a029ccf9da1be54a50=1476589936')
    
    #POST_Data
    #发送请求
    response = urllib.request.urlopen(request,timeout=60)
    #保存网页内容
    context = response.read().decode('UTF8')
    #输出网页内容
    #print(context)
    #context ='=Front&act=playerDetails&id=42047&pid=5044asda" ti=Front&act=playerDetails&id=42047&pid=5044432asda" ti=Front&act=playerDetails&id=42047&pid=504411 " ti'
    searchPid = re.compile(r'pid=(\d+)\D')    
    pid_list=searchPid.findall(context)
    allpid_list = allpid_list +  "','".join(pid_list)
    if(p!=page_num):
        allpid_list = allpid_list + "','"
print(allpid_list)

