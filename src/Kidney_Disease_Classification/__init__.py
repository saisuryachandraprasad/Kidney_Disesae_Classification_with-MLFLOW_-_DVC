import os
import sys
import logging



log_str = "[%(asctime)s  - %(levelname)s - %(module)s - %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir, "running logs.log")

os.makedirs(log_dir, exist_ok= True)


logging.basicConfig(
    level= logging.INFO,
    format= log_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("Kidney_Disease_Classification")