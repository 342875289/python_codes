import urllib.request
import json
import time
import re
def getNums():
    param ={'x':1,
            'TeachinAll_sort':'xid.desc',
            'target':'navTab',
            '_':int(time.time()*1000),
            'page':1,
            'limit':1,}
    param_str = urllib.parse.urlencode(param) 
    url='http://jiangnan.91job.gov.cn/admin/teachin/manage2?'+param_str
    #创建Request对象
    request = urllib.request.Request(url)
    #添加数据
    #添加http header
    request.add_header('Host', 'jiangnan.91job.gov.cn')
    request.add_header('Accept', '*/*')
    request.add_header('Content-Type',' application/x-www-form-urlencoded')
    request.add_header('Referer','http://jiangnan.91job.gov.cn/admin/default/index')
    request.add_header('Cookie','UM_distinctid=15e60471d3a2c3-02ebee99dd6057-4a6b124f-1fa400-15e60471d3b847; admin=149f70d8f9702cae55a9441ef58560c3cf50d31da%3A4%3A%7Bi%3A0%3Bs%3A4%3A%225997%22%3Bi%3A1%3Bs%3A6%3A%22jyzdzx%22%3Bi%3A2%3Bi%3A2592000%3Bi%3A3%3Ba%3A10%3A%7Bs%3A13%3A%22validpassword%22%3Bb%3A1%3Bs%3A10%3A%22superadmin%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22realname%22%3Bs%3A13%3A%22%E5%B0%B1%E4%B8%9A%E5%B8%82%E5%9C%BA1%22%3Bs%3A7%3A%22belongs%22%3Bs%3A3%3A%22742%22%3Bs%3A5%3A%22value%22%3Ba%3A0%3A%7B%7Ds%3A6%3A%22perm_1%22%3Bs%3A1%3A%220%22%3Bs%3A5%3A%22phone%22%3Bs%3A11%3A%2218861821971%22%3Bs%3A10%3A%22department%22%3Bs%3A42%3A%22%E6%B1%9F%E5%8D%97%E5%A4%A7%E5%AD%A6%E5%B0%B1%E4%B8%9A%E5%88%9B%E4%B8%9A%E6%8C%87%E5%AF%BC%E6%9C%8D%E5%8A%A1%E4%B8%AD%E5%BF%83%22%3Bs%3A7%3A%22manager%22%3BN%3Bs%3A9%3A%22education%22%3Bs%3A2%3A%2211%22%3B%7D%7D; scan_teachin=a%3A1%3A%7Bi%3A136931%3Ba%3A3%3A%7Bs%3A3%3A%22xid%22%3Bs%3A6%3A%22136931%22%3Bs%3A12%3A%22company_name%22%3Bs%3A33%3A%22%E4%B8%8A%E6%B5%B7%E7%9B%AE%E8%BF%A9%E7%94%B5%E5%AD%90%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90...%22%3Bs%3A8%3A%22dateline%22%3Bi%3A1505899088%3B%7D%7D; CNZZDATA1259394577=48600896-1504850989-http%253A%252F%252Fjiangnan.91job.gov.cn%252F%7C1505894485; PHPSESSID2=gfchit8h4me505jusdcmtvbjm1')
    #发送请求
    response = urllib.request.urlopen(request,timeout=60)
    #保存网页内容
    context = response.read().decode('utf-8')
    #输出企业总数和页码数
    p_enterprise_num = re.compile(r'<span>条\D+(\d+)+\D+(\d+)页</span>')
    p_enterprise_id = re.compile(r'/teachin/view/id/(\d+)')
    nums = p_enterprise_num.search(context)
    enterprise_num = nums.group(1)
    #enterprise_page_num = nums.group(2)
    return int(enterprise_num)


def getEnterpriseInpages(page_number,page_items_limit = 50):
    param ={'x':1,
            'TeachinAll_sort':'xid.desc',
            'target':'navTab',
            '_':int(time.time()*1000),
            'page':page_number,
            'limit':page_items_limit,}
    param_str = urllib.parse.urlencode(param)
    url='http://jiangnan.91job.gov.cn/admin/teachin/manage2?'+param_str
    #创建Request对象
    request = urllib.request.Request(url)
    #添加数据
    #添加http header
    request.add_header('Host', 'jiangnan.91job.gov.cn')
    request.add_header('Accept', '*/*')
    request.add_header('Content-Type',' application/x-www-form-urlencoded')
    request.add_header('Referer','http://jiangnan.91job.gov.cn/admin/default/index')
    request.add_header('Cookie','UM_distinctid=15e60471d3a2c3-02ebee99dd6057-4a6b124f-1fa400-15e60471d3b847; admin=149f70d8f9702cae55a9441ef58560c3cf50d31da%3A4%3A%7Bi%3A0%3Bs%3A4%3A%225997%22%3Bi%3A1%3Bs%3A6%3A%22jyzdzx%22%3Bi%3A2%3Bi%3A2592000%3Bi%3A3%3Ba%3A10%3A%7Bs%3A13%3A%22validpassword%22%3Bb%3A1%3Bs%3A10%3A%22superadmin%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22realname%22%3Bs%3A13%3A%22%E5%B0%B1%E4%B8%9A%E5%B8%82%E5%9C%BA1%22%3Bs%3A7%3A%22belongs%22%3Bs%3A3%3A%22742%22%3Bs%3A5%3A%22value%22%3Ba%3A0%3A%7B%7Ds%3A6%3A%22perm_1%22%3Bs%3A1%3A%220%22%3Bs%3A5%3A%22phone%22%3Bs%3A11%3A%2218861821971%22%3Bs%3A10%3A%22department%22%3Bs%3A42%3A%22%E6%B1%9F%E5%8D%97%E5%A4%A7%E5%AD%A6%E5%B0%B1%E4%B8%9A%E5%88%9B%E4%B8%9A%E6%8C%87%E5%AF%BC%E6%9C%8D%E5%8A%A1%E4%B8%AD%E5%BF%83%22%3Bs%3A7%3A%22manager%22%3BN%3Bs%3A9%3A%22education%22%3Bs%3A2%3A%2211%22%3B%7D%7D; scan_teachin=a%3A1%3A%7Bi%3A136931%3Ba%3A3%3A%7Bs%3A3%3A%22xid%22%3Bs%3A6%3A%22136931%22%3Bs%3A12%3A%22company_name%22%3Bs%3A33%3A%22%E4%B8%8A%E6%B5%B7%E7%9B%AE%E8%BF%A9%E7%94%B5%E5%AD%90%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90...%22%3Bs%3A8%3A%22dateline%22%3Bi%3A1505899088%3B%7D%7D; CNZZDATA1259394577=48600896-1504850989-http%253A%252F%252Fjiangnan.91job.gov.cn%252F%7C1505894485; PHPSESSID2=gfchit8h4me505jusdcmtvbjm1')
    #发送请求
    response = urllib.request.urlopen(request,timeout=60)
    #保存网页内容
    context = response.read().decode('utf-8')
    #输出网页内容
    return context

def getOneEnterprise(enterprise_id):
    url='http://jiangnan.91job.gov.cn/admin/teachin/update/id/'+str(enterprise_id)
    #创建Request对象
    request = urllib.request.Request(url)
    #添加http header
    request.add_header('Host', 'jiangnan.91job.gov.cn')
    request.add_header('Accept', '*/*')
    request.add_header('Accept-Encoding', '*gzip,deflate')
    request.add_header('Content-Type',' application/x-www-form-urlencoded')
    request.add_header('Referer','http://jiangnan.91job.gov.cn/admin/default/index')
    request.add_header('Cookie','UM_distinctid=15e60471d3a2c3-02ebee99dd6057-4a6b124f-1fa400-15e60471d3b847; admin=149f70d8f9702cae55a9441ef58560c3cf50d31da%3A4%3A%7Bi%3A0%3Bs%3A4%3A%225997%22%3Bi%3A1%3Bs%3A6%3A%22jyzdzx%22%3Bi%3A2%3Bi%3A2592000%3Bi%3A3%3Ba%3A10%3A%7Bs%3A13%3A%22validpassword%22%3Bb%3A1%3Bs%3A10%3A%22superadmin%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22realname%22%3Bs%3A13%3A%22%E5%B0%B1%E4%B8%9A%E5%B8%82%E5%9C%BA1%22%3Bs%3A7%3A%22belongs%22%3Bs%3A3%3A%22742%22%3Bs%3A5%3A%22value%22%3Ba%3A0%3A%7B%7Ds%3A6%3A%22perm_1%22%3Bs%3A1%3A%220%22%3Bs%3A5%3A%22phone%22%3Bs%3A11%3A%2218861821971%22%3Bs%3A10%3A%22department%22%3Bs%3A42%3A%22%E6%B1%9F%E5%8D%97%E5%A4%A7%E5%AD%A6%E5%B0%B1%E4%B8%9A%E5%88%9B%E4%B8%9A%E6%8C%87%E5%AF%BC%E6%9C%8D%E5%8A%A1%E4%B8%AD%E5%BF%83%22%3Bs%3A7%3A%22manager%22%3BN%3Bs%3A9%3A%22education%22%3Bs%3A2%3A%2211%22%3B%7D%7D; scan_teachin=a%3A1%3A%7Bi%3A136931%3Ba%3A3%3A%7Bs%3A3%3A%22xid%22%3Bs%3A6%3A%22136931%22%3Bs%3A12%3A%22company_name%22%3Bs%3A33%3A%22%E4%B8%8A%E6%B5%B7%E7%9B%AE%E8%BF%A9%E7%94%B5%E5%AD%90%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90...%22%3Bs%3A8%3A%22dateline%22%3Bi%3A1505899088%3B%7D%7D; CNZZDATA1259394577=48600896-1504850989-http%253A%252F%252Fjiangnan.91job.gov.cn%252F%7C1505894485; PHPSESSID2=gfchit8h4me505jusdcmtvbjm1')
    #发送请求
    response = urllib.request.urlopen(request,timeout=60)
    #保存网页内容
    context = response.read().decode('utf-8')
    #输出网页内容
    return context
    
