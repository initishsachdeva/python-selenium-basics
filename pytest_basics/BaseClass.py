import inspect
import logging


class BaseClass:

    def getLogger(self):
        # to get correct file name on log file
        loggerName = inspect.stack()[1][3]
        #        logger = logging.getLogger(__name__)
        logger = logging.getLogger(loggerName)

        fileLocation = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileLocation.setFormatter(formatter)

        # file handler object
        logger.addHandler(fileLocation)

        # set the level of logs
        logger.setLevel(logging.INFO)
        return logger
