import websocket
import _thread
import time
import json


import lxhWebsocketApi
import lxh_growup_api
#记录账号信息
account = [ {'account_name':"ming1",'account_id':"ming1",'device_id':"C4BAAFE8-C98D-49C2-B30F-1A7EA5364BAE",'sign':"f4780b5d9f7226dd149e1d5ba01d08ce"},
            {'account_name':"ming2",'account_id':"ming2",'device_id':"00000000-0000-0000-0000-000000000000",'sign':"9ed3339c5462c5f0cd351d5421918439"},
            {'account_name':"ming3",'account_id':"qq342875289",'device_id':"1965FBA4-13AA-49C7-BC00-B6356627C74B",'sign':"500af7ae47afac6747874f45dcc2fc8d"},
            {'account_name':"mingmingming",'account_id':"9471816",'device_id':"C4BAAFE8-C98D-49C2-B30F-1A7EA5364BAE",'sign':"689af8192ab5cf92a38dfbe285eff944"},
          ]
#选择使用哪个账号
account_num = 3
#选择进第几个服务器
server_num = 10#注意！！！变更服务器还需要修改websocketIP
#读取账号登录需要的信息
account_name = account[account_num-1]['account_name']
device_id = account[account_num-1]['device_id']
sign = account[account_num-1]['sign']
report_sign = account[account_num-1]['sign']


email_list = []
def on_message(ws, message):
    global email_list
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
        print("收到人物状态1:")
        print("体力CD:%s,金币:%s,钻石:%s,猫粮:%s,体力:%s"%(TiliCD,Gold,Diamond,Food,Tili))
        return None
    elif MsgID == 16106:#收到任务状态
        Gold = message_json['Msg']['RetData']['Wealth']['Gold']
        Diamond = message_json['Msg']['RetData']['Wealth']['Diamond']
        Food = message_json['Msg']['RetData']['Wealth']['Food']
        Tili = message_json['Msg']['RetData']['Wealth']['Tili']       
        print("收到人物状态2:")
        print("金币:%s,钻石:%s,猫粮:%s,体力:%s"%(Gold,Diamond,Food,Tili))
        return None
    elif MsgID == 17104:#成功领取鱼干
        #{"Header":{"MsgID":17104,"ProtoVersion":1454470775},"Msg":{"RetData":{"Tili":[{"Index":1,"StartHour":12,"EndHour":14,"Num":60,"AddedCost":60,"State":1},{"Index":2,"StartHour":17,"EndHour":19,"Num":60,"AddedCost":60,"State":0},{"Index":3,"StartHour":21,"EndHour":23,"Num":60,"AddedCost":60,"State":0}],"Wealth":{"Gold":983400,"Diamond":2209,"Food":594926,"Tili":180,"BarCard":1,"Soul":0,"EquipSoul":0,"Arena":0,"Bgz":0,"Legion":2080,"Horn":0,"BarMoney":3,"DollsMoney":4},"DataChange":{"Hero":{"New":[],"Update":[],"Del":[]},"BagItem":{"New":[],"Update":[],"Del":[]},"BagEquip":{"New":[],"Update":[],"Del":[]},"HeroFrag":{"New":[],"Update":[],"Del":[]},"EquipFrag":{"New":[],"Update":[],"Del":[]}}}}}
        print('成功领取鱼干')
    elif MsgID == 16306:#收到频道聊天信息汇总
        print('收到聊天信息')
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
            RoleName = boss_list[i]['RoleName'] 
            Level = boss_list[i]['Level'] 
            BossTid = boss_list[i]['BossTid'] 
            BossDegree = boss_list[i]['BossDegree'] 
            print("%s发现了%d级的Boss-%d,BossTid:%d,BossDegree:%d"%(RoleName,Level,BossRoleId,BossTid,BossDegree))
    elif MsgID == 16248:#Boss列表    
        print("-------收到Boss信息-------")
        print("-------收到Boss信息-------")
        print("-------收到Boss信息-------")
    elif MsgID == 16902:#收到右键列表
        print("收到邮件信息")
        email_list = message_json['Msg']['RetData']['MailList']
        return None
    elif MsgID == 16246:
        print("玩家"+message_json['Msg']['RetData']['BossInfo']['BossList']['RoleName']+"发现了一个"+message_json['Msg']['RetData']['BossInfo']['BossList']['Level']+"级的BOSS")
    elif MsgID == 14006:
        Tili = message_json['Msg']['RetData']['Wealth']['Tili']
        Level = message_json['Msg']['RetData']['BaseInfo']['Level'] 
        print("成功完成扫荡,体力剩余:%d,当前等级为:%d"%(Tili,Level))
        return None
    elif MsgID == 10002:
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
    print(message)

def start_game(ws):
    do_something(ws)
    
def step_one(ws):
    print("开始执行-第1步")
    #创建新角色
    ws.send(lxh_growup_api.api_creatname("明明明"+str(account_num)))
    #黑粉催更
    ws.send(lxh_growup_api.api_getitem())
    #修改阵容-加入千针
    ws.send(lxh_growup_api.api_changelocation([0,1041,0,0,1043,0,0,0,0,0,0,0])) 
    print("执行完成,请手动出战第一章1,2,3")
    
def step_two(ws):
    global email_list
    
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
    
    print("执行完成,请手动出战第一章4,5,6")
    
def step_three(ws):
    
    #增加法宝经验
    ws.send(lxh_growup_api.api_treasure_exp_up(2022101, 1))
    
    #领取每日任务奖励1
    ws.send(lxh_growup_api.api_get_dailytask_reward(1))
    

def do_something(ws):
    global email_list
    #心跳包
    ws.send(lxh_growup_api.api_sendHeartPackage1())
    
    '''
    #扫荡第一章第2个boss--30次
    for i in range(5):
        ws.send(lxh_growup_api.api_kill(1, 2, 1))
    '''
    #收取体力
    ws.send(lxh_growup_api.api_getVitality())
    #赠送体力
    ws.send(lxh_growup_api.api_giveVitality())
    
    #领取鱼干
    ws.send(lxh_growup_api.api_get_fish())
    
    #添加大号为好友
    #ws.send(lxh_growup_api.api_addfriend(9401559))
    #加入公会
    #ws.send(lxh_growup_api.api_addLegion(47713))
    
    
def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
                
        ws.send(lxhWebsocketApi.api_login(account_name,device_id,sign,server_num))
       
        #time.sleep(5)
        #str= lxhWebsocketApi.api_kill(10)
        #ws.send(str)
        #print(str)
    #    ws.close()
    #    print("websocket close")
    _thread.start_new_thread(run, ())


if __name__ == "__main__":
    
    websocket.enableTrace(False)
    #ws = websocket.WebSocketApp("ws://47.93.126.149:8002",
    ws = websocket.WebSocketApp("ws://47.93.150.36:8002",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()