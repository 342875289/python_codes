from autoVote_PU import puVote
from autoVote_4 import puVote_4
import xlrd
import xlwt
import os
import time
import random

#参数设置
#投票账户
name=''
password=''
#设置默认密码，针对用户不修改默认密码的情况--暂时未实现
default_password='111111'
#投票的活动
id='167394'
#投票目标 物联网1302-37094
pid='37094'
#
addition=''
#原始账号excel
filename_initial='users'+addition+'.xls'
#可登陆账号excel
filename_login='okUsers'+addition+'.xls'
#投票成功账号excel
filename_voted='FinishUsers'+addition+'.xls'

#是否测试账号可用性
isTest=0;
#是否刷票
isVote=1;
#延时投票控制
isDelay=1
#在60秒~120秒之内随机取时间间隔投票
second_from=5
second_to=10

#用于测试账户
if(isTest==1):
    
    data = xlrd.open_workbook(filename_initial)
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
    table_write = file.add_sheet(filename_login)
    
    j=0
    for i in range(nrows ):
        #读取账号
        if(table.cell(i,0).ctype != 1):#如果单元格格式不是string,则进行转换
            name=str(int(table.cell(i,0).value))
        else:
            name=table.cell(i,0).value
        #读取密码  
        if(table.cell(i,1).ctype != 1):#如果单元格格式不是string,则进行转换
            password=str(int(table.cell(i,1).value))[-6:]
        else:
            password=table.cell(i,1).value[-6:]
        #print(name)
        #print(password)    
        #测试登陆
        result=puVote(name,password,id,pid,0)         
        if(result['login_state']==1):
            print('第'+str(j)+'个登陆成功')
            #写入数据
            #写入数据table.write(行,列,value)
            table_write.write(j,0,name)
            table_write.write(j,1,password)
            table_write.write(j,2,1)
            j=j+1
        else:
            print('登陆失败')
    
    file.save(filename_login)
    print('Finish')

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
        result=puVote(name,password,id,pid,1)
        
        puVote_4(name,password,id,'37056',1)
        
        '''
        if(result['login_state']==1):
            print('登陆成功')
           
        else:
            print('登陆失败')
        '''   
        if(result['login_state']!=1):
            print('登陆失败')
                
        if(result['vote_state']==1):
            print(str(i)+'第'+str(j)+'个投票成功')
            #写入数据
            #写入数据table.write(行,列,value)
            table_write.write(j,0,name)
            table_write.write(j,1,password)
            table_write.write(j,3,1)
            j=j+1
            #投票成功后增加延迟时间
            if(isDelay==1):
                delay=random.randint(second_from,second_to)
                print(str(delay)+'秒后继续投票')
                time.sleep(delay)
        elif(result['vote_state']==-1):
            print('没有投票')  
        else:
            print(str(i)+'投票失败')  
        
    file.save(filename_voted)
    print('Finish')

