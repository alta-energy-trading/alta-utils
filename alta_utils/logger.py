import logging
import os
import smtplib
import os
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Logger():
    def __init__(
            self, 
            sender_email='targo.support@arcpet.co.uk',
            info_email='henryt@arcpet.co.uk',
            error_email='henryt@arcpet.co.uk',
            production_db_server='ArcSql',
            internal_domain='Arcpet'
        ):        
        self.sender_email_address = sender_email
        self.info_email_address = info_email
        self.error_email_address = error_email
        self.production_db_server = production_db_server
        self.production_db_server = production_db_server    
        self.internal_domain = internal_domain


    def _send_email(self, type, subject, body, table=""):
        message = MIMEMultipart('alternative')    
        message['From'] = self.sender_email_address

        if(type.lower() == 'info'):
            subjectPrefix = ''
            message['To'] = self.info_email_address
        elif(type.lower() == 'error'):
            subjectPrefix = 'Error - '
            message['To'] = self.error_email_address
        message['Subject'] = '{}{}'.format(subjectPrefix,subject)


        msg = MIMEText(f"<html><body><p>Dear Analyst,</p><p>{body}</p>{table}</body></html>", 'html')
        message.attach(msg)

        try:
            smptServer = smtplib.SMTP('slomgmt.arcpet.co.uk')
            smptServer.send_message(message)
            smptServer.quit()
        except Exception as e:
            raise e


    def info(self, moduleName, functionName, message):
        logMessage = "{:<8}".format("Info") + " | " + moduleName + "." + "{:<50s}".format(functionName) + " | " + message
        print(logMessage)

        logging.info(logMessage)
        return logMessage


    def warning(self, moduleName, functionName, message):
        logMessage = "{:<8}".format("Warning") + " | " + moduleName + "." + "{:<50s}".format(functionName) + " | " + message
        print(logMessage)

        logging.warning(logMessage)
        return logMessage


    def error(self, moduleName, functionName, message):
        logMessage = "{:<8}".format("Error") + " | " + moduleName + "." + "{:<50s}".format(functionName) + " | " + message
        print(logMessage)

        logging.error(logMessage)
        return logMessage


    def send_error_email(self, moduleName, functionName, message):
        logMessage = "{:<8}".format("Error") + " | " + moduleName + "." + "{:<50s}".format(functionName) + " | " + message
        print(logMessage)

        logging.error(logMessage)


        if(self.internal_domain.lower() in os.environ["userdomain"].lower() ):
            email_subject = moduleName + '.' + functionName
            if(os.environ['ADUB_DBServer'].lower() != self.production_db_server.lower()):
                email_subject = 'TEST ' + email_subject
                
            try:
                self._send_email("Error", email_subject, message)
            except Exception as e:
                logMessage = "{:<8}".format('Error') + " | " + 'Log' + "." + "{:<50s}".format('error_email') + " | " + str(e)
                logging.error(logMessage)

        return logMessage

    

    