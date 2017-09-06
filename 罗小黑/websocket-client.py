import websocket
import _thread
import time
import json


import lxhWebsocketApi
#记录账号信息
account = [ {'account_name':"qq342875289",'account_id':"9401559",'device_id':"1965FBA4-13AA-49C7-BC00-B6356627C74B",'sign':"cd8929990165f5644f1c66c969efd300"},
            {'account_name':"ming1",'account_id':"qq342875289",'device_id':"C4BAAFE8-C98D-49C2-B30F-1A7EA5364BAE",'sign':"f4780b5d9f7226dd149e1d5ba01d08ce"},
            {'account_name':"ming2",'account_id':"qq342875289",'device_id':"00000000-0000-0000-0000-000000000000",'sign':"9ed3339c5462c5f0cd351d5421918439"},
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

def on_message(ws, message):
    
    
    message_json = json.loads(message)
    MsgID = message_json['Header']['MsgID']
    if MsgID == 16308:
        print("收到一条系统通知:"+message_json['Msg']['RetData']['Content'])
    elif MsgID == 16304:
        print("收到一条玩家发言:"+message_json['Msg']['RetData']['ChatMsg'])
    elif MsgID == 16246:
        print("玩家"+message_json['Msg']['RetData']['BossInfo']['BossList']['RoleName']+"发现了一个"+message_json['Msg']['RetData']['BossInfo']['BossList']['Level']+"级的BOSS")
    elif MsgID == 14006:
        print("成功完成扫荡")
    elif MsgID == 10002:
        ws.send(lxhWebsocketApi.api_kill(4,2,10))
        ws.send(lxhWebsocketApi.api_giveVitality())
        ws.send(lxhWebsocketApi.api_getVitality())
    elif MsgID == 20000:   
        if message_json['Msg']['ReqMsgId'] == 16225 or message_json['Msg']['ReqMsgId'] == 16229:
            return None
        elif message_json['Msg']['ReqMsgId'] == 14005 and message_json['Msg']['RetCode'] == 1061:
            print("体力耗尽")
            return None
    print(message)
         
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