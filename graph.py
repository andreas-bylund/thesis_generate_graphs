import matplotlib.pyplot as plt
import numpy as np


class Graph:
    def __init__(self, plot1, plot2, title, xlabel, ylabel, validation=False, save_path=None):

        self.plot1 = plot1
        self.plot2 = plot2
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.validation = validation
        self.save_path = save_path

    def generate_graph(self):
        plt.subplots()

        plt.xlim(xmin=0)
        plt.ylim(ymin=0)

        graph_plot1, = plt.plot(
            self.plot1.get_x_data(),
            self.plot1.get_y_data(),
            self.plot1.get_color()
        )

        graph_plot2, = plt.plot(
            self.plot2.get_x_data(),
            self.plot2.get_y_data(),
            self.plot2.get_color()
        )

        if self.validation:
            plt.yticks(np.arange(0, 3.5, 0.5))
        else:
            plt.yticks(np.arange(0, 1, 0.1))

        plt.legend([graph_plot1, graph_plot2], [self.plot1.get_label(), self.plot2.get_label()])
        plt.xticks(np.arange(0, 50, 10))
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)
        plt.grid()

        #plt.show()
        plt.savefig(self.save_path + '\graph.png')
        plt.close()