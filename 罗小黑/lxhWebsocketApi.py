import websocket
import time
import json

import lxhHttpApi

def api_login(account_name,device_id,sign,server_num):
    account_data = lxhHttpApi.getToken(account_name,device_id,sign)
         
    account_info={
        'ticket': account_data['ticket'],
        'server_num': server_num,
        'version_str': account_data['version_str'],
        'device_id': device_id,
        'account_name': account_name,
        'account_id': account_data['account_id']
    }
    
    #print(account_name)
    #print(account_data['ticket'])
    
    data = {
    'Header' : {'MsgID':10001},
    'Msg' : 
        {
            "Ticket":account_info['ticket'],
            "ServerId":120000+account_info['server_num'],
            "Version":account_info['version_str'],
            "Platform":12,
            "IMEI":account_info['device_id'],
            "ChannelId":70001,
            "Account":account_info['account_name'],
            "AccountId":account_info['account_id']
        }
    }
    request_str = json.dumps(data)
    print(account_info['account_name']+"尝试登陆")
    return request_str


#添加好友
def api_addfriend(playerId):
    requset_str = '{"Header":{"MsgID":16203},"Msg":{"PlayerId":'+playerId+'}}'
    print("申请添加好友")
    return requset_str

#取名字，用于新建角色
def api_creatname(account_name):
    requset_str = '{"Header":{"MsgID":16003},"Msg":{"RoleName":"'+account_name+'","AvatarId":2}}'
    print("创建用户名"+account_name)
    return requset_str
#收取体力
def api_getVitality():
    requset_str = '{"Header":{"MsgID":16229},"Msg":{}}'
    print("收取体力")
    return requset_str

#赠送体力
def api_giveVitality():
    requset_str = '{"Header":{"MsgID":16225},"Msg":{}}'
    print("赠送体力")
    return requset_str

#好友互动
def api_touchFriend(friend_id):
    requset_str = '{"Header":{"MsgID":16213},"Msg":{"PlayerId":'+friend_id+',"ActionType":1}}'
    print("进行好友互动")
    return requset_str

#扫荡
def api_kill(character,boss,times):
    requset_str = '{"Header":{"MsgID":14005},"Msg":{"LevelId":'+str(character)+'000'+str(boss*3)+',"LevelType":1,"Count":'+str(times)+',"ForceId":'+str(character)+'}}'
    print("对第"+str(character)+"章第"+str(boss)+"个BOSS进行了"+str(times)+"次扫荡")
    return requset_str
