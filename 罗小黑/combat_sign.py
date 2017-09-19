import hashlib   

'''
{"Header":{"MsgID":14001},"Msg":{"TeamList":{},"LevelType":1,"LevelId":100003,"ForceId":10}}
{"Header":{"MsgID":14003},"Msg":{"
 RandomSeed":1505789748,
 "LevelId":100003,
 "ForceId":10,
 "Energy":100,
 "TeamList":{},
"Sign":"7c971d60e16c7aa46fcdd00c8cbeb2c1",
 "Result":3,
 "LevelType":1}}

'''

def getCombatSign():
    #appsecret=f01fbef4ed9b1061cb4aaebd60f54657
    m2 = hashlib.md5()   
    str = 'Energy:100ForceId:10LevelId:100003LevelType:1RandomSeed:1505789748Result:3TeamList:85af3ddb1d4c9c1c57f122b1544e1f3e'
    m2.update(str.encode(encoding='utf_8', errors='strict'))   
    return  m2.hexdigest()

if __name__ == "__main__":
    print(getCombatSign())
    print("7c971d60e16c7aa46fcdd00c8cbeb2c1")
    print(u'\u65e0\u5e2e\u6d3e')