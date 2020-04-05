class PlotData:

    def __init__(self, x, y, color, label):
        self.x_data = x
        self.y_data = y
        self.color = color
        self.label = label

    def get_x_data(self):
        return self.x_data

    def get_y_data(self):
        return self.y_data

    def get_color(self):
        return self.color

    def get_label(self):
        return self.label
