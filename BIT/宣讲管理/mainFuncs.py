import time
import re
import math
import traceback
def search_available(enterprise,schedule,class_list):
    available_class = {}
    p_split_time = re.compile(r'(\d+)[:：](\d+)-(\d+)[:：](\d+)')#用于提取时间段
    for query_type in ['display','writtenTest','faceTest']:
        success_list = []
        available_class[query_type] = {}
        #根据宣讲/笔试/面试类型做处理
        if query_type == 'display':
            enterprise_date = enterprise['date_display']
            enterprise_time = enterprise['time_display']
            enterprise_place = enterprise['place_display']
            error_header = '宣讲教室查询时发生错误:'
        elif query_type == 'writtenTest':
            enterprise_date = enterprise['date_writtenTest']
            enterprise_time = enterprise['time_writtenTest']
            enterprise_place = enterprise['place_writtenTest']
            error_header = '笔试教室查询时发生错误:'
        elif query_type == 'faceTest':
            enterprise_date = enterprise['date_faceTest']
            enterprise_time = enterprise['time_faceTest']
            enterprise_place = enterprise['place_faceTest']
            error_header = '面试教室查询时发生错误:'
        #对于一个企业的一种情况作处理,以日期是否填写作为是否处理的依据
        if enterprise_date:
            time = p_split_time.search(enterprise_time)
            if int(time.group(1)) <= 12:#需要上午能用的教室
                time_part_list = ['Allday']
            elif int(time.group(1)) <= 17:#根据时间划分下午和晚上
                time_part_list = ['Allday','Afternoon']
            else:
                time_part_list = ['Allday','Night']
            for time_part in  time_part_list:
                schedule_one_time_part = schedule[str(enterprise_date)][time_part]
                for place in schedule_one_time_part:#对每一个分配的教室做处理
                    schedule_one = schedule_one_time_part[place]
                    if schedule_one['isavailable'] :
                        new_start = int(time.group(1))*100 + int(time.group(2))
                        new_end = int(time.group(3))*100 + int(time.group(4))
                        conflict = 0
                        for enterprise_exist in schedule_one['enterprise_list']:
                            exist_time = p_split_time.search(enterprise_exist['time'])
                            exist_start = int(exist_time.group(1))*100 + int(exist_time.group(2))
                            exist_end = int(exist_time.group(3))*100 + int(exist_time.group(4))
                            if not ((new_start >= exist_end)  or ((new_end <= exist_start) )):
                                conflict = conflict + 1
                                break
                        if not conflict:
                            success_list.append(place)
                            #schedule_one['enterprise_list'].append(one_case)
                            #print("加入成功")
                    #else:#所选教室在该时间段不可用
                        #fail_case = {}
            available_class[query_type] =  success_list        
    return available_class     

def conflict_test_schedule(enterprise_list,schedule,query_types):
    success_list = []
    fail_list = []
    p_split_time = re.compile(r'(\d+)[:：](\d+)-(\d+)[:：](\d+)')#用于提取时间段
    if type(enterprise_list)!= list:#针对输入单个企业的情况作处理
        enterprise_list = [enterprise_list]
    for enterprise in enterprise_list:#遍历企业名单,逐个处理
        if query_types == 'all':#查询全部的教室安排
            query_type_list = ['display','writtenTest','faceTest']
        else:
            query_type_list = [query_type]
        for query_type in query_type_list:
            #根据宣讲/笔试/面试类型做处理
            if query_type == 'display':
                enterprise_date = enterprise['date_display']
                enterprise_time = enterprise['time_display']
                enterprise_place = enterprise['place_display']
                error_header = '宣讲教室查询时发生错误:'
            elif query_type == 'writtenTest':
                enterprise_date = enterprise['date_writtenTest']
                enterprise_time = enterprise['time_writtenTest']
                enterprise_place = enterprise['place_writtenTest']
                error_header = '笔试教室查询时发生错误:'
            elif query_type == 'faceTest':
                enterprise_date = enterprise['date_faceTest']
                enterprise_time = enterprise['time_faceTest']
                enterprise_place = enterprise['place_faceTest']
                error_header = '面试教室查询时发生错误:'
            #对于一个企业的一种情况作处理,以日期是否填写作为是否处理的依据
            if enterprise_date:
                try:
                    time = p_split_time.search(enterprise_time)
                    if int(time.group(1)) <= 17:#根据时间划分下午和晚上
                        time_part = 'Afternoon'
                    else:
                        time_part = 'Night'
                    for place in enterprise_place:#对每一个分配的教室做处理
                        if place[0] == 'F':#北活教室全天可用
                            time_part = 'Allday'
                        schedule_one = schedule[str(enterprise_date)][time_part][place]
                        if schedule_one['isavailable'] :
                            new_start = int(time.group(1))*100 + int(time.group(2))
                            new_end = int(time.group(3))*100 + int(time.group(4))
                            conflict = 0
                            for enterprise_exist in schedule_one['enterprise_list']:
                                exist_time = p_split_time.search(enterprise_exist['time'])
                                exist_start = int(exist_time.group(1))*100 + int(exist_time.group(2))
                                exist_end = int(exist_time.group(3))*100 + int(exist_time.group(4))
                                if not ((new_start >= exist_end)  or ((new_end <= exist_start) )):
                                    conflict = conflict + 1
                                    break
                            if conflict:
                                fail_case = {}
                                fail_case['error_reason'] = error_header+'所分配%d间教室的时间段冲突(已被其他企业占用)'%conflict
                                fail_case['error_msg'] = 'name:%s,date:%s,class:%s,time:%s'% (enterprise['name'],enterprise_date,enterprise_place,enterprise_time)
                                fail_case['error_type'] = 'class_time_conflict'
                                fail_list.append(fail_case)
                            else:
                                success_case = {}
                                success_case['id'] = enterprise['id']
                                success_case['name'] = enterprise['name']
                                success_case['time'] = enterprise_time
                                success_case['place'] = enterprise_place
                                success_case['type'] = query_type
                                success_list.append(success_case)
                                #schedule_one['enterprise_list'].append(one_case)
                                #print("加入成功")
                        else:#所选教室在该时间段不可用
                            fail_case = {}
                            fail_case['error_reason'] = error_header+'所选教室在该时间段不可用(被涂黑)'
                            fail_case['error_msg'] = 'name:%s,date:%s,class:%s,time:%s'% (enterprise['name'],enterprise_date,enterprise_place,enterprise_time)
                            fail_case['error_type'] = 'class_inavailable'
                            fail_list.append(fail_case)
                except  KeyError as msg:#KeyError
                    fail_case = {}
                    fail_case['error_reason'] = error_header+'已分配的教室不在可用教室表中'
                    fail_case['error_msg'] = 'name:%s,date:%s,class:%s,time:%s'% (enterprise['name'],enterprise_date,str(msg),enterprise_time )
                    fail_case['error_type'] = 'no_class'
                    fail_list.append(fail_case)
                except  AttributeError as msg:#KeyError
                    fail_case = {}
                    if not enterprise_time:
                        fail_case['error_reason'] = error_header+'详细时间未填写'
                    elif not enterprise_place:
                        fail_case['error_reason'] = error_header+'教室未分配'
                    else:
                        fail_case['error_reason'] = error_header+'有信息未填写'
                    fail_case['error_msg'] = 'name:%s,date:%s,class:%s,time:%s'% (enterprise['name'],enterprise_date,enterprise_place,enterprise_time )
                    fail_case['error_type'] = 'empty_info'
                    fail_list.append(fail_case)
                except  BaseException as msg:#KeyError
                    fail_case = {}
                    fail_case['error_reason'] = error_header+'发生严重错误'
                    fail_case['error_msg'] = 'name:%s,date:%s,class:%s,time:%s,error:%s'% (enterprise['name'],enterprise_date,enterprise_place,enterprise_time,str(msg))
                    fail_case['error_type'] = 'undef_fault'
                    fail_list.append(fail_case)
                        
    return [success_list,fail_list]                


def add_schedule(enterprise_list,schedule,query_types):
    success_list = []
    fail_list = []
    p_split_time = re.compile(r'(\d+)[:：](\d+)-(\d+)[:：](\d+)')#用于提取时间段
    if type(enterprise_list)!= list:#针对输入单个企业的情况作处理
        enterprise_list = [enterprise_list]
    for enterprise in enterprise_list:#遍历企业名单,逐个处理
        if query_types == 'all':#查询全部的教室安排
            query_type_list = ['display','writtenTest','faceTest']
        else:
            query_type_list = [query_types]
        for query_type in query_type_list:
            #根据宣讲/笔试/面试类型做处理
            if query_type == 'display':
                enterprise_date = enterprise['date_display']
                enterprise_time = enterprise['time_display']
                enterprise_place = enterprise['place_display']
                error_header = '宣讲教室分配时发生错误:'
            elif query_type == 'writtenTest':
                enterprise_date = enterprise['date_writtenTest']
                enterprise_time = enterprise['time_writtenTest']
                enterprise_place = enterprise['place_writtenTest']
                error_header = '笔试教室分配时发生错误:'
            elif query_type == 'faceTest':
                enterprise_date = enterprise['date_faceTest']
                enterprise_time = enterprise['time_faceTest']
                enterprise_place = enterprise['place_faceTest']
                error_header = '面试教室分配时发生错误:'
            #对于一个企业的一种情况作处理,以日期是否填写作为是否处理的依据
            if enterprise_date:
                try:
                    time = p_split_time.search(enterprise_time)
                    if int(time.group(1)) <= 17:#根据时间划分下午和晚上
                        time_part = 'Afternoon'
                    else:
                        time_part = 'Night'
                    for place in enterprise_place:#对每一个分配的教室做处理
                        if place[0] == 'F':#北活教室全天可用
                            time_part = 'Allday'
                        schedule_one = schedule[str(enterprise_date)][time_part][place]
                        if schedule_one['isavailable'] :
                            new_start = int(time.group(1))*100 + int(time.group(2))
                            new_end = int(time.group(3))*100 + int(time.group(4))
                            conflict = 0
                            for enterprise_exist in schedule_one['enterprise_list']:
                                exist_time = p_split_time.search(enterprise_exist['time'])
                                exist_start = int(exist_time.group(1))*100 + int(exist_time.group(2))
                                exist_end = int(exist_time.group(3))*100 + int(exist_time.group(4))
                                if not ((new_start >= exist_end)  or ((new_end <= exist_start) )):
                                    conflict = conflict + 1
                                    break
                            if conflict:
                                fail_case = {}
                                fail_case['error_reason'] = error_header+'所分配%d间教室的时间段冲突(已被其他企业占用)'%conflict
                                fail_case['error_msg'] = 'name:%s,date:%s,class:%s,time:%s'% (enterprise['name'],enterprise_date,place,enterprise_time)
                                fail_case['error_type'] = 'class_time_conflict'
                                fail_list.append(fail_case)
                            else: 
                                success_case={}
                                success_case['id'] = enterprise['id']
                                success_case['name'] = enterprise['name']
                                success_case['time'] = enterprise_time
                                success_case['place'] = enterprise_place
                                success_case['type'] = query_type
                                success_list.append(success_case)
                                schedule_one['enterprise_list'].append(success_case)
                                #print("加入成功")
                        else:#所选教室在该时间段不可用
                            fail_case = {}
                            fail_case['error_reason'] = error_header+'所选教室在该时间段不可用(被涂黑)'
                            fail_case['error_msg'] = 'name:%s,date:%s,class:%s,time:%s'% (enterprise['name'],enterprise_date,place,enterprise_time)
                            fail_case['error_type'] = 'class_inavailable'
                            fail_list.append(fail_case)
                except  KeyError as msg:#KeyError
                    fail_case = {}
                    fail_case['error_reason'] = error_header+'已分配的教室不在可用教室表中'
                    fail_case['error_msg'] = 'name:%s,date:%s,class:%s,time:%s'% (enterprise['name'],enterprise_date,str(msg),enterprise_time )
                    fail_case['error_type'] = 'no_class'
                    fail_list.append(fail_case)
                except  AttributeError as msg:#KeyError
                    fail_case = {}
                    if not enterprise_time:
                        fail_case['error_reason'] = error_header+'时间未填写'
                    elif not enterprise_place:
                        fail_case['error_reason'] = error_header+'教室未分配'
                    else:
                        fail_case['error_reason'] = error_header+'有信息未填写'
                    fail_case['error_msg'] = 'name:%s,date:%s,class:%s,time:%s'% (enterprise['name'],enterprise_date,enterprise_place,enterprise_time )
                    fail_case['error_type'] = 'empty_info'
                    fail_list.append(fail_case)
                    #print([enterprise_date,enterprise_time])
                    #traceback.print_exc()
                except  BaseException as msg:#KeyError
                    fail_case = {}
                    fail_case['error_reason'] = error_header+'发生严重错误'
                    fail_case['error_msg'] = 'name:%s,date:%s,class:%s,time:%s,error:%s'% (enterprise['name'],enterprise_date,enterprise_place,enterprise_time,str(msg))
                    fail_case['error_type'] = 'undef_fault'
                    fail_list.append(fail_case)
    return [success_list,fail_list]                







