import json
import time
import re

from bs4 import BeautifulSoup

year_now = time.localtime().tm_year
month_now = time.localtime().tm_mon

def splitDateTime(datetime):
    global year_now,month_now
    if datetime:
        month_enterprise = int(datetime[0:2])
        if month_now < 9:
            if month_enterprise >= 9:
                year_enterprise = year_now - 1
            else:
                year_enterprise = year_now
        else:
            if month_enterprise < 9:
                year_enterprise = year_now + 1
            else:
                year_enterprise = year_now
        date = str(year_enterprise) + '-' +  datetime[0:5]
        time = datetime[6:18]
    else:
        date = ''
        time = ''
    return [date,time]

def process_enterprise_inPages(context,the_lastone_id = 0):
    
    enterprise_list_not_confirm =[]
    enterprise_list_confirmed =[]
    enterprise_items = {}
    p_enterprise_num = re.compile(r'<span>条\D+(\d+)+\D+(\d+)页</span>')
    p_enterprise_id = re.compile(r'/teachin/view/id/(\d+)')
    p_place = re.compile(r'(\d?\w\d{3})')
    nums = p_enterprise_num.search(context)
    enterprise_num = nums.group(1)
    enterprise_page_num = nums.group(2)
    soup = BeautifulSoup(context,'html.parser')
    trs = soup.find_all('tr',attrs={"target": "xid"})
    for tr in trs:
        tds = tr.find_all('td')
        if the_lastone_id and p_enterprise_id.search(tds[1].a['href']).group(1) == str(the_lastone_id):
            return [0,enterprise_list_not_confirm,enterprise_list_confirmed]
        department = tds[12].get_text().strip()
        if department != '江南大学就业创业指导服务中心':
            continue
        enterprise_items = {}
        enterprise_items['name']                = tds[1].get_text().strip()
        enterprise_items['id']                  = p_enterprise_id.search(tds[1].a['href']).group(1)
        enterprise_items['person']              = tds[2].get_text().strip()
        enterprise_items['phone']               = tds[3].get_text().strip()
        [enterprise_items['date_display'] ,enterprise_items['time_display'] ]       = splitDateTime(tds[4].get_text().strip())
        enterprise_items['place_display']       = p_place.findall(tds[5].get_text())
        [enterprise_items['date_writtenTest'] ,enterprise_items['time_writtenTest'] ]       = splitDateTime(tds[6].get_text().strip())
        enterprise_items['place_writtenTest']   = p_place.findall(tds[7].get_text())
        [enterprise_items['date_faceTest'] ,enterprise_items['time_faceTest'] ]       = splitDateTime(tds[8].get_text().strip())
        enterprise_items['place_faceTest']      = p_place.findall(tds[9].get_text())
        enterprise_items['department']          = department
        enterprise_items['state_comfirm']       = tds[13].get_text().strip()
        if enterprise_items['place_display'] == '未分配':
            enterprise_items['place_display'] = ''
        if enterprise_items['state_comfirm'] == '待审核':
            enterprise_list_not_confirm.append(enterprise_items)
        else:
            enterprise_list_confirmed.append(enterprise_items)
    return [1,enterprise_list_not_confirm,enterprise_list_confirmed]

def process_enterprise_inDetail(context):   
    enterprise_one_items ={}
    one = BeautifulSoup(context,'html.parser')
    divs = one.find_all('div',attrs={"class": "row"})[-19:]
    enterprise_one_items['teachin_site_require']    = divs[0].find('option',attrs={"selected": "selected"}).get_text().strip()
    if divs[3].find('input',attrs={"id": "bsite","checked": "checked"}):
        enterprise_one_items['b_site_require']  = divs[6].find('option',attrs={"selected": "selected"}).get_text().strip()
        b_site_num = divs[7].find('input',attrs={"id": "TeachinAdvance_b_site_num","value": True})
        if b_site_num:
            enterprise_one_items['b_site_num']  =  b_site_num['value']
        else:
            enterprise_one_items['b_site_num']  =  1
        enterprise_one_items['b_other_require'] = divs[8].find('input',attrs={"id": "TeachinAdvance_b_other_require"})['value']
    else:
        enterprise_one_items['b_site_num']  =  0
    
    if divs[11].find('input',attrs={"id": "msite","checked": "checked"}):
        enterprise_one_items['m_site_require']  = divs[14].find('option',attrs={"selected": "selected"}).get_text().strip()
        m_site_num = divs[15].find('input',attrs={"id": "TeachinAdvance_m_site_num","value": True})
        if m_site_num:
            enterprise_one_items['m_site_num']  =  m_site_num['value']
        else:
            enterprise_one_items['m_site_num']  =  1
        enterprise_one_items['m_other_require']               = divs[16].find('input',attrs={"id": "TeachinAdvance_m_other_require"})['value']
    else:
        enterprise_one_items['m_site_num']  =  0
    return enterprise_one_items