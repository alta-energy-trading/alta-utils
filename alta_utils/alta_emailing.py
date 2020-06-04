import smtplib
import os
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from alta_utils.constants import SENDER_EMAIL_ADDRESS, INFO_EMAIL_ADDRESS, ERROR_EMAIL_ADDRESS


def sendEmail(type, subject, body, table=""):

    message = MIMEMultipart('alternative')    
    message['From'] = SENDER_EMAIL_ADDRESS

    if(type.lower() == 'info'):
        subjectPrefix = ''
        message['To'] = INFO_EMAIL_ADDRESS
    elif(type.lower() == 'error'):
        subjectPrefix = 'Error - '
        message['To'] = ERROR_EMAIL_ADDRESS
    message['Subject'] = '{}{}'.format(subjectPrefix,subject)


    msg = MIMEText(f"<html><body><p>Dear Analyst,</p><p>{body}</p>{table}</body></html>", 'html')
    message.attach(msg)

    

    try:
        smptServer = smtplib.SMTP('slomgmt.arcpet.co.uk')
        smptServer.send_message(message)
        smptServer.quit()
    except Exception as e:
        raise e

    