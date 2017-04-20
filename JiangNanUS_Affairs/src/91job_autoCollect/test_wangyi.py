import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email import encoders
from email.utils import parseaddr, formataddr

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 输入Email地址和口令:
from_addr = "mon_dayuan@163.com"
password = "monlovingdayuan0"
# 输入收件人地址:
to_addr = "342875289@qq.com"
# 输入SMTP服务器地址:
smtp_server = "smtp.163.com"

msg = MIMEText('dsadsadas', 'plain', 'utf-8')
#msg['From'] = Header('mon_dayuan@126.com','utf-8')
#msg['From'] = Header("发件人123<mon_dayuan@sina.com>",'utf-8')
msg['To'] = Header("收件人342<342875289@qq.com>",'utf-8')
#msg['From'] = Header("发件人123<mon_dayuan@sina.com>",'utf-8')
msg['Subject'] = Header("放假通缉", 'utf-8')

msg['From'] = _format_addr('Python爱好者 <%s>' %from_addr)
msg['To'] = _format_addr('管理员 <%s>' %to_addr)
msg['Subject'] = Header('来自SMTP的问候……','utf-8').encode()

server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,to_addr, msg.as_string())
server.quit()