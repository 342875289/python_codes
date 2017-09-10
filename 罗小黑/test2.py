import random,time
random.seed ( 1503540711 )
print("".join(random.sample(['a','b','c','d','e','f','g','h','i','j'], 10)))
print(int(time.time()))

import hashlib   

m2 = hashlib.md5()   
#f01fbef4ed9b1061cb4aaebd60f54657
'''
  var_13_1.appid = INPUT_VAR_0_.appid
    var_13_1.account = INPUT_VAR_0_.account
    var_13_1.password = INPUT_VAR_0_.pwd
    var_13_1.check_code = INPUT_VAR_0_.check_code
    var_13_1.source = INPUT_VAR_0_.source
    var_13_1.device = INPUT_VAR_0_.device
    var_13_1.device_uuid = INPUT_VAR_0_.device_uuid
    var_13_1.os = INPUT_VAR_0_.os
    var_13_1.os_vers = INPUT_VAR_0_.os_vers 

sign=8f2e144d2962539a2ab1491596c0a22c    
'''
m2.update('Energy=90#NodeId=32#RandomSeed=1504891131#Result=3#f01fbef4ed9b1061cb4aaebd60f54657'.encode(encoding='utf_8', errors='strict'))   
print( m2.hexdigest()   )


