import sys
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class ForceWindow(QWidget):
    def __init__(self, angle, data, time):
        super(ForceWindow, self).__init__()
        # path = 'C:/Users/Haonan Yuan/Documents/Oregon state University/Python_workspace/Interface_door_PyQT/Door/5.csv'
        self.angle = angle
        self.sensor = data
        self.time = time

        self.move(550, 300)

        self.setWindowTitle('Force_Graph: Sensor')
        self.resize(640, 480)
        # The display for the graph
        self.figure = Figure()
        self.display = FigureCanvas(self.figure)
        self.figure.clear()

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        but_layout = QHBoxLayout()

        main_layout.addWidget(self.display)
        main_layout.addLayout(but_layout)

        self.show()

    def get_data(self, sensor_num):
        time_data = []
        for i in range(len(self.time)):
            time_data.append(i)
        force_data = self.sensor[:, sensor_num]
        return time_data, force_data

    def draw(self, num, t=0):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        time, force = self.get_data(num)
        ax.plot(time, force)
        ax.plot(time[t], force[t], 'ro')
        ax.set_title('Force_Graph: Sensor ' + str(num + 1))
        ax.set_xlabel('Time(s)')
        ax.set_ylabel('Force(N)')
        self.display.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_mainwindow = ForceWindow()
    the_mainwindow.show()
    sys.exit(app.exec_())
