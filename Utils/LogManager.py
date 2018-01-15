import logging
import datetime
from Setting import DefineManager

def PrintLogMessage(fileName = "Logger", methodName = "PrintLogMessage", message = "Wrong log level accepted.", logLevel = DefineManager.LOG_LEVEL_ERROR):
    logger = logging.getLogger()

    nowDateInfo = datetime.datetime.now()
    try:
        loggingTime = nowDateInfo.strftime('%H:%M:%S')
    except:
        loggingTime = "??:??:??"

    logMessage = " " + loggingTime + " [" + fileName + "] <" + methodName + "> (" + message + ")"
    if logLevel == DefineManager.LOG_LEVEL_INFO:
        logger.setLevel(logging.INFO)
        logging.info(logMessage)
    elif logLevel == DefineManager.LOG_LEVEL_DEBUG:
        logger.setLevel(logging.DEBUG)
        logging.debug(logMessage)
    elif logLevel == DefineManager.LOG_LEVEL_WARN:
        logger.setLevel(logging.WARN)
        logging.warning(logMessage)
    elif logLevel == DefineManager.LOG_LEVEL_ERROR:
        logger.setLevel(logging.ERROR)
        logging.error(logMessage)
    else:
        logger.setLevel(logging.ERROR)
    return