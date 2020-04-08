import os
import pandas as pd

class Gather_data_helper():

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

    def folder_parser(self, folder_name):

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

        folder_attributes['Model'] = y[1]
        folder_attributes['Serial'] = y[2]
        folder_attributes['Seed'] = y[3]
        folder_attributes['Date'] = y[4]
        folder_attributes['Time'] = y[5].replace("-", ":")
        folder_attributes['Full name'] = folder_name

        return folder_attributes

    def gather_files_by_type_and_file_extension(self, dict, type, file_extension):
        data = []

        for k in dict.keys():
            for x in dict[k]['Files']:
                if dict[k]['Files'][x]['Type'] == type.lower() and \
                        dict[k]['Files'][x]['File extension'] == file_extension.lower():
                    data.append(dict[k]['Files'][x])
        return data

    def get_file_path(self, dict, model, serial, seed, type, file_extension):
        path = None
        model = "Model_" + str(model)

        for k in dict.keys():

            if model in k and serial in k and seed in k:
                for x in dict[k]['Files']:
                    if dict[k]['Files'][x]['Type'] == type.lower() and \
                            dict[k]['Files'][x]['File extension'] == file_extension.lower():
                        path = dict[k]['Files'][x].get('Path')

        if path:
            return path

    def average(self, lst):
        return sum(lst) / len(lst)

    def get_average_validation_acc(self, dict):

        return_dict = {}

        data = self.gather_by_models_serials_and_their_seeds(dict)

        for k in data.keys():

            # Get average value
            list_avg = []
            paths = data.get(k)['paths']

            for path in paths:
                list_avg.append(self.get_max_value_from_csv_column(path, "val_accuracy"))

            avg_value = self.average(list_avg)
            return_dict[k] = {
                'avg_value': avg_value
            }

        return return_dict

    def gather_folder_information(self, custom_logs_folder_path):

        # Custom_logs
        file_information = {}

        model_folders = os.listdir(custom_logs_folder_path)

        for folder in model_folders:

            folder_attributes = self.folder_parser(folder)

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
        return file_information

    def gather_by_models_serials_and_their_seeds(self, dict):

        temp = {}

        for k in dict.keys():
            model = dict[k].get('Model')
            serial = dict[k].get('Serial')
            key = model + "-" + serial
            seed = dict[k].get('Seed')

            path = self.get_file_path(
                dict,
                model,
                serial,
                seed,
                'other',
                'csv'
            )

            # Check if key exists
            if key in temp:
                temp[key]['seeds'].append(seed)
                temp[key]['paths'].append(path)
            else:
                temp[key] = {
                    'seeds': [],
                    'paths': []
                }

                temp[key]['seeds'].append(seed)
                temp[key]['paths'].append(path)

        return temp