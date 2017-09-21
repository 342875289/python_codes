import urllib.request
import http.cookiejar
import json
import time

from bs4 import BeautifulSoup

page_number = 1
page_items_limit = 50
enterprise_items = {}

#加入对cookies的支持
cookieJarInMemory = http.cookiejar.CookieJar();
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookieJarInMemory));
urllib.request.install_opener(opener);
param ={'x':1,
        'page':page_number,
        'limit':page_items_limit,
        'target':'navTab',
        '_':int(time.time()*1000),
        
        }
param_str = urllib.parse.urlencode(param)
url='http://jiangnan.91job.gov.cn/admin/teachin/update/id/139771/rel/manage2?'+param_str
#创建Request对象
request = urllib.request.Request(url)
#添加数据
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
#print(context)

soup = BeautifulSoup(context,'html.parser')
trs = soup.find_all('div',attrs={"class": "row"})

for tr in trs:
    labels = tr.find_all('label',attrs={"class": "label required"})
    options = tr.find_all('option',attrs={"selected": "selected"})
    #print(tr)
    print(labels)
    print(options)
'''
for tr in trs:
    tds = tr.find_all('td')
    department = tds[12].get_text().strip()
    if department != '江南大学就业创业指导服务中心':
        continue
    enterprise_items['name']                = tds[1].get_text().strip()
    enterprise_items['href']                = tds[1].a['href']
    enterprise_items['person']              = tds[2].get_text().strip()
    enterprise_items['phone']               = tds[3].get_text().strip()
    enterprise_items['time_display']        = tds[4].get_text().strip()
    enterprise_items['place_display']       = tds[5].get_text().strip()
    enterprise_items['time_writtenTest']    = tds[6].get_text().strip()
    enterprise_items['place_writtenTest']   = tds[7].get_text().strip()
    enterprise_items['time_faceTest']       = tds[8].get_text().strip()
    enterprise_items['place_faceTest']      = tds[9].get_text().strip()
    enterprise_items['department']          = department
    enterprise_items['state_comfirm']       = tds[13].get_text().strip()
    if enterprise_items['place_display'] == '未分配':
        enterprise_items['place_display'] = ''
    print(enterprise_items)
'''