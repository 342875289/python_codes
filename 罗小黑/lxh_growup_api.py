import websocket
import time
import json

import lxhHttpApi
from app import equipId

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


#取名字，用于新建角色
def api_creatname(account_name):
    requset_str = '{"Header":{"MsgID":16003},"Msg":{"RoleName":"'+account_name+'","AvatarId":2}}'
    print("创建用户名"+account_name)
    return requset_str

#黑粉催更
def api_getitem():
    requset_str = '{"Header":{"MsgID":17001},"Msg":{"DrawType":2}}'
    print("进行一次黑粉催更")
    return requset_str


#心跳包1--疑似查询
def api_sendHeartPackage1():
    requset_str = '{"Header":{"MsgID":16057},"Msg":{}}'
    print("发送心跳包-查询人物状态")
    return requset_str
#心跳包2--疑似查询
def api_sendHeartPackage2():
    requset_str = '{"Header":{"MsgID":16105},"Msg":{}}'
    print("发送心跳包-查询人物状态")
    return requset_str

#修改出场阵容
def api_changelocation(Layout):
    requset_str = '{"Header":{"MsgID":13401},"Msg":{"GodId":1,"Layout":'+str(Layout)+',"TechId":0}}'
    print("修改出场阵容为%s"%(str(Layout)))
    return requset_str

#出战
def api_kill_indisplay(character,boss):
    requset_str ='{"Header":{"MsgID":14001},"Msg":{"TeamList":{},"LevelType":1,"LevelId":'+str(character)+'000'+str(boss*3)+',"ForceId":'+str(character)+'}}'
    print("出战第"+str(character)+"章第"+str(boss)+"节")
    return requset_str

def api_testkill1():
    requset_str ='{"Header":{"MsgID":14001},"Msg":{"TeamList":{},"LevelType":1,"LevelId":20001,"ForceId":2}}'
    print("testkill1-14001")
    return requset_str
def api_testkill2():
    requset_str ='{"Header":{"MsgID":16353},"Msg":{"DungeonType":2,"LevelWave":1,"LevelId":20001}}'
    print("testkill2-16353")
    return requset_str
def api_testkill3():
    requset_str ='{"Header":{"MsgID":14003},"Msg":{"RandomSeed":1503540804,"LevelId":20001,"ForceId":2,"Energy":100,"TeamList":{},"Sign":"357e36b13a18a471c1108ed19d0f8046","Result":3,"LevelType":1}}'
    print("testkill3-14003")
    return requset_str
#领取星星奖励
def api_get_stars_reward(character,starCount):
    requset_str ='{"Header":{"MsgID":14007},"Msg":{"StarCount":'+str(starCount)+',"LevelType":1,"ForceId":'+str(character)+'}}'
    print("领取第"+str(character)+"章的"+str(starCount)+"个星星的奖励")
    return requset_str


#寻宝
def api_get_explor_reward(character):
    requset_str ='{"Header":{"MsgID":18701},"Msg":{"LevelType":1,"ForceId":'+str(character)+'}}'
    print("对第"+str(character)+"章进行一次寻宝")
    return requset_str


#穿戴装备
def api_weapons_up():
    requset_str ='{"Header":{"MsgID":12027},"Msg":{"SrcSlot":{"HeroTid":0,"SlotType":2,"EquipId":1},"DstSlot":{"HeroTid":1043,"SlotType":1,"EquipId":0}}}'
    print("穿戴装备，参数待定")
    return requset_str

#一键强化装备
def api_weapons_strengthen(HeroTid):
    requset_str ='{"Header":{"MsgID":12031},"Msg":{"TemplateId":'+str(HeroTid)+'}}'
    print("强化了%d的装备"%HeroTid)
    return requset_str

#升级宠物技能
def api_pets_skills_strengthen(HeroTid,skillIndex,toLevel):
    requset_str ='{"Header":{"MsgID":12041},"Msg":{"TemplateId":'+str(HeroTid)+',"Index":'+str(skillIndex)+',"ToLevel":'+str(toLevel)+'}}'
    print("升级了了%d的第%d个技能到%d级装备"%(HeroTid,skillIndex,toLevel))
    return requset_str
#宠物进阶
def api_pets_quality_strengthen(HeroTid):
    requset_str ='{"Header":{"MsgID":12023},"Msg":{"TemplateId":'+str(HeroTid)+'}}'
    print("进阶了%d的品质"%(HeroTid))
    return requset_str

#合成宠物
def api_get_pets_byCompose(HeroTid):
    requset_str ='{"Header":{"MsgID":12001},"Msg":{"TemplateId":'+str(HeroTid)+'}}'
    print("合成了新的宠物:%d"%(HeroTid))
    return requset_str

#增加宠物经验
def api_pets_exp_up(HeroTid,ItemTid,Count):
    requset_str ='{"Header":{"MsgID":12021},"Msg":{"HeroTid":'+str(HeroTid)+',"ItemTid":'+str(ItemTid)+',"Count":'+str(Count)+'}}'
    print("使用%d个%d增加了宠物%d的经验"%(HeroTid,ItemTid,Count))
    return requset_str


#增加法宝经验
def api_treasure_exp_up(ItemTid,Count):
    requset_str ='{"Header":{"MsgID":13201},"Msg":{"ItemTid":'+str(ItemTid)+',"Count":'+str(Count)+'}}'
    print("使用%d个%d增加了法宝经验"%(ItemTid,Count))
    return requset_str

#查看邮件
def api_look_email_reward(MailId):
    requset_str ='{"Header":{"MsgID":16903},"Msg":{"MailId":'+str(MailId)+'}}'
    print("领取了邮件%d中的物品"%(MailId))
    return requset_str

#领取邮箱物品
def api_get_email_reward(MailId):
    requset_str ='{"Header":{"MsgID":16905},"Msg":{"MailId":'+str(MailId)+'}}'
    print("领取了邮件%d中的物品"%(MailId))
    return requset_str

#收取所有邮件奖励
def api_get_all_email_reward(ws,email_list):
    if email_list :
        print("存在邮件")
        #获取邮件礼物
        for i in range(len(email_list)):
            print("收取第%d封邮件"%(i+1))
            ws.send(api_look_email_reward(email_list[i]['MailId']))
            ws.send(api_get_email_reward(email_list[i]['MailId']))
        email_list = [] 
    else:
        print("暂无邮件")

#领取当前时段的鱼干
def api_get_fish():
    requset_str ='{"Header":{"MsgID":17103},"Msg":{}}'
    print("领取了鱼干")
    return requset_str

#获取商店物品信息
def api_get_shop_items():
    requset_str ='{"Header":{"MsgID":18601},"Msg":{}}'
    print("获取商店物品信息")
    return requset_str

#购买商店物品
def api_buy_shop_items(ShopItemIndex):
    requset_str ='{"Header":{"MsgID":18605},"Msg":{"ShopItemIndex":'+str(ShopItemIndex)+',"ShopType":1}}'
    print("购买商店物品")
    return requset_str

#添加好友
def api_addfriend(playerId):
    requset_str = '{"Header":{"MsgID":16203},"Msg":{"PlayerId":'+str(playerId)+'}}'
    print("申请添加好友")
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
def api_touchFriend(friend_id,ActionType):
    requset_str = '{"Header":{"MsgID":16213},"Msg":{"PlayerId":'+str(friend_id)+',"ActionType":'+str(ActionType)+'}}'
    print("进行好友互动")
    return requset_str
#创建公会
def api_creatLegion(LegionName):
    requset_str = '{"Header":{"MsgID":15505},"Msg":{"IconId":1011,"LegionName":'+str(LegionName)+'}}'
    print("创建公会:"+str(LegionName))
    return requset_str
#加入公会
def api_addLegion(LegionId):
    requset_str = '{"Header":{"MsgID":15507},"Msg":{"LegionId":'+str(LegionId)+'}}'
    print("申请加入公会")
    return requset_str
#退出公会
def api_quitLegion():
    requset_str = '{"Header":{"MsgID":15513},"Msg":{}}'
    print("退出公会")
    return requset_str
#扫荡
def api_kill(character,boss,times):
    requset_str = '{"Header":{"MsgID":14005},"Msg":{"LevelId":'+str(character)+'000'+str(boss*3)+',"LevelType":1,"Count":'+str(times)+',"ForceId":'+str(character)+'}}'
    print("对第"+str(character)+"章第"+str(boss)+"个BOSS进行了"+str(times)+"次扫荡")
    return requset_str
#灵质熔炼-金-5020111,木-5020131,水-5020121,火-5020141,土-5020151
#5030211,,5030221,
def api_strengthen_soul(thing,level):
    item_number = thing + (level-1)*10100
    item_string = str(item_number)+','+str(item_number)+','+str(item_number)+','+str(item_number)+','+str(item_number)
    requset_str = '{"Header":{"MsgID":12601},"Msg":{"ItemList":['+item_string+']}}'
    print("灵质熔炼")
    return requset_str

#打开背包中的箱子
def api_open_box_inBag(Count,TemplateId):
    requset_str = '{"Header":{"MsgID":12605},"Msg":{"Count":'+str(Count)+',"TemplateId":'+str(TemplateId)+'}}'
    print("打开箱子")
    return requset_str

#领取等级奖励-榨菜丹 300006 300007 - 300015
def api_get_level_reward(TaskId):
    requset_str = '{"Header":{"MsgID":13603},"Msg":{"TaskId":'+str(300000+TaskId)+'}}'
    #print("领取等级奖励-榨菜丹")
    return requset_str

#抓娃娃第一步-投币
def api_get_pets_by_zhuawawa_1():
    requset_str = '{"Header":{"MsgID":18751},"Msg":{}}'
    print("抓娃娃第一步-投币")
    return requset_str
#抓娃娃第二步-抓
def api_get_pets_by_zhuawawa_2(Index):
    requset_str = '{"Header":{"MsgID":18753},"Msg":{"Index":'+str(Index)+'}}'
    print("抓娃娃第二步-抓")
    return requset_str
#
#新账号任务11-猫村理财
def api_newAccountTask11():
    requset_str = '{"Header":{"MsgID":17129},"Msg":{}}'
    print("猫村理财")
    return requset_str
#新账号任务12-猫村理财
def api_newAccountTask12():
    requset_str = '{"Header":{"MsgID":17127},"Msg":{}}'
    print("猫村理财")
    return requset_str
#新账号任务2-疯狂升级-10-15-20-25-30-35-40
def api_newAccountTask2(level):
    requset_str = '{"Header":{"MsgID":17109},"Msg":{"Level":'+str(level)+'}}'
    print("疯狂升级")
    return requset_str
#新账号任务3-登录有礼-1~14
def api_newAccountTask3(Day):
    requset_str = '{"Header":{"MsgID":17313},"Msg":{"Day":'+str(Day)+'}}'
    print("登录有礼")
    return requset_str
#新账号任务4-冲级送礼-10-20-25-30-32-34-36-38-40-45-50
def api_newAccountTask4(level):
    requset_str = '{"Header":{"MsgID":17303},"Msg":{"Level":'+str(level)+'}}'
    print("冲级送礼")
    return requset_str
#新账号任务5-每日签到
def api_newAccountTask5():
    requset_str = '{"Header":{"MsgID":17101},"Msg":{}}'
    print("每日签到")
    return requset_str

#新账号任务6-投资会馆等级：1-会馆等级，2-会馆容量,3-会馆BOSS,5-鱼干总数,6-个人鱼干数
def api_newAccountTask6(LegionTechId,Type):
    requset_str = '{"Header":{"MsgID":15525},"Msg":{"LegionTechId":'+str(LegionTechId)+',"Type":'+str(Type)+'}}'
    print("投资会馆等级")
    return requset_str
#新账号任务7-领取活跃度奖励-20-50-100-130
def api_newAccountTask7(Active):
    requset_str = '{"Header":{"MsgID":13615},"Msg":{"Active":'+str(Active)+'}}'
    print("领取活跃度奖励")
    return requset_str
#新账号任务8-全民基金福利-20-50-100-130
def api_newAccountTask8(Count):
    requset_str = '{"Header":{"MsgID":17417},"Msg":{"Count":'+str(Count)+'}}'
    print("领取全民基金福利")
    return requset_str
#新账号任务9-买鱼干
def api_newAccountTask9():
    requset_str = '{"Header":{"MsgID":16051},"Msg":{"ExchangeType":3}}'
    print("买鱼干")
    return requset_str

#领取每日任务奖励
def api_get_dailytask_reward(TaskType):
    #每日奖励---1
    #普通副本10次---2
    #收获农田---4
    #购买两次商品---5
    #普通催更3次---6
    #兑换金币---7
    #兑换猫饭---8
    #装备强化---9
    #装备熔炼---10
    #好友互动---12
    #角色修炼---13
    #后山探险---16
    #会馆捐献---20
    requset_str ='{"Header":{"MsgID":13613},"Msg":{"TaskType":'+str(TaskType)+'}}'
    print("领取了第%d个每日任务奖励"%TaskType)
    return requset_str
#每日任务1-兑换猫饭---8
def api_dailyTask1():
    requset_str = '{"Header":{"MsgID":16051},"Msg":{"ExchangeType":2}}'
    print("兑换猫饭")
    return requset_str
#每日任务2-收获农田---4
def api_dailyTask2():
    requset_str = '{"Header":{"MsgID":13007},"Msg":{"BuildingId":5}}'
    print("收获农田")
    return requset_str
#每日任务3-普通催更3次---6
def api_dailyTask3():
    requset_str = '{"Header":{"MsgID":17001},"Msg":{"DrawType":1}}'
    print("普通催更")
    return requset_str
#每日任务4-兑换金币---7
def api_dailyTask4():
    requset_str = '{"Header":{"MsgID":16051},"Msg":{"ExchangeType":1}}'
    print("兑换金币")
    return requset_str
#每日任务-领取会馆猫粮
def api_dailyTask5():
    requset_str = '{"Header":{"MsgID":15579},"Msg":{"Type":0}}'
    print("领取会馆猫粮")
    return requset_str

#每日任务-开启会馆猫粮宴
def api_dailyTask6():
    requset_str = '{"Header":{"MsgID":15577},"Msg":{}}'
    print("开启会馆猫粮宴")
    return requset_str

#每日任务-榨菜丹给千针修炼
def api_dailyTask7():
    requset_str = '{"Header":{"MsgID":12151},"Msg":{"TemplateId":1043,"Count":1,"Type":1}}'
    print("榨菜丹给千针修炼")
    return requset_str
#每日任务-装备熔炼
def api_dailyTask8(equipId):
    requset_str = '{"Header":{"MsgID":12663},"Msg":{"EquipList":['+str(equipId)+'],"FragList":{}}}'
    print("装备熔炼")
    return requset_str
#每日任务-装备强化
def api_dailyTask9(equipId):
    requset_str = '{"Header":{"MsgID":12651},"Msg":{"SrcSlot":{"HeroTid":0,"SlotType":2,"EquipId":'+str(equipId)+'},"ToLevel":20}}'
    print("装备强化")
    return requset_str
#每日任务-在线礼包
def api_dailyTask10():
    requset_str = '{"Header":{"MsgID":17117},"Msg":{}}'
    print("在线礼包")
    return requset_str
#每日任务-世界冒险一键收获
def api_dailyTask11():
    requset_str = '{"Header":{"MsgID":15007},"Msg":{}}'
    print("世界冒险一键收获")
    return requset_str
#每日任务-愿望转盘
def api_dailyTask12():
    requset_str = '{"Header":{"MsgID":17113},"Msg":{}}'
    print("愿望转盘")
    return requset_str
#每日任务-村的日常
def api_dailyTask13(TrialTyp,Level):
    requset_str = '{"Header":{"MsgID":14107},"Msg":{"TrialType":'+str(TrialTyp)+',"Level":'+str(Level)+'}}'
    print("村的日常,副本:"+str(TrialTyp)+",等级:"+str(Level))
    return requset_str
#每日任务-会馆成员每日福利
def api_dailyTask14():
    requset_str = '{"Header":{"MsgID":15585},"Msg":{}}'
    print("会馆成员每日福利")
    return requset_str
#每日任务-会馆练武场收取奖励
def api_dailyTask15(Index):
    requset_str = '{"Header":{"MsgID":15589},"Msg":{"Index":'+str(Index)+'}}'
    print("会馆练武场收取奖励")
    return requset_str
#每日任务-会馆谛听碎片抽奖开局
def api_dailyTask16():
    requset_str = '{"Header":{"MsgID":15571},"Msg":{}}'
    print("会馆谛听碎片抽奖开局")
    return requset_str
#每日任务-会馆谛听碎片-继续
def api_dailyTask17():
    requset_str = '{"Header":{"MsgID":15573},"Msg":{}}'
    print("会馆谛听碎片-见好就收")
    return requset_str
#每日任务-会馆谛听碎片-见好就收
def api_dailyTask18():
    requset_str = '{"Header":{"MsgID":15575},"Msg":{}}'
    print("会馆谛听碎片-见好就收")
    return requset_str

#每日任务-会馆练武场-训练
#1015-无限,1042-青丘,1062-秃贝,1032-大吉,1201-喷火小黑,1024-罗小白,1034-元月
def api_dailyTask19(TemplateId,Index):
    requset_str = '{"Header":{"MsgID":15587},"Msg":{"TemplateId":'+str(TemplateId)+',"Index":'+str(Index)+',"TrainMode":1}}'
    print("会馆练武场收取奖励")
    return requset_str
#每日任务-领取会馆猫粮-钻石
def api_dailyTask20():
    requset_str = '{"Header":{"MsgID":15579},"Msg":{"Type":2}}'
    print("领取会馆猫粮-用钻石")
    return requset_str
#每日任务-后山探险
def api_dailyTask21():
    requset_str = '{"Header":{"MsgID":14633},"Msg":{}}'
    print("后山探险")
    return requset_str
#每日任务-后山探险-查看奖励
def api_dailyTask22():
    requset_str = '{"Header":{"MsgID":14619},"Msg":{}}'
    print("后山探险-查看奖励")
    return requset_str
#每日任务-后山探险-领取奖励
#3-3,3-10,3-13,20
def api_dailyTask23(Index,Layer):
    requset_str = '{"Header":{"MsgID":14617},"Msg":{"Index":'+str(Index)+',"Layer":'+str(Layer)+'}}'
    print("后山探险-领取奖励")
    return requset_str
#每日任务-后山探险-查看奖励2
def api_dailyTask24():
    requset_str = '{"Header":{"MsgID":14627},"Msg":{}}'
    print("后山探险-查看奖励2")
    return requset_str