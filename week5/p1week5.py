'''
Created on Apr 14, 2018

@author: student
'''
import smtplib
from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# msg = MIMEMultipart()
# msg.attach(MIMEText(body, 'plain'))

SMTP_SERVER = "smtp.mail.yahoo.com"
SMTP_PORT = 587
SMTP_USERNAME = "playdoh888@yahoo.com"
SMTP_PASSWORD = "mypassword"
EMAIL_FROM = "playdoh888@yahoo.com"
EMAIL_TO = "jack.wang888@gmail.com"
EMAIL_SUBJECT = "REMINDER: "
co_msg = """
    Hello, Jack! Just wanted to send a friendly appointment
    reminder for your Python class time:
    Avtech
    Where: Fairfield, NJ
    Time: 9:30am
"""
def send_email():
    msg = MIMEText(co_msg)
    msg['Subject'] = EMAIL_SUBJECT + "Avtech - Python class @Fairfield"
    msg['From'] = EMAIL_FROM 
    msg['To'] = EMAIL_TO
    debuglevel = True
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.set_debuglevel(debuglevel)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    mail.quit()

if __name__=='__main__':
    send_email()