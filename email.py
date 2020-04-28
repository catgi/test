# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.header import Header
 

if __name__ == '__main__':
    server = "smtp.163.com"                 #服务器
    mail_user = "zhongjd_test@163.com"      #用户名
    mail_pwd = "JKOKPRSNCQRJGSDT"           #授权码
    
    
    #构造邮件对象
    msg = MIMEMultipart()
    
    #邮件头部
    subject = '结果'
    sender = 'zhongjd_test@163.com'         #发件人
    receivers = '419137107@qq.com'
    #receivers = 'markma@SeasDa.com'          #收件人
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = Header(sender)
    msg['To'] =  Header(receivers)
    
    #邮件正文
    content = '截图1、2、3的结果'
    msg.attach(MIMEText(content, 'plain', 'utf-8'))
    
    #邮件附件
    file_path = '1.txt'
    with open(file_path,'rb') as f:
        attachFile = MIMEApplication(f.read())
        attachFile.add_header('Content-Disposition','attachment',filename = '1.txt')
    msg.attach(attachFile)
    
    file_path = '2.txt'
    with open(file_path,'rb') as f:
        attachFile = MIMEApplication(f.read())
        attachFile.add_header('Content-Disposition','attachment',filename = '2.txt')
    msg.attach(attachFile)
    
    file_path = '3.txt'
    with open(file_path,'rb') as f:
        attachFile = MIMEApplication(f.read())
        attachFile.add_header('Content-Disposition','attachment',filename = '3.txt')
    msg.attach(attachFile)
        
    #发送邮件
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(server,25)
        smtpObj.login(mail_user,mail_pwd) 
        smtpObj.sendmail(sender, receivers, msg.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print("邮件发送失败")
        print(e)
    