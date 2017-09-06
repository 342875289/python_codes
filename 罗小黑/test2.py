import random,time
random.seed ( 1503540711 )
print("".join(random.sample(['a','b','c','d','e','f','g','h','i','j'], 10)))
print(int(time.time()))

import hashlib   

m2 = hashlib.md5()   
m2.update('lxh-global.bjmanya.com:9009/user/login?account=qq342875289appid=100000check_code=device=iphonedevice_uuid1965FBA4-13AA-49C7-BC00-B6356627C74BosIOSos_vers10.3.3password000000source'.encode(encoding='utf_8', errors='strict'))   
print( m2.hexdigest()   )
#cd8929990165f5644f1c66c969efd300
for i in [3,10,13,20,23]:
    print(i)


