import os
import pandas as pd


class T_test():

    def get_max_value_from_csv_column(self, csv_file, column):
        df = pd.read_csv(csv_file)

        return max(df[column])

