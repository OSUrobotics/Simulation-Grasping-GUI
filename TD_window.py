import sys

from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib as mpl
from numpy import cos, sin, pi, linspace


class TDWindow(QWidget):
    def __init__(self, angle, data, time, type):
        super(TDWindow, self).__init__()
        self.angle = angle
        self.data = data
        self.time = time
        self.type = type

        self.move(1200, 100)

        self.setWindowTitle('2D_model_colormap')
        self.resize(500, 375)
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

    def draw(self, num):

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        angles_circle = [j * pi / 180 for j in range(0, 360)]
        r = 0.635
        sensor6_x = r * cos(angles_circle) - 2.9
        sensor6_y = r * sin(angles_circle) + 3.429
        sensor2_x = r * cos(angles_circle) - 0.635
        sensor2_y = r * sin(angles_circle) + 3.429
        sensor9_x = r * cos(angles_circle) + 1.6256
        sensor9_y = r * sin(angles_circle) + 3.429

        sensor8_x = r * cos(angles_circle) - 1.6256
        sensor8_y = r * sin(angles_circle) + 1.6256
        sensor7_x = r * cos(angles_circle) + 0.635
        sensor7_y = r * sin(angles_circle) + 1.6256
        sensor10_x = r * cos(angles_circle) + 2.9
        sensor10_y = r * sin(angles_circle) + 1.6256

        sensor1_x = r * cos(angles_circle) - 1.6256
        sensor1_y = r * sin(angles_circle) - 1.6256
        sensor4_x = r * cos(angles_circle) + 0.635
        sensor4_y = r * sin(angles_circle) - 1.6256
        sensor11_x = r * cos(angles_circle) + 2.9
        sensor11_y = r * sin(angles_circle) - 1.6256

        sensor5_x = r * cos(angles_circle) - 2.9
        sensor5_y = r * sin(angles_circle) - 3.429
        sensor12_x = r * cos(angles_circle) - 0.635
        sensor12_y = r * sin(angles_circle) - 3.429
        sensor3_x = r * cos(angles_circle) + 1.626
        sensor3_y = r * sin(angles_circle) - 3.429

        ax.plot(sensor1_x, sensor1_y, color=(0, 0, 0))
        ax.text(-3.15, 3.179, '6', fontsize=14, color='black')
        ax.plot(sensor2_x, sensor2_y, color=(0, 0, 0))
        ax.text(-0.885, 3.179, '2', fontsize=14, color='black')
        ax.plot(sensor3_x, sensor3_y, color=(0, 0, 0))
        ax.text(1.3756, 3.179, '9', fontsize=14, color='black')
        ax.plot(sensor4_x, sensor4_y, color=(0, 0, 0))
        ax.text(-1.8756, 1.3756, '8', fontsize=14, color='black')
        ax.plot(sensor5_x, sensor5_y, color=(0, 0, 0))
        ax.text(0.385, 1.3756, '7', fontsize=14, color='black')
        ax.plot(sensor6_x, sensor6_y, color=(0, 0, 0))
        ax.text(2.4, 1.3756, '10', fontsize=14, color='black')
        ax.plot(sensor7_x, sensor7_y, color=(0, 0, 0))
        ax.text(- 1.8756, -1.8756, '1', fontsize=14, color='black')
        ax.plot(sensor8_x, sensor8_y, color=(0, 0, 0))
        ax.text(0.385, -1.8756, '4', fontsize=14, color='black')
        ax.plot(sensor9_x, sensor9_y, color=(0, 0, 0))
        ax.text(2.4, -1.8756, '11', fontsize=14, color='black')
        ax.plot(sensor10_x, sensor10_y, color=(0, 0, 0))
        ax.text(- 3.15, - 3.679, '5', fontsize=14, color='black')
        ax.plot(sensor11_x, sensor11_y, color=(0, 0, 0))
        ax.text(- 1.135, - 3.679, '12', fontsize=14, color='black')
        ax.plot(sensor12_x, sensor12_y, color=(0, 0, 0))
        ax.text(1.376, - 3.679, '3', fontsize=14, color='black')

        sensor1_c, = ax.fill(sensor1_x, sensor1_y, color=(0, 0, 1), alpha=1)
        sensor2_c, = ax.fill(sensor2_x, sensor2_y, color=(0, 0, 1), alpha=1)
        sensor3_c, = ax.fill(sensor3_x, sensor3_y, color=(0, 0, 1), alpha=1)
        sensor4_c, = ax.fill(sensor4_x, sensor4_y, color=(0, 0, 1), alpha=1)
        sensor5_c, = ax.fill(sensor5_x, sensor5_y, color=(0, 0, 1), alpha=1)
        sensor6_c, = ax.fill(sensor6_x, sensor6_y, color=(0, 0, 1), alpha=1)
        sensor7_c, = ax.fill(sensor7_x, sensor7_y, color=(0, 0, 1), alpha=1)
        sensor8_c, = ax.fill(sensor8_x, sensor8_y, color=(0, 0, 1), alpha=1)
        sensor9_c, = ax.fill(sensor9_x, sensor9_y, color=(0, 0, 1), alpha=1)
        sensor10_c, = ax.fill(sensor10_x, sensor10_y, color=(0, 0, 1), alpha=1)
        sensor11_c, = ax.fill(sensor11_x, sensor11_y, color=(0, 0, 1), alpha=1)
        sensor12_c, = ax.fill(sensor12_x, sensor12_y, color=(0, 0, 1), alpha=1)

        sensor1_c.set_color(self.get_color(self.data, num)[0])
        sensor2_c.set_color(self.get_color(self.data, num)[1])
        sensor3_c.set_color(self.get_color(self.data, num)[2])
        sensor4_c.set_color(self.get_color(self.data, num)[3])
        sensor5_c.set_color(self.get_color(self.data, num)[4])
        sensor6_c.set_color(self.get_color(self.data, num)[5])
        sensor7_c.set_color(self.get_color(self.data, num)[6])
        sensor8_c.set_color(self.get_color(self.data, num)[7])
        sensor9_c.set_color(self.get_color(self.data, num)[8])
        sensor10_c.set_color(self.get_color(self.data, num)[9])
        sensor11_c.set_color(self.get_color(self.data, num)[10])
        sensor12_c.set_color(self.get_color(self.data, num)[11])

        if self.type == 'door':
            sensor13_x = r * cos(angles_circle) + 4.35
            sensor13_y = r * sin(angles_circle) + 4.572
            sensor14_x = r * cos(angles_circle) + 4.35
            sensor14_y = r * sin(angles_circle) - 4.572
            ax.plot(sensor13_x, sensor13_y, color=(0, 0, 0))
            ax.text(3.85, 4.322, '13', fontsize=14, color='black')
            ax.plot(sensor14_x, sensor14_y, color=(0, 0, 0))
            ax.text(3.85, -4.822, '14', fontsize=14, color='black')
            sensor13_c, = ax.fill(sensor13_x, sensor13_y, color=(0, 0, 1), alpha=1)
            sensor14_c, = ax.fill(sensor14_x, sensor14_y, color=(0, 0, 1), alpha=1)
            sensor13_c.set_color(self.get_color(self.data, num)[12])
            sensor14_c.set_color(self.get_color(self.data, num)[13])

        ax.set_title('Color_map: Sensor')
        ax.axis('equal')
        ax.set_xticks([])
        ax.set_yticks([])
        cmap = mpl.cm.Spectral_r
        ax3 = self.figure.add_axes([0.77, 0.15, 0.05, 0.7])
        norm = mpl.colors.Normalize(vmin=0, vmax=100)
        bounds = [round(elem, 2) for elem in linspace(0, 100, 14)]
        cb3 = mpl.colorbar.ColorbarBase(ax3, cmap=cmap,
                                        norm=norm,
                                        # to use 'extend', you must
                                        # specify two extra boundaries:
                                        boundaries=[0] + bounds + [5],
                                        extend='both',
                                        ticks=bounds,  # optional
                                        spacing='proportional',
                                        orientation='vertical')
        self.display.draw()

    def get_color(self, data, num):

        y = data[num, 0:14]
        s_color = []
        for i in y:
            i = i
            if 0 <= i <= 255:
                force_color = [0, i / 255, 1]
                s_color.append(force_color)
            elif 256 <= i <= 511:
                force_color = [0, 1, (511 - i) / 255]
                s_color.append(force_color)
            elif 512 <= i <= 767:
                force_color = [(i - 512) / 255, 1, 0]
                s_color.append(force_color)
            elif 768 <= i <= 1023:
                force_color = [1, (1023 - i) / 255, 0]
                s_color.append(force_color)
        return s_color


if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_mainwindow = TDWindow()
    the_mainwindow.show()
    sys.exit(app.exec_())
