from autoVote_PU_new import puVote
from autoVote_4 import puVote_4
import xlrd
import xlwt
import os
import time
import random

#参数设置
#投票的活动
id='185081'
#投票目标
pid=['40805','40815','40828','40810','40826','40820','40801','40818','40811','40827','40806','40822']
len_pid= len(pid)
#为了投满15票才生效
otherpid=['40816','40803','40821','40817','40814','40813','40829','40824','40808','40825','40819','40807']
len_otherpid= len(otherpid)
i_other=0
'''
物联网工程学院：
潘庭龙  40815
熊伟丽  40828
设计：
王安霞  40810
鲍懿喜  40826
外语：
李健雪 40820
朱义华  40801
理学院：
刘朗 40818
王勇  40811
数媒：章洁  40827
体育：张健  40806
商学院：黄建康  40822
'''




#参数设置

#
addition=''
#可登陆账号excel
filename_login='okUsers'+addition+'.xls'
#投票成功账号excel
filename_voted='FinishUsers'+addition+'.xls'

#是否刷票
isVote=1;
#延时投票控制
isDelay=0
#随机取时间间隔投票
second_from=1
second_to=3

if(isVote==1):
    #用于刷票
    data = xlrd.open_workbook(filename_login)
    #得到第一个工作表
    table = data.sheets()[0]
    #获取行数
    nrows = table.nrows
    #获取列数
    ncols = table.ncols
    print(nrows)
    print(ncols)
    
    #写入数据
    #新建一个excel文件
    file = xlwt.Workbook() #注意这里的Workbook首字母是大写，无语吧
    #新建一个sheet
    table_write = file.add_sheet('okUsers')
    
    j=0
    for i in range(nrows ):
        #读取账号
        if(table.cell(i,0).ctype != 1):#如果单元格格式不是string,则进行转换
            name=str(int(table.cell(i,0).value))
        else:
            name=table.cell(i,0).value
        #读取密码  
        if(table.cell(i,1).ctype != 1):#如果单元格格式不是string,则进行转换
            password=str(int(table.cell(i,1).value))
        else:
            password=table.cell(i,1).value
        #自动投票
    
        
        #用于刷票
        #自动投票
        for ii in range(len_pid):
            
            result=puVote(name,password,id,pid[ii],1)
            
            if(result['login_state']!=1):
                print('登陆失败')
               
            if(result['vote_state']==1):
                print(str(ii+1),end=" ")
            elif(result['vote_state']==-1):
                print('没有投票')  
          # else:
          #     print('第'+str(ii+1)+'位老师投票失败')  
        print("   ",end="   ")
        ok_num=0;
        for iii in range(8):
            result=puVote(name,password,id,otherpid[i_other],1)
            if(result['vote_state']==1):
                print(str(i_other+1),end=" ")
                i_other +=1
                ok_num +=1
            else:
            #    print('投票失败') 
                i_other +=1
            if(i_other==(len_otherpid-1)):
                i_other = 0
            if(ok_num==3):
                success_flag = 1;
                break
            
        #写入数据
        #写入数据table.write(行,列,value)
        
        print(' ')
        print('第'+str(i+1)+'个账号投票完成')
        print(' ')
        #投票成功后增加延迟时间
        if(isDelay==1 and success_flag == 1):
            delay=random.randint(second_from,second_to)
            print(str(delay)+'秒后继续投票')
            time.sleep(delay)
            success_flag = 0;

       
print('Finish')


