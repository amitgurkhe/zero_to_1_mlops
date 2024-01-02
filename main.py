from log_trial import logger
import mlflow
import pandas
import numpy
try:
    1/0
except ZeroDivisionError as e:
    logger.info(e)

logger.info("completed division")