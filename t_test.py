import os
import pandas as pd


class T_test():

    def get_max_value_from_csv_column(self, csv_file, column):
        df = pd.read_csv(csv_file)

        return max(df[column])

    def gather_folder_information(self, custom_logs_folder_path):

        model_folders = os.listdir(custom_logs_folder_path)

        for folder in model_folders:
            path = custom_logs_folder_path + "\\" + folder

            for file in os.listdir(path):
                folder_information = {
                    "Model": "",
                    "Serial": None,
                    "Seed": None,
                    "File extension": "",
                    "Type": "",
                    "Date": "",
                    "Time": "",
                    "Full name": "",
                    "Path": "",
                    "Max_val_acc": None
                }

                # Example: Folder name: Model_11_S3_R1_2020-04-04_11-33-10

                # File path
                file_path = custom_logs_folder_path + "\\" + folder + "\\" + file

                # print(file_path)
                # parse file name and store it to a dictonary
                y = file.split('_')
                x = file.split(".")
                folder_information['Model'] = y[0] + " " + y[1]
                folder_information['Serial'] = y[2]
                folder_information['Seed'] = y[3]
                folder_information['Date'] = y[4]
                folder_information['Time'] = y[5]
                folder_information['Full name'] = file
                folder_information['File extension'] = x[1]
                folder_information['Path'] = file_path

                if "_confusion_matrix" in file:
                    folder_information['Type'] = "_confusion_matrix"
                    folder_information['Time'] = y[5]
                elif "_hyper" in file:
                    folder_information['Type'] = "_hyper"
                    folder_information['Time'] = y[5]
                elif "_prediction" in file:
                    folder_information['Type'] = "_prediction"
                    folder_information['Time'] = y[5]
                else:
                    if "csv" in x[1]:
                        folder_information['Max_val_acc'] = self.get_max_value_from_csv_column(file_path,
                                                                                               'val_accuracy')
                    folder_information['Type'] = "other"
                    time = y[5].split('.')
                    folder_information['Time'] = time[0]

        return folder_information

    def remove_folders_without_max_val_acc(self, folders):

        for entry in folders.items():
            key = entry[0]
            val = entry[1]

            print("Key: " + key + " Value:" + str(val))

        return folders