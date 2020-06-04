import logging
import os

from alta_utils.constants import INTERNAL_DOMAIN, PRODUCTION_DB_SERVER
import alta_utils.alta_emailing


def info(moduleName, functionName, message):
    logMessage = "{:<8}".format("Info") + " | " + moduleName + "." + "{:<50s}".format(functionName) + " | " + message
    print(logMessage)

    logging.info(logMessage)
    return logMessage


def warning(moduleName, functionName, message):
    logMessage = "{:<8}".format("Warning") + " | " + moduleName + "." + "{:<50s}".format(functionName) + " | " + message
    print(logMessage)

    logging.warning(logMessage)
    return logMessage


def error(moduleName, functionName, message):
    logMessage = "{:<8}".format("Error") + " | " + moduleName + "." + "{:<50s}".format(functionName) + " | " + message
    print(logMessage)

    logging.error(logMessage)
    return logMessage


def error_email(moduleName, functionName, message):
    logMessage = "{:<8}".format("Error") + " | " + moduleName + "." + "{:<50s}".format(functionName) + " | " + message
    print(logMessage)

    logging.error(logMessage)

    if(INTERNAL_DOMAIN.lower() in os.environ["userdomain"].lower() ):
        if(os.environ['ADUB_DBServer'].lower() != PRODUCTION_DB_SERVER.lower()):
            emailSubject = 'TEST ' + emailSubject
            
        try:
            alta_emailing.sendEmail("Error", moduleName + '.' + functionName, message)
        except Exception as e:
            logMessage = "{:<8}".format('Error') + " | " + 'Log' + "." + "{:<50s}".format('error_email') + " | " + str(e)
            logging.error(logMessage)

    return logMessage

    

    