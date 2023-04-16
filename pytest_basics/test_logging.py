import logging


def test_logging():
    logger = logging.getLogger(__name__)

    fileLocation = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileLocation.setFormatter(formatter)

    # file handler object
    logger.addHandler(fileLocation)

    # set the level of logs
    logger.setLevel(logging.INFO)

    # hierarchy will be like by default -> debug, info, warning ...etc
    logger.debug("A debug statement is executed")
    logger.info("Information statements")
    logger.warning("warning message")
    logger.error("a major error has happened")
    logger.critical("critical issue")
