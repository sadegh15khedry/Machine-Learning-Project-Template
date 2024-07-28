import logging
import os
from datetime import datetime


logs_dir = os.path.join('../', 'logs')
log_file_name = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
log_file_path = os.path.join(logs_dir, log_file_name)

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
    # try:
    #     a = 10/0
        
    # except:
    #     # raise CustomException
    #     logging.error("division by zero")