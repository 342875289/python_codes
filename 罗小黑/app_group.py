from tkinter import * 
import websocket
import _thread
import time
import json

#15到17

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
            {'sign': 'e9d7ef63556b60acfa7e2b1d1fc80ab9', 'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'account_name': 'mingg25'},
            {'sign': '73552ea9ad0fdcc0737539ccf6816ed2', 'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'account_name': 'mingg26'},
            {'sign': '161f35c041e8714ff161b87c18334b53', 'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'account_name': 'mingg27'},
            {'sign': '1eb9767ba23d991b8afd13ddb568b80a', 'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'account_name': 'mingg28'},
            {'sign': '2f62689050f0bbaf511222c8dd9280c0', 'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'account_name': 'mingg29'},
            {'sign': 'a22eb35a14910babf83c2eaa84198e4c', 'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'account_name': 'mingg30'},
            {'sign': '04416791b724bd886b7cc6177aed8b4f', 'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'account_name': 'mingg31'},
            {'sign': '28c8ecdcb4db5e3552ae6a6b9e9f21d0', 'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'account_name': 'mingg32'},
            {'sign': '8cd2f086a1cfe6b0d4c29180c529d683', 'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'account_name': 'mingg33'},
            {'sign': '6e3e260ce7e11135d752a76b803897ed', 'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'account_name': 'mingg34'},
            {'sign': '1740d542fdf18587529e743e87e71375', 'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'account_name': 'mingg35'},
            {'sign': '7937201f2f706baf891464cf82ee0cdb', 'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'account_name': 'mingg36'},
            {'sign': '78b9a696d70f2033d4e5b5414407f254', 'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'account_name': 'mingg37'},
            {'sign': '013cda36dfdf793375a7229413a0b07d', 'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'account_name': 'mingg38'},
            {'sign': '2adb5fde1f09b9ace6001ffb0af92279', 'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'account_name': 'mingg39'},
            {'sign': '1e17cede7daf83079d91b813a264069a', 'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'account_name': 'mingg40'},
            {'sign': '71d88905436d1585bb4d1d69803c775b', 'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'account_name': 'mingg41'},
            {'sign': 'ca8056f9ae96384b4f40e62ec89522e5', 'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'account_name': 'mingg42'},
            {'sign': 'a22736c89fc6ef316f217ff9f324cfa4', 'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'account_name': 'mingg43'},
            {'sign': 'edc56f6459aec3d1dbfa16e1ffce8650', 'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'account_name': 'mingg44'},
            {'sign': '228a94be2a1cf9b5033493c8580a484f', 'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'account_name': 'mingg45'},
            {'sign': '36bfab56db3814c4e79c4721f8639ae0', 'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'account_name': 'mingg46'},
            {'sign': 'f3926d73010df8db99aca1be0a6cd8eb', 'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'account_name': 'mingg47'},
            {'sign': '4a64ac607f9601f7293249a7f921cab6', 'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'account_name': 'mingg48'},
            {'sign': '26d5d2c32285c69d37ccaa2213ac51c7', 'device_id': '1965FBA4-13AA-49C7-BC00-B6356627C74B', 'account_name': 'mingg49'},
]




#选择使用哪个账号
account_num = 0
#选择进第几个服务器
server_num = 10#注意！！！变更服务器还需要修改websocketIP
#
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
        label_tili.config(text='体力:'+str(Tili))
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
                label_boss.config(text='有Boss',fg='red')
                isBoss = 1
        return None
    elif MsgID == 16248:#Boss列表    
        BossRoleId = message_json['Msg']['RetData']['BossInfo']['BossRoleId'] 
        if BossRoleId != 9401559:
            label_boss.config(text='有Boss',fg='red')
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
        #print("成功完成扫荡,体力剩余:%d,当前等级为:%d"%(Tili,level))
        label_tili.config(text='体力:'+str(Tili))
        label_accountName.config(text=account_name+'等级:'+str(level))
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
        label_accountName.config(text=account_name+'等级:'+str(level))
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

def step_one():
    global account_num,ws
    print("开始执行-第1步")
    #创建新角色
    ws.send(lxh_growup_api.api_creatname("明明明公会"+var_accountNumber.get()))
    #黑粉催更
    ws.send(lxh_growup_api.api_getitem())
    #修改阵容-加入千针
    ws.send(lxh_growup_api.api_changelocation([0,1041,0,0,1043,0,0,0,0,0,0,0])) 
    print("执行完成,请手动出战第一章1,2,3")
    
def step_two():
    global email_list,ws
    
    print("开始执行-第2步")
    #领取星星奖励
    ws.send(lxh_growup_api.api_get_stars_reward(1, 2))
    #寻宝
    ws.send(lxh_growup_api.api_get_explor_reward(1))
    #穿装备
    ws.send(lxh_growup_api.api_weapons_up())
    #强化千针装备
    ws.send(lxh_growup_api.api_weapons_strengthen(1043))
    #升级千针技能
    ws.send(lxh_growup_api.api_pets_skills_strengthen(1043,1,2))
    #进阶东北虎
    ws.send(lxh_growup_api.api_pets_quality_strengthen(1041))
    #合成保险男
    ws.send(lxh_growup_api.api_get_pets_byCompose(1091))
    #增加保险男经验
    ws.send(lxh_growup_api.api_pets_exp_up(1091, 2020301, 1))
    
    #收取所有邮件奖励
    lxh_growup_api.api_get_all_email_reward(ws,email_list)
    
    #修改阵容-加入保险男和皇受
    ws.send(lxh_growup_api.api_changelocation([0,1041,0,1091,1043,0,0,1025,0,0,0,0])) 
    
    ws.send(lxh_growup_api.api_kill(1, 1, 1))
    ws.send(lxh_growup_api.api_kill(1, 1, 1))
    ws.send(lxh_growup_api.api_kill(1, 1, 1))
    ws.send(lxh_growup_api.api_kill(1, 1, 1))
    ws.send(lxh_growup_api.api_kill(1, 1, 1))
    
    
    #增加法宝经验
    ws.send(lxh_growup_api.api_treasure_exp_up(2022101, 1))
    #领取每日任务奖励1
    ws.send(lxh_growup_api.api_get_dailytask_reward(1))
    ws.send(lxh_growup_api.api_newAccountTask9()) 
    ws.send(lxh_growup_api.api_newAccountTask3(1))
    
    for i in range(120):
        ws.send(lxh_growup_api.api_kill(1, 1, 1))
    #添加大号为好友
    #ws.send(lxh_growup_api.api_addfriend(9401559))
    #加入公会
    #ws.send(lxh_growup_api.api_addLegion(50197))
    #投资会馆
    ws.send(lxh_growup_api.api_newAccountTask6(1,2))
    ws.send(lxh_growup_api.api_newAccountTask6(1,2))
    ws.send(lxh_growup_api.api_newAccountTask6(1,2))
    time.sleep(1)
    #新账号任务系列
    ws.send(lxh_growup_api.api_newAccountTask11())
    ws.send(lxh_growup_api.api_newAccountTask12())
    ws.send(lxh_growup_api.api_newAccountTask2(10))
    ws.send(lxh_growup_api.api_newAccountTask2(15))
    ws.send(lxh_growup_api.api_newAccountTask4(10))
    ws.send(lxh_growup_api.api_newAccountTask5())
    ws.send(lxh_growup_api.api_newAccountTask7(20))
    ws.send(lxh_growup_api.api_newAccountTask8(20))
    ws.send(lxh_growup_api.api_newAccountTask8(50))
    ws.send(lxh_growup_api.api_newAccountTask8(100))
    ws.send(lxh_growup_api.api_newAccountTask8(150))
    ws.send(lxh_growup_api.api_newAccountTask8(200))
    ws.send(lxh_growup_api.api_newAccountTask8(300))
    ws.send(lxh_growup_api.api_newAccountTask8(400))
    ws.send(lxh_growup_api.api_newAccountTask8(700))
    ws.send(lxh_growup_api.api_newAccountTask8(1000))

def do_dailyTask():
    global ws
    #投资会馆
    ws.send(lxh_growup_api.api_newAccountTask6(1,2))
    ws.send(lxh_growup_api.api_newAccountTask6(1,2))
    ws.send(lxh_growup_api.api_newAccountTask6(1,2))
    '''
    ws.send(lxh_growup_api.api_get_dailytask_reward(1))
    ws.send(lxh_growup_api.api_newAccountTask9())
    ws.send(lxh_growup_api.api_get_dailytask_reward(2))
    ws.send(lxh_growup_api.api_dailyTask1())
    ws.send(lxh_growup_api.api_get_dailytask_reward(8))
    ws.send(lxh_growup_api.api_dailyTask2())
    ws.send(lxh_growup_api.api_get_dailytask_reward(4))
    ws.send(lxh_growup_api.api_dailyTask3())
    ws.send(lxh_growup_api.api_get_dailytask_reward(6))
    ws.send(lxh_growup_api.api_dailyTask4())
    ws.send(lxh_growup_api.api_get_dailytask_reward(7))
    ws.send(lxh_growup_api.api_dailyTask6())
    ws.send(lxh_growup_api.api_dailyTask5())
    ws.send(lxh_growup_api.api_newAccountTask7(20))
    ws.send(lxh_growup_api.api_newAccountTask7(50))
    ws.send(lxh_growup_api.api_touchFriend(9401559,4))
    ws.send(lxh_growup_api.api_touchFriend(9401559,1))  
    ws.send(lxh_growup_api.api_get_dailytask_reward(12))     
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
    '''
    
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
    
    '''
    #登录有礼
    for i in range(10,14):
        ws.send(lxh_growup_api.api_newAccountTask3(i+1))
        ws.send(lxh_growup_api.api_get_level_reward(i+1))
    '''
    
def login():
    global account_name,device_id,sign,report_sign,ws,level
    print('登录第'+var_accountNumber.get()+'个账号') 
    
    account_num = int(var_accountNumber.get())
    account_name = account[account_num-1]['account_name']
    device_id = account[account_num-1]['device_id']
    sign = account[account_num-1]['sign']
    report_sign = account[account_num-1]['sign']
    label_accountName.config(text=account_name+'等级:'+str(level))
    _thread.start_new_thread(run, ())
def bugTili():
    global ws
    #领取鱼干
    ws.send(lxh_growup_api.api_get_fish())  
    ws.send(lxh_growup_api.api_newAccountTask9())  
    
def logout():
    global ws,islogin
    ws.close()
    islogin = 0
    label_accountName.config(text='请选择要登录的账号' )
    label_boss.config(text='暂无Boss',fg='black')

def logout_in(val):
    global account
    account_num = int(var_accountNumber.get() ) + val
    if (account_num != 0) and ( account_num <= len(account) ):
        logout()
        var_accountNumber.set(account_num)
        login()

def logout_in_oldaccount():
    global account_name,device_id,sign,level
    print('登录大号') 
    account_name = "qq342875289"
    device_id = "1965FBA4-13AA-49C7-BC00-B6356627C74B"
    sign = "cd8929990165f5644f1c66c969efd300"
    label_accountName.config(text=account_name+'等级:'+str(level))
    _thread.start_new_thread(run, ()) 

           
def get_pets_by_zhuawawa():
    global ws
    ws.send(lxh_growup_api.api_get_pets_by_zhuawawa_1())
    ws.send(lxh_growup_api.api_get_pets_by_zhuawawa_2(2006))  
               
def kill():
    global ws
    killcount = var_killcount.get()
    print('扫荡'+killcount+'次') 
    for i in range(int(killcount)):
        ws.send(lxh_growup_api.api_kill(1, 1, 1))
    #label_boss.config(text='有Boss',fg='red')
def checklogin():
    global islogin
    while (islogin==0):
        time.sleep(1)
        None
    time.sleep(1)
    
            
def AutoKill():
    def test():
        global tili,ws,isBoss,islogin,level_oldaccount,level
        count_finish = 0
        count_isBoss = 0
        count_noTili = 0
        autoFromNumber = int(var_autoFromNumber.get() ) 
        autoToNumber = int(var_autoToNumber.get() )
        for i in range(autoFromNumber,autoToNumber):
            var_accountNumber.set(i)
            isBoss = 0
            login()
            checklogin()
            while 1 :
                if (level > (level_oldaccount - 20)) and (isBoss == 1) :
                    print("发现Boss,退出扫荡")
                    count_isBoss = count_isBoss + 1
                    break
                elif tili < 5:
                    print("发体力耗尽,退出扫荡")
                    count_noTili = count_noTili + 1
                    break
                for i in range(5):
                    ws.send(lxh_growup_api.api_kill(1, 1, 1))
                time.sleep(1)
            logout()
            count_finish = count_finish + 1
            label_autoKill.config(text='已完成:'+str(count_finish)+',有Boss:'+str(count_isBoss)+',体力耗尽:'+str(count_noTili))
            time.sleep(1)
    _thread.start_new_thread(test, ())
    
def dailyTask():
    def test():
        global ws,level,level_limit
        autoFromNumber = int(var_autoFromNumber.get() ) 
        autoToNumber = int(var_autoToNumber.get() )
        for i in range(autoFromNumber,autoToNumber):
            var_accountNumber.set(i)
            login()
            checklogin()
            if(level>level_limit):
                print("账号:"+str(int(var_accountNumber.get())-1)+'超出等级限制,不进行每日任务')
            else:
                do_dailyTask()
                print("账号:"+str(int(var_accountNumber.get())-1)+'完成每日任务')
            time.sleep(2)
            logout()
    _thread.start_new_thread(test, ())
    
 
#只能做一次的每日任务
def dailyTask_once():
    def test():
        global ws,item_number,equipId
        autoFromNumber = int(var_autoFromNumber.get() ) 
        autoToNumber = int(var_autoToNumber.get() )
        for i in range(autoFromNumber,autoToNumber):
            var_accountNumber.set(i)
            equipId = 0
            item_number[0] = 0
            login()
            checklogin()
            if(level>level_limit):
                print("账号:"+str(int(var_accountNumber.get())-1)+'超出等级限制,不进行一次性每日任务')
            else:
                ws.send(lxh_growup_api.api_newAccountTask5())  
                ws.send(lxh_growup_api.api_dailyTask12())
                ws.send(lxh_growup_api.api_dailyTask14())
                #买体力
                ws.send(lxh_growup_api.api_newAccountTask9())  
                ws.send(lxh_growup_api.api_newAccountTask9()) 
                ws.send(lxh_growup_api.api_newAccountTask9()) 
                #投资会馆等级
                ws.send(lxh_growup_api.api_newAccountTask6(2))
                ws.send(lxh_growup_api.api_newAccountTask6(2))
                ws.send(lxh_growup_api.api_newAccountTask6(2))
                ws.send(lxh_growup_api.api_get_dailytask_reward(20)) 
                #购买商店物品两次
                ws.send(lxh_growup_api.api_get_shop_items())
                time.sleep(5)
                if item_number[0]!=0 :
                    ws.send(lxh_growup_api.api_buy_shop_items(item_number[0]))
                    ws.send(lxh_growup_api.api_buy_shop_items(item_number[1]))
                    ws.send(lxh_growup_api.api_get_dailytask_reward(5))
                #装备
                if equipId != 0:
                    #装备强化
                    ws.send(lxh_growup_api.api_dailyTask9(equipId))
                    ws.send(lxh_growup_api.api_get_dailytask_reward(9))
                    #装备熔炼
                    ws.send(lxh_growup_api.api_dailyTask8(equipId))
                    ws.send(lxh_growup_api.api_get_dailytask_reward(10))
                #喂榨菜丹
                ws.send(lxh_growup_api.api_dailyTask7())
                ws.send(lxh_growup_api.api_dailyTask7())
                ws.send(lxh_growup_api.api_dailyTask7())
                ws.send(lxh_growup_api.api_get_dailytask_reward(13))
                print("账号:"+str(int(var_accountNumber.get())-1)+'完成一次性每日任务')
            time.sleep(5)
            logout()
    _thread.start_new_thread(test, ())
 
def onekey():
    count_finish = 0
    count_isBoss = 0
    count_noTili = 0
    def AutoKill():
        global tili,ws,isBoss,level_oldaccount,level,count_finish,count_isBoss,count_noTili
        while 1 :
            if (level > (level_oldaccount - 20)) and (isBoss == 1) :
                print("发现Boss,退出扫荡")
                count_isBoss = count_isBoss + 1
                break
            elif tili < 5:
                print("发体力耗尽,退出扫荡")
                count_noTili = count_noTili + 1
                break
            for i in range(5):
                ws.send(lxh_growup_api.api_kill(1, 1, 1))
            time.sleep(1)
        count_finish = count_finish + 1
        label_autoKill.config(text='已完成:'+str(count_finish)+',有Boss:'+str(count_isBoss)+',体力耗尽:'+str(count_noTili))
     
    def dailyTask():
        global ws,level,level_limit
        if(level>level_limit):
            print("账号:"+str(int(var_accountNumber.get())-1)+'超出等级限制,不进行每日任务')
        else:
            do_dailyTask()
            print("账号:"+str(int(var_accountNumber.get())-1)+'完成每日任务')
        time.sleep(1)
    def dailyTask_once():
        global ws,item_number,equipId
        if(level>level_limit):
            print("账号:"+str(int(var_accountNumber.get())-1)+'超出等级限制,不进行一次性每日任务')
        else:
            ws.send(lxh_growup_api.api_newAccountTask5())  
            ws.send(lxh_growup_api.api_dailyTask12())
            ws.send(lxh_growup_api.api_dailyTask14())
            #买体力
            ws.send(lxh_growup_api.api_newAccountTask9())  
            ws.send(lxh_growup_api.api_newAccountTask9()) 
            ws.send(lxh_growup_api.api_newAccountTask9()) 
            #投资会馆等级
            ws.send(lxh_growup_api.api_newAccountTask6(2))
            ws.send(lxh_growup_api.api_newAccountTask6(2))
            ws.send(lxh_growup_api.api_newAccountTask6(2))
            ws.send(lxh_growup_api.api_get_dailytask_reward(20)) 
            #购买商店物品两次
            ws.send(lxh_growup_api.api_get_shop_items())
            time.sleep(2)
            if item_number[0]!=0 :
                ws.send(lxh_growup_api.api_buy_shop_items(item_number[0]))
                ws.send(lxh_growup_api.api_buy_shop_items(item_number[1]))
                ws.send(lxh_growup_api.api_get_dailytask_reward(5))
            #装备
            if equipId != 0:
                #装备强化
                ws.send(lxh_growup_api.api_dailyTask9(equipId))
                ws.send(lxh_growup_api.api_get_dailytask_reward(9))
                #装备熔炼
                ws.send(lxh_growup_api.api_dailyTask8(equipId))
                ws.send(lxh_growup_api.api_get_dailytask_reward(10))
            #喂榨菜丹
            ws.send(lxh_growup_api.api_dailyTask7())
            ws.send(lxh_growup_api.api_dailyTask7())
            ws.send(lxh_growup_api.api_dailyTask7())
            ws.send(lxh_growup_api.api_get_dailytask_reward(13))
            print("账号:"+str(int(var_accountNumber.get())-1)+'完成一次性每日任务')
        time.sleep(1)
            
    def test():
        global ws,isBoss,equipId,item_number,count_finish,count_isBoss,count_noTili
        count_finish = 0
        count_isBoss = 0
        count_noTili = 0
        equipId = 0
        item_number[0] = 0
        autoFromNumber = int(var_autoFromNumber.get() ) 
        autoToNumber = int(var_autoToNumber.get() )
        for i in range(autoFromNumber,autoToNumber):
            isBoss = 0
            var_accountNumber.set(i)
            login()
            checklogin()
            dailyTask_once()
            AutoKill()
            dailyTask()
            logout()
        print("第一轮已完成")
        for times in range(2):
            time.sleep(5*60)
            for i in range(autoFromNumber,autoToNumber):
                var_accountNumber.set(i)
                login()
                checklogin()
                dailyTask()
                logout()
            print("第"+str(times+2)+"轮已完成")
    _thread.start_new_thread(test, ())    

def oldaccount_dailytask():
    global ws
    ws.send(lxh_growup_api.api_get_dailytask_reward(1))
    ws.send(lxh_growup_api.api_dailyTask2())
    ws.send(lxh_growup_api.api_get_dailytask_reward(4))
    ws.send(lxh_growup_api.api_dailyTask3())
    ws.send(lxh_growup_api.api_get_dailytask_reward(6))
    ws.send(lxh_growup_api.api_dailyTask20())
    ws.send(lxh_growup_api.api_dailyTask10())
    ws.send(lxh_growup_api.api_dailyTask11())
    ws.send(lxh_growup_api.api_touchFriend(9494242,1)) 
    ws.send(lxh_growup_api.api_get_dailytask_reward(12)) 
    ws.send(lxh_growup_api.api_newAccountTask5())
    ws.send(lxh_growup_api.api_newAccountTask6(1))
    ws.send(lxh_growup_api.api_newAccountTask6(1))
    ws.send(lxh_growup_api.api_newAccountTask6(1))
    ws.send(lxh_growup_api.api_get_dailytask_reward(20)) 
    for i in range(7,0,-1):
        ws.send(lxh_growup_api.api_dailyTask15(i))
    ws.send(lxh_growup_api.api_dailyTask19(1015,1))
    ws.send(lxh_growup_api.api_dailyTask19(1042,2))
    ws.send(lxh_growup_api.api_dailyTask19(1062,3))
    ws.send(lxh_growup_api.api_dailyTask19(1032,4))
    ws.send(lxh_growup_api.api_dailyTask19(1201,5))
    ws.send(lxh_growup_api.api_dailyTask19(1024,6))
    ws.send(lxh_growup_api.api_dailyTask19(1034,7))
    #收取所有邮件奖励
    lxh_growup_api.api_get_all_email_reward(ws,email_list)

    print("大号完成每日任务")
    
def oldaccount_dailytask_once():
    global ws,item_number
    item_number[0] = 0
    ws.send(lxh_growup_api.api_dailyTask1())
    ws.send(lxh_growup_api.api_get_dailytask_reward(8))
    ws.send(lxh_growup_api.api_dailyTask4())
    ws.send(lxh_growup_api.api_get_dailytask_reward(7))
    ws.send(lxh_growup_api.api_dailyTask12())
    ws.send(lxh_growup_api.api_dailyTask14())
    for i in range(3):
        ws.send(lxh_growup_api.api_dailyTask13(1,3))
        ws.send(lxh_growup_api.api_dailyTask13(2,3))
        ws.send(lxh_growup_api.api_dailyTask13(3,3))
        ws.send(lxh_growup_api.api_dailyTask13(4,3))
        ws.send(lxh_growup_api.api_dailyTask13(5,2))
    for i in range(5):
        ws.send(lxh_growup_api.api_dailyTask16())
        ws.send(lxh_growup_api.api_dailyTask17())
        ws.send(lxh_growup_api.api_dailyTask18())
    #后山探险
        ws.send(lxh_growup_api.api_dailyTask21())
        ws.send(lxh_growup_api.api_dailyTask22())
    for i in [3,10,13,20,23,30,33,40,43]:
        ws.send(lxh_growup_api.api_dailyTask23(3,i))
        ws.send(lxh_growup_api.api_dailyTask24())
    ws.send(lxh_growup_api.api_get_dailytask_reward(16)) 
    #购买商店物品两次
    ws.send(lxh_growup_api.api_get_shop_items())
    while (item_number[0] == 0):
        None
    ws.send(lxh_growup_api.api_buy_shop_items(item_number[0]))
    ws.send(lxh_growup_api.api_buy_shop_items(item_number[1]))
    ws.send(lxh_growup_api.api_get_dailytask_reward(5))
    print("大号完成每日任务")
    
    
def strengthen_soul():
    global ws
    for i in range(20):#金-5020111,木-5020131,水-5020121,火-5020141,土-5020151
        ws.send(lxh_growup_api.api_strengthen_soul(5020111, 1)) 
        ws.send(lxh_growup_api.api_strengthen_soul(5020131, 1)) 
        ws.send(lxh_growup_api.api_strengthen_soul(5020121, 1)) 
        ws.send(lxh_growup_api.api_strengthen_soul(5020141, 1)) 
        ws.send(lxh_growup_api.api_strengthen_soul(5020151, 1))
    for i in range(20):#金-5020111,木-5020131,水-5020121,火-5020141,土-5020151
        ws.send(lxh_growup_api.api_strengthen_soul(5020111, 2)) 
        ws.send(lxh_growup_api.api_strengthen_soul(5020131, 2)) 
        ws.send(lxh_growup_api.api_strengthen_soul(5020121, 2)) 
        ws.send(lxh_growup_api.api_strengthen_soul(5020141, 2)) 
        ws.send(lxh_growup_api.api_strengthen_soul(5020151, 2))        
    print('灵质熔炼完成')   


def quitgroup():
    def test():
        global ws,level,level_limit
        autoFromNumber = int(var_autoFromNumber.get() ) 
        autoToNumber = int(var_autoToNumber.get() )
        for i in range(autoFromNumber,autoToNumber):
            var_accountNumber.set(i)
            login()
            checklogin()
            ws.send(lxh_growup_api.api_quitLegion()) 
            time.sleep(2)
            logout()
    _thread.start_new_thread(test, ())
    
    
if __name__ == "__main__":
    #窗体参数
    win = Tk()#定义一个窗体  
    win.title('lxh-app')#定义窗体标题  
    #win.geometry('400x200')#定义窗体的大小，是400X200像素  
    #控件参数
    label_accountName = Label(win)  
    label_accountName['text'] = '请选择要登录的账号'  
    label_accountName.pack(side=TOP) 
    #登录frame
    frm_login = Frame(win)
    frm_login.pack(side=TOP)
    var_accountNumber = StringVar()
    entry_accountNumber = Entry(frm_login,textvariable = var_accountNumber)   
    var_accountNumber.set(str(len(account)))
    entry_accountNumber.pack(side=LEFT) 
    btn_login = Button(frm_login, text='登录', command=login)  
    btn_login.pack(side=LEFT)
    btn_logout = Button(frm_login, text='注销', command=logout)  
    btn_logout.pack(side=LEFT)
    btn_login_last = Button(frm_login, text='上一个', command=lambda:logout_in(-1))  
    btn_login_last.pack(side=LEFT)
    btn_login_next = Button(frm_login, text='下一个', command=lambda:logout_in(+1))  
    btn_login_next.pack(side=LEFT)
    #扫荡frame
    frm_kill = Frame(win)
    frm_kill.pack(side=TOP)
    var_killcount = StringVar()
    killcount = Entry(frm_login,textvariable = var_killcount)   
    var_killcount.set("1")
    killcount.pack(side=LEFT) 
    btn_kill = Button(frm_login, text='投资', command=do_dailyTask)  
    btn_kill.pack(side=LEFT)
    btn_bugTili = Button(frm_login, text='购买体力', command=bugTili)  
    btn_bugTili.pack(side=LEFT)
    label_boss = Label(frm_login)  
    label_boss['text'] = '暂无Boss'  
    label_boss.pack(side=RIGHT) 
    label_tili = Label(frm_login)  
    label_tili['text'] = '体力:0'  
    label_tili.pack(side=RIGHT) 
    #自动范围选择frame
    frm_auto = Frame(win)
    frm_auto.pack(side=TOP)
    label_auto = Label(frm_auto)  
    label_auto['text'] = '选择自动范围' 
    label_auto.pack(side=LEFT) 
    
    var_autoFromNumber = StringVar()
    entry_autoFromNumber = Entry(frm_auto,textvariable = var_autoFromNumber)   
    var_autoFromNumber.set("1")
    entry_autoFromNumber.pack(side=LEFT) 
    
    label_auto_to = Label(frm_auto)  
    label_auto_to['text'] = 'To' 
    label_auto_to.pack(side=LEFT) 
    
    var_autoToNumber = StringVar()
    entry_autoToNumber = Entry(frm_auto,textvariable = var_autoToNumber)   
    var_autoToNumber.set("28")
    entry_autoToNumber.pack(side=LEFT)

    #自动扫荡frame
    frm_autoKill = Frame(win)
    frm_autoKill.pack(side=TOP)
    btn_dailyTask_once = Button(frm_autoKill, text='只能做一次的每日任务', command=dailyTask_once)  
    btn_dailyTask_once.pack(side=RIGHT)
    btn_dailyTask = Button(frm_autoKill, text='每日任务', command=dailyTask)  
    btn_dailyTask.pack(side=RIGHT)
    btn_autoKill = Button(frm_autoKill, text='自动退会', command=quitgroup)  
    btn_autoKill.pack(side=RIGHT)
    
    label_autoKill = Label(frm_autoKill)  
    label_autoKill['text'] = '已完成:0,有Boss:0,体力耗尽:0'  
    label_autoKill.pack(side=RIGHT)
    #大号frame
    frm_oldaccount = Frame(win)
    frm_oldaccount.pack(side=TOP)
    label_oldaccount = Label(frm_oldaccount)  
    label_oldaccount['text'] = '大号操作区:'  
    #练小号frame
    frm_newaccount = Frame(win)
    frm_newaccount.pack(side=TOP)
    label_newaccount = Label(frm_newaccount)  
    label_newaccount['text'] = '练小号步骤:'  
    label_newaccount.pack(side=LEFT) 
    btn_stepOne = Button(frm_newaccount, text='第一步', command=step_one)  
    btn_stepOne.pack(side=LEFT)
    btn_stepTwo = Button(frm_newaccount, text='第二步', command=step_two)  
    btn_stepTwo.pack(side=LEFT)
    btn_testkill = Button(frm_newaccount, text='一口气', command=onekey)  
    btn_testkill.pack(side=LEFT) 

    mainloop() #进入主循环，程序运行  
