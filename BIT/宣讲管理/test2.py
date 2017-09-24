import re
time = '17:00-17:30'
p_time = re.compile(r'(\d+):(\d+)-(\d+):(\d+)')
t = p_time.search(time)
print(t.group(1))
print(t.group(2))
print(t.group(3))
print(t.group(4))