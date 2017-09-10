import hashlib   

def getLoginSign(account):
    #appsecret=f01fbef4ed9b1061cb4aaebd60f54657
    m2 = hashlib.md5()   
    str = 'account='+account+'#appid=100000#check_code=#device=iphone#device_uuid=1965FBA4-13AA-49C7-BC00-B6356627C74B#os=IOS#os_vers=10.3.3#password=000000#source=#f01fbef4ed9b1061cb4aaebd60f54657'
    m2.update(str.encode(encoding='utf_8', errors='strict'))   
    return  m2.hexdigest()

if __name__ == "__main__":
    print(getLoginSign("mingg7"))
