import hashlib   

import hashlib   

def getRegisterSign(account):
    #appsecret=f01fbef4ed9b1061cb4aaebd60f54657
    m2 = hashlib.md5()   
    str = 'account='+account+'#account_type=1#appid=100000#check_code=#device=iphone#device_uuid=1965FBA4-13AA-49C7-BC00-B6356627C74B#os=IOS#os_vers=10.3.3#password=000000#source=#f01fbef4ed9b1061cb4aaebd60f54657'
    m2.update(str.encode(encoding='utf_8', errors='strict'))   
    return  m2.hexdigest()

if __name__ == "__main__":
    print(getRegisterSign("tttttt123"))


'''
POST /user/register HTTP/1.1
Host: lxh-global.bjmanya.com:9009
Accept: */*
Content-Length: 204
Content-Type: application/x-www-form-urlencoded

{"status":0,"message":"\u6210\u529f","data":{"userid":86847321,"token":"2b6582da95e0635a1ef713d5d915ee65","expire":1506185245,"bind_name":"tttttt123","bind_email":"","bind_phone":""}}
'''
