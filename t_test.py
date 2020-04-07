import os
import pandas as pd


class T_test():

    def get_max_value_from_csv_column(self, csv_file, column):
        df = pd.read_csv(csv_file)

        return max(df[column])

    def file_parser(self, file_name, path):

        file_attributes = {
            'Name': "",
            "Date": "",
            "Time": "",
            "Path": "",
            "File extension": ""
        }

        file_path = path + "\\" + file_name

        y = file_name.split('_')
        x = file_name.split(".")

        file_attributes['Name'] = file_name
        file_attributes['Date'] = y[4]
        file_attributes['File extension'] = x[1]
        file_attributes['Path'] = file_path

        if "_confusion_matrix" in file_name:
            file_attributes['Type'] = "confusion_matrix"
            file_attributes['Time'] = y[5].replace("-", ":")
        elif "_hyper" in file_name:
            file_attributes['Type'] = "hyper"
            file_attributes['Time'] = y[5].replace("-", ":")
        elif "_prediction" in file_name:
            file_attributes['Type'] = "prediction"
            file_attributes['Time'] = y[5].replace("-", ":")
        else:
            file_attributes['Type'] = "other"
            time = y[5].split('.')
            file_attributes['Time'] = time[0].replace("-", ":")

        return file_attributes

    def folder_paser(self, folder_name):

        folder_attributes = {
            "Model": "",
            "Serial": None,
            "Seed": None,
            "File extension": "",
            "Date": "",
            "Time": "",
            "Full name": "",
        }

        y = folder_name.split('_')

        folder_attributes['Model'] = y[0] + " " + y[1]
        folder_attributes['Serial'] = y[2]
        folder_attributes['Seed'] = y[3]
        folder_attributes['Date'] = y[4]
        folder_attributes['Time'] = y[5].replace("-", ":")
        folder_attributes['Full name'] = folder_name

        return folder_attributes

    def gather_folder_information(self, custom_logs_folder_path):

        # Custom_logs
        file_information = {}

        model_folders = os.listdir(custom_logs_folder_path)

        for folder in model_folders:

            folder_attributes = self.folder_paser(folder)

            file_information[folder] = {
                'Model': folder_attributes.get('Model'),
                "Serial": folder_attributes.get('Serial'),
                "Seed": folder_attributes.get('Seed'),
                "Date": folder_attributes.get('Date'),
                "Time": folder_attributes.get('Time'),
                "Full name": folder_attributes.get('Full name'),
                "Files": {}
            }

            path = custom_logs_folder_path + "\\" + folder

            counter = 0
            for file in os.listdir(path):
                file_attributes = self.file_parser(file, path)

                file_information[folder]["Files"][counter] = {
                    'Name': file_attributes.get('Name'),
                    "Date": file_attributes.get('Date'),
                    "Time": file_attributes.get('Time'),
                    "Path": file_attributes.get('Path'),
                    "Type": file_attributes.get('Type'),
                    "File extension": file_attributes.get('File extension')
                }

                counter += 1

            counter = 0
        print(file_information)
        #
        # for folder in model_folders:
        #     path = custom_logs_folder_path + "\\" + folder
        #
        #     for file in os.listdir(path):
        #         folder_information = {
        #             "Model": "",
        #             "Serial": None,
        #             "Seed": None,
        #             "File extension": "",
        #             "Type": "",
        #             "Date": "",
        #             "Time": "",
        #             "Full name": "",
        #             "Path": "",
        #             "Max_val_acc": None
        #         }
        #
        #         # Example: Folder name: Model_11_S3_R1_2020-04-04_11-33-10
        #
        #         # File path
        #         file_path = custom_logs_folder_path + "\\" + folder + "\\" + file
        #
        #         # print(file_path)
        #         # parse file name and store it to a dictonary
        #         y = file.split('_')
        #         x = file.split(".")
        #         folder_information['Model'] = y[0] + " " + y[1]
        #         folder_information['Serial'] = y[2]
        #         folder_information['Seed'] = y[3]
        #         folder_information['Date'] = y[4]
        #         folder_information['Time'] = y[5]
        #         folder_information['Full name'] = file
        #         folder_information['File extension'] = x[1]
        #         folder_information['Path'] = file_path
        #
        #         if "_confusion_matrix" in file:
        #             folder_information['Type'] = "_confusion_matrix"
        #             folder_information['Time'] = y[5]
        #         elif "_hyper" in file:
        #             folder_information['Type'] = "_hyper"
        #             folder_information['Time'] = y[5]
        #         elif "_prediction" in file:
        #             folder_information['Type'] = "_prediction"
        #             folder_information['Time'] = y[5]
        #         else:
        #             if "csv" in x[1]:
        #                 folder_information['Max_val_acc'] = self.get_max_value_from_csv_column(file_path,
        #                                                                                        'val_accuracy')
        #             folder_information['Type'] = "other"
        #             time = y[5].split('.')
        #             folder_information['Time'] = time[0]

