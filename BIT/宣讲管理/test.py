import urllib.request
import json
import time
import re
import math
import traceback

from bs4 import BeautifulSoup

import httpapi,process_context,excel

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

if enterprise_list_not_confirm:
    print('有'+str(len(enterprise_list_not_confirm))+'项申请待处理:')

    #for items in enterprise_list_not_confirm:
        #print(items['name'])

        #context_one = httpapi.getOneEnterprise(items['id'])
        #enterprise_one_items = process_context.process_enterprise_inDetail(context_one)
        #print(enterprise_one_items)
        
        
print('有'+str(len(enterprise_list_confirmed))+'项申请已处理:')

#for items in enterprise_list_confirmed:
    #print(items['name'])


[date_num,class_num,class_list,schedule] = excel.reloadTemplate()
#print('读取到:%d天,%d个教室'% (date_num,class_num))
print(class_list)
p_split_time = re.compile(r'(\d+):(\d+)-(\d+):(\d+)')
for enterprise_new in enterprise_list_confirmed:
    #print(enterprise_new['name'])
    #宣讲
    if enterprise_new['date_display']:
        try:
            time = p_split_time.search(enterprise_new['time_display'])
            if int(time.group(1)) <= 17:
                time_part = 'Afternoon'
            else:
                time_part = 'Night'
            for place in enterprise_new['place_display']:
                #print(enterprise_new['date_display'])
                #print(place_display)
                if place[0] == 'F':
                    time_part = 'Allday'
                schedule_one = schedule[str(enterprise_new['date_display'])][time_part][place]
                if schedule_one['isavailable'] :
                    new_start = int(time.group(1))*100 + int(time.group(2))
                    new_end = int(time.group(3))*100 + int(time.group(4))
                    conflict = 0
                    for enterprise_exist in schedule_one['enterprise_list']:
                        exist_time = p_split_time.search(enterprise_exist['time_display'])
                        exist_start = int(exist_time.group(1))*100 + int(exist_time.group(2))
                        exist_end = int(exist_time.group(3))*100 + int(exist_time.group(4))
                        if not (((new_start <= exist_start) and (new_start <= exist_end)) or ((new_end >= exist_start) and (new_end >= exist_end))):
                            conflict = 1
                    if conflict:
                        print(enterprise_new)
                        print('时间段冲突')
                    else:
                        schedule_one['enterprise_list'].append([enterprise_new['name'],enterprise_new['date_display'],enterprise_new['time_display'],enterprise_new['place_display']])
                        #print("加入成功")
                else:
                    print(enterprise_new)
                    print('时间段错误')
                    continue
        except  KeyError as msg:#KeyError
            print('d错误信息:'+repr(msg))
            print(enterprise_new)
        except  BaseException as msg:#KeyError
            print('d错误信息:')
            print(enterprise_new)
            traceback.print_exc()
            continue
                    
    #笔试
    if enterprise_new['date_writtenTest']:
        try:
            time = p_split_time.search(enterprise_new['time_writtenTest'])
            if int(time.group(1)) <= 17:
                time_part = 'Afternoon'
            else:
                time_part = 'Night'
            for place in enterprise_new['place_writtenTest']:
                #print(enterprise_new['date_display'])
                #print(place_display)
                if place[0] == 'F':
                    time_part = 'Allday'
                schedule_one = schedule[str(enterprise_new['date_writtenTest'])][time_part][place]
                if schedule_one['isavailable'] :
                    new_start = int(time.group(1))*100 + int(time.group(2))
                    new_end = int(time.group(3))*100 + int(time.group(4))
                    conflict = 0
                    for enterprise_exist in schedule_one['enterprise_list']:
                        print(enterprise_exist)
                        exist_time = p_split_time.search(enterprise_exist['time_writtenTest'])
                        exist_start = int(exist_time.group(1))*100 + int(exist_time.group(2))
                        exist_end = int(exist_time.group(3))*100 + int(exist_time.group(4))
                        if not (((new_start <= exist_start) and (new_start <= exist_end)) or ((new_end >= exist_start) and (new_end >= exist_end))):
                            conflict = 1
                    if conflict:
                        print(enterprise_new)
                        print('时间段冲突')
                    else:
                        schedule_one['enterprise_list'].append([enterprise_new['name'],enterprise_new['date_writtenTest'],enterprise_new['time_writtenTest'],enterprise_new['place_writtenTest']])
                        #print("加入成功")
                else:
                    print(enterprise_new)
                    print('时间段错误')
                    continue
        except  KeyError as msg:#KeyErro
            print('b错误信息:'+repr(msg))
            print(enterprise_new)
        except  BaseException as enterprise_exist:#KeyError
            print('b错误信息:')
            print(enterprise_new)
            print(enterprise_exist)
            traceback.print_exc()
            continue
    #面试
    if enterprise_new['date_faceTest']:
        try:
            time = p_split_time.search(enterprise_new['time_faceTest'])
            if int(time.group(1)) <= 17:
                time_part = 'Afternoon'
            else:
                time_part = 'Night'
            for place in enterprise_new['place_faceTest']:
                #print(enterprise_new['date_display'])
                #print(place_display)
                if place[0] == 'F':
                    time_part = 'Allday'
                schedule_one = schedule[str(enterprise_new['date_faceTest'])][time_part][place]
                if schedule_one['isavailable'] :
                    new_start = int(time.group(1))*100 + int(time.group(2))
                    new_end = int(time.group(3))*100 + int(time.group(4))
                    conflict = 0
                    for enterprise_exist in schedule_one['enterprise_list']:
                        exist_time = p_split_time.search(enterprise_exist['time_faceTest'])
                        exist_start = int(exist_time.group(1))*100 + int(exist_time.group(2))
                        exist_end = int(exist_time.group(3))*100 + int(exist_time.group(4))
                        if not (((new_start <= exist_start) and (new_start <= exist_end)) or ((new_end >= exist_start) and (new_end >= exist_end))):
                            conflict = 1
                    if conflict:
                        print(enterprise_new)
                        print('时间段冲突')
                    else:
                        schedule_one['enterprise_list'].append([enterprise_new['name'],enterprise_new['date'],enterprise_new['time_writtenTest'],enterprise_new['place_writtenTest']])
                        #print("加入成功")
                else:
                    print(enterprise_new)
                    print('时间段错误')
                    continue
        except  KeyError as msg:#KeyError
            print('f错误信息:'+repr(msg))
            print(enterprise_new)
        except  BaseException as msg:#KeyError
            print('f错误信息:')
            print(enterprise_new)
            traceback.print_exc()
            continue
#print(schedule)




