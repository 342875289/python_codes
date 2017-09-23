import re
p_enterprise_num = re.compile(r'(\d?\w\d{3})')
nums = p_enterprise_num.findall('第二教学楼2D304/2D305')
print(nums)
print(p_enterprise_num.findall('北区活动中心F103、F105'))