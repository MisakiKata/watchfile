import configparser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from lib.emailtemple import templatefile
import os

global templatefile


def sendemail(data, movefile):
    config = configparser.ConfigParser()
    config.read(os.getcwd()+'/config.ini')
    semail = config['EMAIL']

    sender = semail['mail_user']
    receivers = semail['receiver']

    file = templatefile.format(hostname=data['hostname'],time=data['time'],filename=data['filename'],
                                maskname=data['maskname'],filepath=data['filepath'])

    message = MIMEMultipart()
    message['From'] = Header(sender, 'utf-8')
    message['To'] =  Header(receivers, 'utf-8')
    subject = '文件变动通知'
    message['Subject'] = Header(subject, 'utf-8')

    message.attach(MIMEText(file, 'html', 'utf-8'))

    att1 = MIMEText(open(movefile, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="result.csv"'
    message.attach(att1)
    
    
    try:
        if semail['mail_ssl'] == 'False':
            smtpObj = smtplib.SMTP() 
            smtpObj.connect(semail['mail_host'], int(semail['mail_port']))  
            smtpObj.login(semail['mail_user'],semail['mail_pass'])
            smtpObj.sendmail(sender, receivers, message.as_string())
        else:
            server=smtplib.SMTP_SSL(semail['mail_host'], int(semail['mail_port']))
            server.login(semail['mail_user'],semail['mail_pass'])
            server.sendmail(sender, receivers,message.as_string())
            server.quit()
        return True
    except smtplib.SMTPException:

        return False

