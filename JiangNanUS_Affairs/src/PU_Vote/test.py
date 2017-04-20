import urllib.request
import json
import re
link = "http://jiangnan.91job.gov.cn/jobfair/view/id/26225"
print(link)
url=link
#创建Request对象
request = urllib.request.Request(url)
request.add_header('Content-Type','application/x-www-form-urlencoded')
response = urllib.request.urlopen(request)
the_page = response.read()
enterprise_data = the_page.decode('UTF8')
#print(enterprise_data)
date = "2016-09-29"
p_item_detail = re.compile(r'<span>'+date+' ((.){11})</span>(.)+举办地址.<span>((.)+)</span>')
p_item_detail = re.compile(date)

test = "<li>具体时间：<span>2016-09-29 13:00-16:30</span></li><li>举办城市：<span>江苏省 - 无锡市</span></li><li>举办地址：<span>北活音乐厅、北活F105</span></li>"
details = p_item_detail.search(test)
time=details.group()
location=details.group()
print(time)
print(location)


a="16:25"
b="13:05"
c=int(a[0:2])+int(b[0:2])
print(a[0:2]) 
print(str(c)) 
c=int(a[3:5])+int(b[3:5])
print(str(c)) 
print(range(8))
#print(list_zhaopin.sort(key=None, reverse=False))


#<li>具体时间：<span>2016-09-29 13:00-16:30</span></li>
#<li>举办城市：<span>江苏省 - 无锡市</span></li>
#<li>举办地址：<span>北活音乐厅、北活F105</span></li>