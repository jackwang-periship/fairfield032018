'''
Created on Apr 14, 2018

@author: student
'''
import smtplib
from email.mime.text import MIMEText

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

from sys import argv

# from email.mime.multipart import MIMEMultipart
# msg = MIMEMultipart()
# msg.attach(MIMEText(body, 'plain'))

SMTP_SERVER = "smtp.mail.yahoo.com"
SMTP_PORT = 587
SMTP_USERNAME = "fairfield032018@yahoo.com"
SMTP_PASSWORD = "nj.07004"
EMAIL_FROM = "fairfield032018@yahoo.com"
EMAIL_TO = "jack.wang888@gmail.com"
EMAIL_SUBJECT = "REMINDER: "
co_msg = """
    Hello, Jack! Just wanted to send a friendly appointment
    reminder for your Python class time:
    Avtech
    Where: Fairfield, NJ
    Time: 9:30am
"""
def send_email(server, port, username, password, email_from, email_to, email_subject, email_body):
    try:
        msg = MIMEText(email_body)
        msg['Subject'] = email_subject + "Avtech - Python class @Fairfield"
        msg['From'] = email_from 
        msg['To'] = email_to
        debuglevel = True
        mail = smtplib.SMTP(server, port)
        mail.set_debuglevel(debuglevel)
        #Calling starttls() to place the SMTP connection in TLS (Transport Layer Security) mode. 
        mail.starttls()
        mail.login(username, password)
        mail.sendmail(email_from, email_to, msg.as_string())
    except smtplib.SMTPException as err:
        print "SMTP Error: %s" % err.smtp_error
    
    mail.quit()
    
def send_email_with_attachment(server, port, username, password, email_from, email_to, email_subject, email_body, attached_filed_name):
    try:
        msg = MIMEMultipart()
        msg['Subject'] = email_subject + "Avtech - Python class @Fairfield"
        msg['From'] = email_from 
        msg['To'] = email_to

        msg.attach(MIMEText(email_body, 'plain'))

        #Attache the file content as the second part of the email.
        attachment = open(attached_filed_name, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        #IMPORTANT: convert the file into a Base64 before sending it
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % attached_filed_name)
        msg.attach(part)

        mail = smtplib.SMTP(server, port)

        debuglevel = True
        mail.set_debuglevel(debuglevel)

        #Calling starttls() to place the SMTP connection in miTLS (Transport Layer Security) mode. 
        mail.starttls()
        mail.login(username, password)
        text = msg.as_string()
        mail.sendmail(email_from, email_to, text)
    except smtplib.SMTPException as err:
        print "SMTP Error: %s" % err.smtp_error
    except IOError as err:
        print "The file open error: %s" % err.smtp_error
    
    mail.quit()
    


if __name__=='__main__':
    
    # Get the total number of args passed to the demo.py
    total = len(argv)

    if total != 2:
        send_email(SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD,
            EMAIL_FROM, EMAIL_TO, EMAIL_SUBJECT, co_msg)
    else:
        # Get the arguments list 
        cmdargs = str(argv)
        filename = argv[1]
        co_msg = """
            Hello, Jack! Please see the meeting invitation attached to this email.
            Where: Fairfield, NJ
            Time: 9:30am
        """
        send_email_with_attachment(SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD,
               EMAIL_FROM, EMAIL_TO, EMAIL_SUBJECT, co_msg, filename)
    print "Email sent, Bye!"
    exit(0)
    