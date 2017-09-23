import time

year_now = time.localtime().tm_year
month_now = time.localtime().tm_mon

datetime = '09-25 08:00-12:00'.strip()
#global year_now,month_now
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

print(date)

print(time)