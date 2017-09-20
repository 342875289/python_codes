from tkinter import * 
import websocket
import _thread
import time
import json


import lxhWebsocketApi
import lxh_growup_api
#记录账号信息
account = [ {'account_name':"ming1",'device_id':"C4BAAFE8-C98D-49C2-B30F-1A7EA5364BAE",'sign':"f4780b5d9f7226dd149e1d5ba01d08ce"},
            {'account_name':"ming2",'device_id':"00000000-0000-0000-0000-000000000000",'sign':"9ed3339c5462c5f0cd351d5421918439"},
            {'account_name':"ming3",'device_id':"1965FBA4-13AA-49C7-BC00-B6356627C74B",'sign':"500af7ae47afac6747874f45dcc2fc8d"},
            {'account_name':"ming4",'device_id':"00000000-0000-0000-0000-000000000000",'sign':"4a754ec554ce05e80f81d6a3e0e09d44"},
            {'account_name':"ming5",'device_id':"00000000-0000-0000-0000-000000000000",'sign':"24dc23aadadbd58dad798405623b9a09"},
            {'account_name':"ming6",'device_id':"00000000-0000-0000-0000-000000000000",'sign':"be34338837b689c49234d7af552c5df2"},
            {'account_name':"ming7",'device_id':"00000000-0000-0000-0000-000000000000",'sign':"f0a2f2ec8a164c215869162602aef4d6"},
            {'account_name':"ming8",'device_id':"00000000-0000-0000-0000-000000000000",'sign':"dc9aa8a53d08348e38e0866c5bcdff4c"},
            {'account_name':"ming9",'device_id':"00000000-0000-0000-0000-000000000000",'sign':"0c1d3bb64900727d3848ab7e1a32e0a9"},
            
            {'account_name':"ming10",'device_id':"00000000-0000-0000-0000-000000000000",'sign':"ee15dbe4a066fac7a5da5b711a292e42"},
            {'account_name':"ming11",'device_id':"00000000-0000-0000-0000-000000000000",'sign':"14ce13b71a96632e61bdbabe3834b8a2"},
            {'account_name':"ming12",'sign':"ce15bc39963ca495d9b8b4b1523ddfc4",'device_id':"00000000-0000-0000-0000-000000000000"},
            {'account_name':"ming13",'sign':"04a7945ab3d2eb614da73e132995e959",'device_id':"00000000-0000-0000-0000-000000000000"},
            {'account_name':"ming14",'sign':"55597c8934e3a8aa9ecdcea88688cdc8",'device_id':"00000000-0000-0000-0000-000000000000"},
            {'account_name':"ming15",'sign':"69accd65d599da2742ca07defee276ab",'device_id':"00000000-0000-0000-0000-000000000000"},
            {'account_name':"ming16",'sign':"70bdfb0f8f50798018495b0994f979d0",'device_id':"00000000-0000-0000-0000-000000000000"},
            {'account_name':"ming17",'sign':"2747e94ccd4da716a1444fe345ed56da",'device_id':"00000000-0000-0000-0000-000000000000"},
            {'account_name':"ming18",'sign':"2af61b1c7dfb265880129caca2a33452",'device_id':"00000000-0000-0000-0000-000000000000"},
            {'account_name':"ming19",'sign':"6147ce70cafb80aa3d2a3d468ae641d6",'device_id':"00000000-0000-0000-0000-000000000000"},
            {'account_name':"ming20",'sign':"44cfed1c4612014975a01a43347700c7",'device_id':"00000000-0000-0000-0000-000000000000"},
            {'account_name':"ming21",'sign':"0700a1092866264ca29e891c5b291cc2",'device_id':"00000000-0000-0000-0000-000000000000"},
            {'account_name':"ming22",'sign':"7be72abd6787c08072cc9312a136323e",'device_id':"00000000-0000-0000-0000-000000000000"},
            {'account_name':"ming23",'sign':"ee8b3bde15f0a1ea3785d5d3da4c03b9",'device_id':"00000000-0000-0000-0000-000000000000"},
            {'account_name':"ming24",'sign':"d50135a4bebbccc2998b36c9ad38eb6f",'device_id':"00000000-0000-0000-0000-000000000000"},
            {'account_name':"ming25",'sign':"297e83e9fab6d207df053e3034bed7ea",'device_id':"00000000-0000-0000-0000-000000000000"},
            {'account_name':"ming26",'sign':"a7fefccd546ba78619c712cedd45d1f0",'device_id':"00000000-0000-0000-0000-000000000000"},
            {'account_name':"mingmingming",'device_id':"C4BAAFE8-C98D-49C2-B30F-1A7EA5364BAE",'sign':"689af8192ab5cf92a38dfbe285eff944"},
          ]

            
            
#选择使用哪个账号
account_num = 0
#选择进第几个服务器
server_num = 10#注意！！！变更服务器还需要修改websocketIP
#
level_oldaccount = 59
level_limit = 45
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
        print("成功完成扫荡,体力剩余:%d,当前等级为:%d"%(Tili,level))
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
    ws.send(lxh_growup_api.api_creatname("明明明"+var_accountNumber.get()))
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
    ws.send(lxh_growup_api.api_addfriend(9401559))
    #加入公会
    ws.send(lxh_growup_api.api_addLegion(47713))
    
    #新账号任务系列
    ws.send(lxh_growup_api.api_newAccountTask1())
    ws.send(lxh_growup_api.api_newAccountTask2(10))
    ws.send(lxh_growup_api.api_newAccountTask2(15))
    ws.send(lxh_growup_api.api_newAccountTask4(10))
    ws.send(lxh_growup_api.api_newAccountTask5())
    #ws.send(lxh_growup_api.api_newAccountTask6())
    #ws.send(lxh_growup_api.api_newAccountTask6())
    #ws.send(lxh_growup_api.api_newAccountTask6())
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

def do_dailyTask(isgetExp):
    global ws
    ws.send(lxh_growup_api.api_newAccountTask9())
    ws.send(lxh_growup_api.api_dailyTask2())
    ws.send(lxh_growup_api.api_dailyTask3())
    ws.send(lxh_growup_api.api_touchFriend(9401559,4))
    ws.send(lxh_growup_api.api_touchFriend(9401559,1))  
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
    #开启并领取猫粮宴
    ws.send(lxh_growup_api.api_dailyTask6())
    ws.send(lxh_growup_api.api_dailyTask5())
    #兑换猫饭金币
    ws.send(lxh_growup_api.api_dailyTask1())
    ws.send(lxh_growup_api.api_dailyTask4())
    #每日签到
    ws.send(lxh_growup_api.api_newAccountTask5())  
    ws.send(lxh_growup_api.api_dailyTask12())
    ws.send(lxh_growup_api.api_dailyTask14())
    #买体力
    ws.send(lxh_growup_api.api_newAccountTask9())  
    ws.send(lxh_growup_api.api_newAccountTask9()) 
    ws.send(lxh_growup_api.api_newAccountTask9()) 
    #投资会馆等级
    ws.send(lxh_growup_api.api_newAccountTask6(5,1))
    ws.send(lxh_growup_api.api_newAccountTask6(5,1))
    ws.send(lxh_growup_api.api_newAccountTask6(6,1))
    #购买商店物品两次
    ws.send(lxh_growup_api.api_get_shop_items())
    time.sleep(5)
    if item_number[0]!=0 :
        ws.send(lxh_growup_api.api_buy_shop_items(item_number[0]))
        ws.send(lxh_growup_api.api_buy_shop_items(item_number[1]))
    #装备
    if equipId != 0:
        #装备强化
        ws.send(lxh_growup_api.api_dailyTask9(equipId))
        #装备熔炼
        ws.send(lxh_growup_api.api_dailyTask8(equipId))
    #喂榨菜丹
    ws.send(lxh_growup_api.api_dailyTask7())
    ws.send(lxh_growup_api.api_dailyTask7())
    ws.send(lxh_growup_api.api_dailyTask7())
    if isgetExp:
        ws.send(lxh_growup_api.api_get_dailytask_reward(8))
        ws.send(lxh_growup_api.api_get_dailytask_reward(7))
        ws.send(lxh_growup_api.api_get_dailytask_reward(20)) 
        ws.send(lxh_growup_api.api_get_dailytask_reward(5))
        ws.send(lxh_growup_api.api_get_dailytask_reward(9))
        ws.send(lxh_growup_api.api_get_dailytask_reward(10))
        ws.send(lxh_growup_api.api_get_dailytask_reward(13))
        ws.send(lxh_growup_api.api_newAccountTask7(20))
        ws.send(lxh_growup_api.api_newAccountTask7(50))
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
            #领取鱼干
            ws.send(lxh_growup_api.api_get_fish()) 
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
                do_dailyTask(False)
                print("账号:"+str(int(var_accountNumber.get())-1)+'超出等级限制,不领取每日任务经验奖励')
            else:
                do_dailyTask(True)
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
                do_dailyTask_once(False)
                print("账号:"+str(int(var_accountNumber.get())-1)+'超出等级限制,不领取一次性每日任务经验奖励')
            else:
                do_dailyTask_once(True)
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
        #领取鱼干
        ws.send(lxh_growup_api.api_get_fish()) 
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
            do_dailyTask(False)
            print("账号:"+str(int(var_accountNumber.get())-1)+'超出等级限制,不领取每日任务经验奖励')
        else:
            do_dailyTask(True)
            print("账号:"+str(int(var_accountNumber.get())-1)+'完成每日任务')
        time.sleep(1)
    def dailyTask_once():
        global ws,item_number,equipId
        if(level>level_limit):
            do_dailyTask_once(False)
            print("账号:"+str(int(var_accountNumber.get())-1)+'超出等级限制,不领取一次性每日任务经验奖励')
        else:
            do_dailyTask_once(True)
            print("账号:"+str(int(var_accountNumber.get())-1)+'完成一次性每日任务')
        time.sleep(1)
            
    def test():
        global ws,isBoss,equipId,item_number,count_finish,count_isBoss,count_noTili
        count_finish = 0
        count_isBoss = 0
        count_noTili = 0
        autoFromNumber = int(var_autoFromNumber.get() ) 
        autoToNumber = int(var_autoToNumber.get() )
        for i in range(autoFromNumber,autoToNumber):
            equipId = 0
            item_number[0] = 0
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
    ws.send(lxh_growup_api.api_newAccountTask6(1,1))
    ws.send(lxh_growup_api.api_newAccountTask6(1,1))
    ws.send(lxh_growup_api.api_newAccountTask6(1,1))
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
    #领取活跃度奖励
    ws.send(lxh_growup_api.api_newAccountTask7(20))
    ws.send(lxh_growup_api.api_newAccountTask7(50))
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
    for i in [3,10,13,20,23,30,33,40,43,50,53]:
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
    #黑粉催更
    ws.send(lxh_growup_api.api_getitem())
    #永久月卡
    ws.send(lxh_growup_api.api_dailyTask25())
    #领取活跃度奖励
    ws.send(lxh_growup_api.api_newAccountTask7(20))
    ws.send(lxh_growup_api.api_newAccountTask7(50))
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
    var_accountNumber.set("2")
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
    btn_kill = Button(frm_login, text='扫荡', command=kill)  
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
    btn_autoKill = Button(frm_autoKill, text='自动扫荡', command=AutoKill)  
    btn_autoKill.pack(side=RIGHT)
    
    label_autoKill = Label(frm_autoKill)  
    label_autoKill['text'] = '已完成:0,有Boss:0,体力耗尽:0'  
    label_autoKill.pack(side=RIGHT)
    #大号frame
    frm_oldaccount = Frame(win)
    frm_oldaccount.pack(side=TOP)
    label_oldaccount = Label(frm_oldaccount)  
    label_oldaccount['text'] = '大号操作区:'  
    label_oldaccount.pack(side=LEFT) 
    btn_oldaccount_login = Button(frm_oldaccount, text='登录大号', command=logout_in_oldaccount)  
    btn_oldaccount_login.pack(side=LEFT)
    btn_oldaccount_logout = Button(frm_oldaccount, text='注销', command=logout)  
    btn_oldaccount_logout.pack(side=LEFT)
    btn_oldaccount_dailytask = Button(frm_oldaccount, text='每日任务', command=oldaccount_dailytask)  
    btn_oldaccount_dailytask.pack(side=LEFT)
    btn_oldaccount_dailytask_once = Button(frm_oldaccount, text='只能做一次的每日任务', command=oldaccount_dailytask_once)  
    btn_oldaccount_dailytask_once.pack(side=LEFT)
    btn_oldaccount_soul = Button(frm_oldaccount, text='灵质熔炼', command=strengthen_soul)  
    btn_oldaccount_soul.pack(side=LEFT) 
    btn_oldaccount_zhua = Button(frm_oldaccount, text='抓娃娃', command=get_pets_by_zhuawawa)  
    btn_oldaccount_zhua.pack(side=LEFT) 
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
