import urllib.request
import json
import time
import re
import math
from bs4 import BeautifulSoup

import httpapi,process_context,excel

the_lastone_id = 134571

page_items_limit = 100
enterprise_list_not_confirm = []
enterprise_list_confirmed = []
enterprise_num = httpapi.getNums()
enterprise_paga_num = math.ceil(httpapi.getNums()/page_items_limit)

for page_count in range(1,enterprise_paga_num+1):
    print('正在收集第%d页'%page_count)
    context = httpapi.getEnterpriseInpages(page_count,page_items_limit)
    [state,enterprise_list_not_confirm_part,enterprise_list_confirmed_part] = process_context.process_enterprise_inPages(context,the_lastone_id)
    enterprise_list_not_confirm.extend(enterprise_list_not_confirm_part)
    enterprise_list_confirmed.extend(enterprise_list_confirmed_part)
    if state == 0:
        break

print(enterprise_list_not_confirm)
print(enterprise_list_confirmed)

if enterprise_list_not_confirm:
    print('有'+str(len(enterprise_list_not_confirm))+'项申请待处理:')
    '''
    for items in enterprise_list_not_confirm:
        print(items['name'])
'''
        #context_one = httpapi.getOneEnterprise(items['id'])
        #enterprise_one_items = process_context.process_enterprise_inDetail(context_one)
        #print(enterprise_one_items)
        
        
print('有'+str(len(enterprise_list_confirmed))+'项申请已处理:')
'''
for items in enterprise_list_confirmed:
    print(items['name'])
'''
    
[date_num,class_num,class_list,schedule] = excel.reloadTemplate()
print('读取到:%d天,%d个教室'% (date_num,class_num))
print(class_list)
