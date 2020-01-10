import importlib,sys
importlib.reload(sys)
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 发送邮箱服务器
smtpserver = 'smtp.qq.com'
# 发送邮箱用户/密码
user = '1366039190@qq.com'
password = 'fcazftsnuqelgijg'
# 发送邮箱
sender = '1366039190@qq.com'
# 接收邮箱
receiver = '2016302580182@whu.edu.cn'

# 创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header('Python 测试', 'utf-8')
message['To'] = Header('测试', 'utf-8')
subject = 'Python SMTP邮件测试'
message['Subject'] = Header(subject, 'utf-8')

# 邮件正文内容
message.attach(MIMEText('这是测试Python发送附件功能....', 'plain', 'utf-8'))

# 构造附件1，传送当前目录下的test.txt文件
att1 = MIMEText(open('123.txt', 'rb').read(), 'base64', 'utf-8')
att1['Content-Type'] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字 邮件中就显示什么名字
att1['Content-Disposition'] = 'attachment;filename:"123.txt"'
message.attach(att1)

smtp = smtplib.SMTP()
smtp.connect(smtpserver, 25)
smtp.login(user, password)
smtp.sendmail(sender, receiver, message.as_string())
smtp.quit()