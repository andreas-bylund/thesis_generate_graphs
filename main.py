import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from plotdata import PlotData
from graph import Graph as gh
from t_test import T_test
import time


def generate_graph(csv_file, save_path):
    ''' Generate a graph

    This function generates a graph with data from csv_file.

     Each line (PlotData) in the graph have some settings (parameters). For example:
        - x values - [List] X values on the graph
        - y values - [List] Y values on the graph
        - color - [String] What color the line is going to have
        - label - [String] Label/name of the line. Used for "plt.legend"

     Even the graph (gh) have some settings (parameters). For example:
        - gh(line (plot) 1, line (plot) 2, Title on graph, x label, y label, ticks settings (more information
        about this further down), save path
        plot1 - [PlotData obj] Obj containing line data
        plot2 - [PlotData obj] Obj containing line data
        title,- [String] Title on the graph
        xlabel - [String] X-label
        ylabel - [String] Y-label
        validation - [Boolean] A flag that determines how the y-values are going to be generated (plt.yticks). So right
        now there are two different settings (true or false). (If you need more settings this could be changed to a
        string or something.)
        save_path - [String] Where the graph is going to be saved.

    :args:
        :param csv_file: The location of the csv file where the data are collected
        :param save_path: The location where the graph is going to be saved at
    '''

    # Read the csv file
    df = pd.read_csv(csv_file)

    # Epochs
    epochs = []
    for x in range(len(df['loss'])):
        epochs.append(x)

    # Accuracy
    plot1 = PlotData(epochs, df['val_accuracy'], "red", "Validation accuracy")
    plot2 = PlotData(epochs, df['accuracy'], "blue", "Training accuracy")

    graph = gh(plot1, plot2, "TITLE", "Training Epoch", "Training Accuracy", False, save_path)
    graph.generate_graph()
    del plot1, plot2, graph

    # Loss
    plot1 = PlotData(epochs, df['val_loss'], "red", "Validation loss")
    plot2 = PlotData(epochs, df['loss'], "blue", "Training loss")

    graph = gh(plot1, plot2, "TITLE", "Training Epoch", "Training Loss", True, save_path)
    graph.generate_graph()
    del plot1, plot2, graph


def main(custom_logs_folder_path):
    ''' Find folder containing data

    This function find all models sub folders in Custom_logs and fetches the right .csv file containing the
    data we want to generate graph form. This function do also create a folder called "graphs" if the folder
    doesn't exists.

    There are three different types of .csv in Custom_logs folder. This script in the current form is only
    interested in the .csv file not containing "_confusion_matrix", "_hyper" or "_prediction".

    :args:
        :param custom_logs_folder_path: The location of Custom_logs folder
    '''
    model_folders = os.listdir(custom_logs_folder_path)

    for folder in model_folders:
        path = custom_logs_folder_path + "\\" + folder

        for file in os.listdir(path):
            if file.endswith(".csv"):
                if "_confusion_matrix" not in file and \
                        "_hyper" not in file and \
                        "_prediction" not in file: \
 \

                        # Create a folder that stores graphs
                        try:
                            os.mkdir(path + '\\' + "graphs")
                        except FileExistsError:
                            pass

                        csv_file = path + '\\' + file
                        save_path = path + '\\' + "graphs"
                        generate_graph(csv_file, save_path)

if __name__ == "__main__":
    start_time = time.time()

    # Where is Custom_logs folder located?
    custom_logs_folder_path = r"C:\Users\Andreas Bylund\Desktop\Python T-test\Custom_logs"

    # T-Test
    T_test = T_test()

    # Get folder and file information
    folders = T_test.gather_folder_information(custom_logs_folder_path)

    # Remove information which does not have any "Max_val_acc" value
    folders = T_test.remove_folders_without_max_val_acc(folders)
    print("--- %s seconds ---" % (time.time() - start_time))

    print(folders)

    #main(custom_logs_folder_path)
