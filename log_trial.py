import logging
import os
import sys

# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")

str_format = "[%(asctime)s : %(levelname)s : %(module)s : %(message)s]"

log_dir = "log"
log_file_path = os.path.join(log_dir,"logs.log")
os.makedirs(log_dir,exist_ok = True)

logging.basicConfig(level=logging.INFO,
                    format= str_format,
                    handlers=[
                        logging.FileHandler(log_file_path),
                        logging.StreamHandler(sys.stdout)
                    ])

logger = logging.getLogger("proj")