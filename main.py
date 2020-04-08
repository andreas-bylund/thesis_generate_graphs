from graphics import Graphics as gh
from gather_data_helper import Gather_data_helper
from t_test import T_test as T_test

import time

if __name__ == "__main__":
    start_time = time.time()

    dh = Gather_data_helper()

    # Where is Custom_logs folder located?
    custom_logs_folder_path = r"C:\Users\Andreas Bylund\Desktop\Backup - Tränade modeller och logs\Custom_logs"

    # Get folder and file information
    data = dh.gather_folder_information(custom_logs_folder_path)

    # Get average result from all models
    result = dh.get_average_validation_acc(data)

    print(result)

    print("--- %s seconds ---" % (time.time() - start_time))
