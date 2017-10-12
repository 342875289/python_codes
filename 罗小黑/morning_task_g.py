import websocket
import _thread
import time
import json


import lxhWebsocketApi
import lxh_growup_api
#记录账号信息
account = [ {'account_name':"mingg1",'device_id':"1965FBA4-13AA-49C7-BC00-B6356627C74B",'sign':"3ec7cce0b2274e4f3311aa00ccaf0ecf"},
            {'account_name':"mingg2",'device_id':"1965FBA4-13AA-49C7-BC00-B6356627C74B",'sign':"249774b15b42c9127ab221c513941bd2"},
            {'account_name':"mingg3",'device_id':"1965FBA4-13AA-49C7-BC00-B6356627C74B",'sign':"9a9c6d01f0dee2461e44e4df6747e2ef"},
            {'account_name':"mingg4",'device_id':"1965FBA4-13AA-49C7-BC00-B6356627C74B",'sign':"bb308171c573e531e1b91820fe05ce1e"},
            {'account_name':"mingg5",'device_id':"1965FBA4-13AA-49C7-BC00-B6356627C74B",'sign':"d00fc7211f308d7b1e2b391c30543614"},
            {'account_name':"mingg6",'device_id':"1965FBA4-13AA-49C7-BC00-B6356627C74B",'sign':"625d291b8055cc07d9ce3d27de505f0a"},
            {'account_name':"mingg7",'device_id':"1965FBA4-13AA-49C7-BC00-B6356627C74B",'sign':"8f2e144d2962539a2ab1491596c0a22c"},
            {'account_name':"mingg8",'device_id':"1965FBA4-13AA-49C7-BC00-B6356627C74B",'sign':"f05ec7d998c181a61449c0f5f674385e"},
            {'account_name':"mingg10",'device_id':"1965FBA4-13AA-49C7-BC00-B6356627C74B",'sign':"ace4ec28c6177f4a83d67732bb217b57"},
            {'account_name':"mingg10",'device_id':"1965FBA4-13AA-49C7-BC00-B6356627C74B",'sign':"ace4ec28c6177f4a83d67732bb217b57"},
            {'account_name':"mingg11",'device_id':"1965FBA4-13AA-49C7-BC00-B6356627C74B",'sign':"292521ba0241313dadaa79ee24d1330f"},
            {'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'sign': 'a90e37e2f20e8d73db87c82ed313906d', 'account_name': 'mingg12'},
            {'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'sign': 'b2fd9a56fdf63e1c16eb51bbf6f26051', 'account_name': 'mingg13'},
            {'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'sign': '6e73f76ccc2ef603eefc84ffd1e4011c', 'account_name': 'mingg14'},
            {'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'sign': '7685003585c1b6706af0f2ada6f06edf', 'account_name': 'mingg15'},
            {'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'sign': '905b559602d9feadb103268c095b6e38', 'account_name': 'mingg16'},
            {'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'sign': '9821016cb59b273a8f33a0d56aab9995', 'account_name': 'mingg17'},
            {'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'sign': 'c8b308a1cdaac4f30b1922987ff9598a', 'account_name': 'mingg18'},
            {'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'sign': '5bdc4cb134da212511348c24fbc03d5c', 'account_name': 'mingg19'},
            {'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'sign': '7ba8703ecf2fe7b2ab3b5503652743e6', 'account_name': 'mingg20'},
            {'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'sign': '4462c60e2cda6b89d06cffe9ad39c9e8', 'account_name': 'mingg21'},
            {'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'sign': 'd08f94853189928fe9ed71871362417f', 'account_name': 'mingg22'},
            {'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'sign': '585d7e326abf93cf2f2ea8065409b914', 'account_name': 'mingg23'},
            {'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'sign': '1b00ab88fcf4ba9fb1bce4f9f3b9ebc7', 'account_name': 'mingg24'},

]

            
            
#选择使用哪个账号
account_num = 0
#选择进第几个服务器
server_num = 10#注意！！！变更服务器还需要修改websocketIP
#
level_oldaccount = 65
level_limit = 48
#以下参数不需要修改
#读取账号登录需要的信息
account_name = ''
device_id = ''
sign = ''
report_sign = ''
tili = 0
isBoss = 0
level = 0
email_list = []
item_number = [0,0]
equipId = 0
islogin = 0
def on_message(ws, message):
    global email_list,isBoss,tili,level,item_number,equipId,islogin
    #print(message)
    '''
    if message == "Illegal Request":
        return None
    '''
    message_json = json.loads(message)
    MsgID = message_json['Header']['MsgID']
    if MsgID == 16308:
        #print("收到一条系统通知:"+message_json['Msg']['RetData']['Content'])
        return None
    elif MsgID == 16304:
        #print("收到一条玩家发言:"+message_json['Msg']['RetData']['ChatMsg'])
        return None
    elif MsgID == 16058:#收到任务状态
        TiliCD = message_json['Msg']['RetData']['CDInfo']['TiliCD']
        Gold = message_json['Msg']['RetData']['Wealth']['Gold']
        Diamond = message_json['Msg']['RetData']['Wealth']['Diamond']
        Food = message_json['Msg']['RetData']['Wealth']['Food']
        Tili = message_json['Msg']['RetData']['Wealth']['Tili']       
        #print("收到人物状态1:")
        print("体力CD:%s,金币:%s,钻石:%s,猫粮:%s,体力:%s"%(TiliCD,Gold,Diamond,Food,Tili))
        tili = Tili
        return None
    elif MsgID == 16106:#收到任务状态
        return None
    elif MsgID == 17104:#成功领取鱼干
        #{"Header":{"MsgID":17104,"ProtoVersion":1454470775},"Msg":{"RetData":{"Tili":[{"Index":1,"StartHour":12,"EndHour":14,"Num":60,"AddedCost":60,"State":1},{"Index":2,"StartHour":17,"EndHour":19,"Num":60,"AddedCost":60,"State":0},{"Index":3,"StartHour":21,"EndHour":23,"Num":60,"AddedCost":60,"State":0}],"Wealth":{"Gold":983400,"Diamond":2209,"Food":594926,"Tili":180,"BarCard":1,"Soul":0,"EquipSoul":0,"Arena":0,"Bgz":0,"Legion":2080,"Horn":0,"BarMoney":3,"DollsMoney":4},"DataChange":{"Hero":{"New":[],"Update":[],"Del":[]},"BagItem":{"New":[],"Update":[],"Del":[]},"BagEquip":{"New":[],"Update":[],"Del":[]},"HeroFrag":{"New":[],"Update":[],"Del":[]},"EquipFrag":{"New":[],"Update":[],"Del":[]}}}}}
        print('成功领取鱼干')
    elif MsgID == 16306:#收到频道聊天信息汇总
        #标志着正式登陆成功
        #print('收到聊天信息')
        islogin = 1
        start_game(ws)
        return None
    elif MsgID == 15508:#成功加入公会
        print('成功加入公会')
        return None

    elif MsgID == 16246:#Boss列表
        #print(message)
        boss_list = message_json['Msg']['RetData']['BossInfo']['BossList']
        for i in range(len(boss_list)):
            BossRoleId = boss_list[i]['BossRoleId'] 
            if BossRoleId == 9401559:
                print("-------收到Boss信息--=-大号")
                continue
            else:
                RoleName = boss_list[i]['RoleName'] 
                Level = boss_list[i]['Level'] 
                BossTid = boss_list[i]['BossTid'] 
                BossDegree = boss_list[i]['BossDegree'] 
                print("%s发现了%d级的Boss-%d,BossTid:%d,BossDegree:%d"%(RoleName,Level,BossRoleId,BossTid,BossDegree))
                isBoss = 1
        return None
    elif MsgID == 16248:#Boss列表    
        BossRoleId = message_json['Msg']['RetData']['BossInfo']['BossRoleId'] 
        if BossRoleId != 9401559:
            isBoss = 1
            print(str(isBoss))
            print("-------收到Boss信息-------")
        else:
            print("-------收到Boss信息--=-大号")
        return None
    elif MsgID == 16902:#收到右键列表
        #print("收到邮件信息")
        email_list = message_json['Msg']['RetData']['MailList']
        return None
    elif MsgID == 16246:
        print("玩家"+message_json['Msg']['RetData']['BossInfo']['BossList']['RoleName']+"发现了一个"+message_json['Msg']['RetData']['BossInfo']['BossList']['Level']+"级的BOSS")
    elif MsgID == 14006:
        Tili = message_json['Msg']['RetData']['Wealth']['Tili']
        level = message_json['Msg']['RetData']['BaseInfo']['Level'] 
        print("成功完成扫荡,体力剩余:%d,当前等级为:%d"%(Tili,level))
        tili = Tili
        return None
    elif MsgID == 18602:#收到商店货物信息
        item_number[0] = message_json['Msg']['RetData']['AllShopInfo']['AllShopList'][0]['ItemList'][1]['ShopIndex']
        item_number[1] = message_json['Msg']['RetData']['AllShopInfo']['AllShopList'][0]['ItemList'][3]['ShopIndex']
        return None
    elif MsgID == 18752:#收到抓娃娃投币结果
        DollsMoney = message_json['Msg']['RetData']['Wealth']['DollsMoney']    
        print("投币成功，收到抓娃娃投币结果")
        print("还剩下抓娃娃币%s枚"%(DollsMoney))
        return None
    elif MsgID == 18754:#收到抓娃娃投币结果
        Result = message_json['Msg']['RetData']['Result']   
        if Result:
            print("抓取成功")
        else:
            print("抓取失败")
        return None
    elif MsgID == 10002:#个人相关信息
        equipId = message_json['Msg']['RetData']['BagEquipList'][0]['EquipId']
        level = message_json['Msg']['RetData']['BaseInfo']['Level']
        ws.send('{"Header":{"MsgID":10003},"Msg":{}}')
        return None
        #ws.send('{"Header":{"MsgID":16901},"Msg":{}}')
        #正式进入游戏
    elif MsgID == 20000:   
        if message_json['Msg']['ReqMsgId'] == 16225 or message_json['Msg']['ReqMsgId'] == 16229:
            return None
        elif message_json['Msg']['ReqMsgId'] == 14005 and message_json['Msg']['RetCode'] == 1061:
            print("体力耗尽")
            return None
    #print(message)
    

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    ws.send(lxhWebsocketApi.api_login(account_name,device_id,sign,server_num))
    return None

def run(*args):
    global ws
    #读取账号登录需要的信息
    websocket.enableTrace(False)
    #ws = websocket.WebSocketApp("ws://47.93.126.149:8002",
    ws = websocket.WebSocketApp("ws://47.93.150.36:8002",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()            
       
    print('websocket open')
    
    
def start_game(ws):
    do_something(ws)
    
def do_dailyTask(isgetExp):
    global ws
    ws.send(lxh_growup_api.api_dailyTask3())
 
    do_something(ws)
    ws.send(lxh_growup_api.api_newAccountTask4(20))
    ws.send(lxh_growup_api.api_newAccountTask4(25))
    ws.send(lxh_growup_api.api_newAccountTask4(30))
    ws.send(lxh_growup_api.api_newAccountTask4(32))  
    ws.send(lxh_growup_api.api_newAccountTask4(34))
    ws.send(lxh_growup_api.api_newAccountTask4(36))
    ws.send(lxh_growup_api.api_newAccountTask4(38))
    ws.send(lxh_growup_api.api_newAccountTask2(20))
    ws.send(lxh_growup_api.api_newAccountTask2(25))
    ws.send(lxh_growup_api.api_newAccountTask2(30))
    ws.send(lxh_growup_api.api_newAccountTask2(35))
    ws.send(lxh_growup_api.api_newAccountTask2(40))
    ws.send(lxh_growup_api.api_newAccountTask2(45))
    ws.send(lxh_growup_api.api_newAccountTask7(20))
    ws.send(lxh_growup_api.api_newAccountTask7(50))
    if isgetExp:
        ws.send(lxh_growup_api.api_get_dailytask_reward(1))
        ws.send(lxh_growup_api.api_get_dailytask_reward(2))
        ws.send(lxh_growup_api.api_get_dailytask_reward(4))
        ws.send(lxh_growup_api.api_get_dailytask_reward(6))
        ws.send(lxh_growup_api.api_get_dailytask_reward(12)) 


def do_dailyTask_once(isgetExp):
    global ws,item_number,equipId
    #每日签到
    ws.send(lxh_growup_api.api_newAccountTask5())  
    ws.send(lxh_growup_api.api_dailyTask12())
    ws.send(lxh_growup_api.api_dailyTask14())
def do_something(ws):
    global email_list
    print("Do_Something")
    #心跳包
    ws.send(lxh_growup_api.api_sendHeartPackage1())
    #收取体力
    ws.send(lxh_growup_api.api_getVitality())
    #赠送体力
    ws.send(lxh_growup_api.api_giveVitality())
    #领取鱼干
    ws.send(lxh_growup_api.api_get_fish())  
    #收取所有邮件奖励
    lxh_growup_api.api_get_all_email_reward(ws,email_list)
    #登录有礼-领取榨菜丹
    for i in range(1,20):
        #ws.send(lxh_growup_api.api_newAccountTask3(i+1))
        print("领取等级奖励-榨菜丹")
        ws.send(lxh_growup_api.api_get_level_reward(i+1))
    
    
def login(account_num):
    global account_name,device_id,sign,report_sign,ws,level
    print('登录第'+str(account_num)+'个账号') 
    account_name = account[account_num-1]['account_name']
    device_id = account[account_num-1]['device_id']
    sign = account[account_num-1]['sign']
    report_sign = account[account_num-1]['sign']
    _thread.start_new_thread(run, ())

def logout():
    global ws,islogin
    ws.close()
    islogin = 0

def logout_in_oldaccount():
    global account_name,device_id,sign,level
    print('登录大号') 
    account_name = "qq342875289"
    device_id = "1965FBA4-13AA-49C7-BC00-B6356627C74B"
    sign = "cd8929990165f5644f1c66c969efd300"
    _thread.start_new_thread(run, ()) 

def checklogin():
    global islogin
    while (islogin==0):
        time.sleep(1)
        None
    time.sleep(1)
    
            
def dailyTask():
    global ws,level,level_limit
    if(level>level_limit):
        do_dailyTask(False)
        print('账号超出等级限制,不领取每日任务经验奖励')
    else:
        do_dailyTask(True)
        print('账号完成每日任务')
    time.sleep(1)
    
def dailyTask_once():
    global ws,item_number,equipId
    if(level>level_limit):
        do_dailyTask_once(False)
        print('账号超出等级限制,不领取一次性每日任务经验奖励')
    else:
        do_dailyTask_once(True)
        print('账号完成一次性每日任务')
    time.sleep(1)
 
def AutoKill():
    global tili,ws,isBoss,level_oldaccount,level,count_finish,count_isBoss,count_noTili
    #领取鱼干
    ws.send(lxh_growup_api.api_get_fish()) 
    while 1 :
        if (level >= (level_oldaccount - 20)) and (isBoss == 1) :
            print("发现Boss,退出扫荡")
            break
        elif tili < 5:
            print("发体力耗尽,退出扫荡")
            break
        for i in range(5):
            ws.send(lxh_growup_api.api_kill(1, 1, 1))
        time.sleep(1)
               

if __name__ == "__main__":
    #global ws,isBoss,equipId,item_number,count_finish,count_isBoss,count_noTili

    for i in range(1,len(account)+1):#len(account)+1
        equipId = 0
        item_number[0] = 0
        isBoss = 0
        login(i)
        time.sleep(1)
        checklogin()
        time.sleep(1)
        #
        dailyTask()
        time.sleep(1)
        dailyTask_once()
        time.sleep(1)
        AutoKill()
        #
        logout()
        time.sleep(1)
        '''
        
        
        AutoKill()
        time.sleep(1)
        
        '''
        
