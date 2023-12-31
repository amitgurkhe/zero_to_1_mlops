from log_trial import logger

try:
    1/0
except ZeroDivisionError as e:
    logger.info(e)

logger.info("completed division")