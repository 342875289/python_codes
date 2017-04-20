import smtplib
from email.mime.text import MIMEText
from email.header import Header
# 输入Email地址和口令:
from_addr = "mon_dayuan@sina.com"
password = "labcat127"
# 输入收件人地址:
to_addr = "342875289@qq.com"
# 输入SMTP服务器地址:
smtp_server = "smtp.sina.com"
msg = MIMEText('dsadsadas', 'plain', 'utf-8')
msg['To'] = Header("收件人342<342875289@qq.com>",'utf-8')
msg['From'] = Header("Xiao_Ming<mon_dayuan@sina.com>")
msg['Subject'] = Header("放假通知", 'utf-8')
server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,to_addr, msg.as_string())
server.quit()