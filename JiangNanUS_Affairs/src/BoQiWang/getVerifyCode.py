import urllib.request
import http.cookiejar
import json
import random
from PIL import Image
import io
import matplotlib.pyplot as plt

#加入对cookies的支持
cookieJarInMemory = http.cookiejar.CookieJar();
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookieJarInMemory));
urllib.request.install_opener(opener);

#url和数据编码
url='http://www.boqii.com/user/images/vcode/vcode.php'
data_values = {'update' : str( random.randint(1,1000)  )}
url_data = urllib.parse.urlencode(data_values)
#HTTP头部
http_headers = {'Host':'www.boqii.com',
'Connection':'keep-alive',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.8.2000 Chrome/30.0.1599.101 Safari/537.36',
'Content-Type':'application/x-www-form-urlencoded',
'Accept-Language':'zh-CN',
'Referer':'http://www.boqii.com/',
'DNT':'1'
}

#创建Request对象
request = urllib.request.Request(url = url+'?'+url_data,
                                 headers= http_headers)
#发送请求
response = urllib.request.urlopen(request)

#显示验证码
im_data = response.read()
file = io.BytesIO(im_data)
img=Image.open(file)
plt.imshow(img)
plt.show()
#人工输入验证码
vcode = input("请输入验证码")
print("验证码是"+vcode)



