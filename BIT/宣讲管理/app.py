import urllib.request
import json
import time
import re
import math
import traceback

from bs4 import BeautifulSoup

import httpapi,process_context,excel,mainFuncs

the_lastone_id = 134571

page_items_limit = 100
enterprise_list_not_confirm = []
enterprise_list_confirmed = []
enterprise_num = httpapi.getNums()
enterprise_paga_num = math.ceil(httpapi.getNums()/page_items_limit)
for page_count in range(1,enterprise_paga_num+1):
#for page_count in range(1,2):
    print('正在收集第%d页'%page_count)
    context = httpapi.getEnterpriseInpages(page_count,page_items_limit)
    [state,enterprise_list_not_confirm_part,enterprise_list_confirmed_part] = process_context.process_enterprise_inPages(context,the_lastone_id)
    enterprise_list_not_confirm.extend(enterprise_list_not_confirm_part)
    enterprise_list_confirmed.extend(enterprise_list_confirmed_part)
    if state == 0:
        break
#print(enterprise_list_not_confirm)
#print(enterprise_list_confirmed)

#if enterprise_list_not_confirm:
    #for items in enterprise_list_not_confirm:
        #print(items['name'])
        #context_one = httpapi.getOneEnterprise(items['id'])
        #enterprise_one_items = process_context.process_enterprise_inDetail(context_one)
        #print(enterprise_one_items)
        


[date_num,class_num,class_list,schedule] = excel.reloadTemplate()
#print('读取到:%d天,%d个教室'% (date_num,class_num))
print(class_list)

print('有'+str(len(enterprise_list_not_confirm))+'项申请待处理:') 
for enterprise in enterprise_list_not_confirm: 
    print(enterprise['name'])   
print('有'+str(len(enterprise_list_confirmed))+'项申请已处理:')
[success_list,fail_list] = mainFuncs.add_schedule(enterprise_list_confirmed,schedule,'all')
'''
#for i in range(30): 
    #enterprise = enterprise_list_confirmed[i]
for enterprise in enterprise_list_confirmed: 
    print(enterprise['name']) 
    [success_list,fail_list] = mainFuncs.add_schedule(enterprise_list_confirmed,schedule,'all')
    for case in success_list:
        print(case['name'])
        print(case['type']) 
        print(case['time'])  
        print(case['place']) 
    for case in fail_list:
        print(case['error_reason'])
        print(case['error_msg']) 
        print(case['error_type'])
 '''   

#print(schedule)

print('插入成功%d条企业申请'%len(success_list))
#print(success_list)
print('插入失败%d条企业申请'%len(fail_list))
'''
for enterprise in success_list:
    print(enterprise['name'])
for enterprise in fail_list:
    print(enterprise['error_msg'])
'''
for fail_case in fail_list:
    if fail_case['error_type'] == 'no_class':
        continue
    print(fail_case['error_reason'])
    print(fail_case['error_msg'])
    print(fail_case['error_type'])


'''
for enterprise in enterprise_list_not_confirm:
    available_class = mainFuncs.search_available(enterprise,schedule,class_list)
    print('')
    print(enterprise['name'])
    for class_type in available_class:
        if available_class[class_type]:
            print('%s:%s'%(class_type,available_class[class_type]))
'''