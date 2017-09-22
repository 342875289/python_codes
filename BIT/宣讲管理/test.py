import urllib.request
import json
import time
import re
import math
from bs4 import BeautifulSoup

import httpapi,process_context

the_lastone_id = 134571

page_number = 1
page_items_limit = 100
enterprise_num = httpapi.getNums()
enterprise_paga_num = math.ceil(httpapi.getNums()/page_items_limit)

for page_count in range(1,enterprise_paga_num+1):
    print(page_count)
    context = httpapi.getEnterpriseInpages(page_count,page_items_limit)
    [state,enterprise_list_not_confirm,enterprise_list_confirmed] = process_context.process_enterprise_inPages(context,the_lastone_id)
    
    if enterprise_list_not_confirm:
        print('有'+str(len(enterprise_list_not_confirm))+'项申请待处理:')
        for items in enterprise_list_not_confirm:
            print(items['name'])
            '''
            #context_one = httpapi.getOneEnterprise(items['id'])
            #enterprise_one_items = process_context.process_enterprise_inDetail(context_one)
            #print(enterprise_one_items)
            '''
    print('有'+str(len(enterprise_list_confirmed))+'项申请已处理:')
    for items in enterprise_list_confirmed:
        print(items['name'])
    if state == 0:
        break