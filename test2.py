# -*- coding: utf-8 -*-
from email.header import Header
from email.mime.text import MIMEText
import time

import xlrd
from datetime import date,datetime
#导入smtplib邮件发送模块
import smtplib


#获取邮箱信息
ExceFileUrl = xlrd.open_workbook(r'C:\Users\yoyo\Desktop\test.xlsx')
sheet_date = ExceFileUrl.sheet_by_index(0)
#print(sheet_date.name,sheet_date.nrows,sheet_date.ncols)
email_data1 = sheet_date.col_values(0)
email_data2 = sheet_date.col_values(1)
#print(email_data1)
#print(email_data2)

def sender_mail():
    #创建对象
    smt_p = smtplib.SMTP()
    #设置smtp服务器
    smt_p.connect(host='smtp.qq.com', port=25)
    #进行邮箱登录一次
    smt_p.login(user='1366039190@qq.com', password='fcazftsnuqelgijg')
    count_num = 1
    #使用for循环来进行发邮件
    for (i,j) in zip(email_data1,email_data2):
        print(i)
        print(j)
        send_msg = MIMEText(i+'您好,这是一封测试邮件','plain', 'utf-8')
        send_msg['From'] = 'zh'
        send_msg['To'] = j
        send_msg['subject'] = 'python测试'
        smt_p.sendmail('1366039190@qq.com',j,send_msg.as_string())
        #sleep5秒是因为发送频率过快，判定垃圾邮件的几率大大增加了。
        time.sleep(5)
        print('第%d次发送给%s' % (count_num,i))
        count_num = count_num + 1

    smt_p.quit()
sender_mail()