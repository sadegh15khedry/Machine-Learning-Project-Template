import logging
import os
from datetime import datetime

# LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.log"
# logs_path = os.path.join('../', 'logs', LOG_FILE)
# os.mkdir(logs_path)
# Define the directory and log file name
logs_dir = os.path.join('../', 'logs')
log_file_name = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
log_file_path = os.path.join(logs_dir, log_file_name)

# LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Create the logs directory if it does not exist
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

logging.basicConfig(
    filename=log_file_path,
    format= "[%(asctime)s] %(lineno)d -%(levelname)s - %(message)s",
    level=logging.INFO,
)
if __name__ == "__main__":
    logging.info("Logging started.")