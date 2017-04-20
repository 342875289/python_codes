from autoVote_PU import puVote
from autoVote_4 import puVote_4
import xlrd
import xlwt
import os
import time
import random

#参数设置
#投票的活动
id='42047'
#每个账号至少要投多少篇才生效
need_vote_num = 10
#投票目标
pid=['5558']
#为了投满15票才生效
otherpid=['5373','5024','5309','5055','5626','5209','5573','5530','5627','5502','5342','5189','5431','5266','4995','5379','5376','5474','5606','5237','5536','5168','5286','5118','5087','5247','5092','5086','5068','5060','5358','5101','5437','5566','5261','5194','5531','5252','5258','5467','5316','5519','5159','5257','5308','4975','5601','5339','5130','5224','5451','5422','5371','5343','5187','5487','5044']
#参数设置
len_pid= len(pid)
len_otherpid= len(otherpid)
i_other=0
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
        for iii in range( need_vote_num-len_pid ):
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
        
        print('第'+str(i+1)+'个账号投票完成')
        #投票成功后增加延迟时间
        if(isDelay==1 and success_flag == 1):
            delay=random.randint(second_from,second_to)
            print(str(delay)+'秒后继续投票')
            time.sleep(delay)
            success_flag = 0;

       
print('Finish')


