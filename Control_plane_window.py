import sys
import re
import os

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from read_file_csv import read_file
from Force_graph_window import ForceWindow
from TD_window import TDWindow
from THD_window import THD_window
from Video_window import video_window


def createSlider():

    slider = QSlider(Qt.Horizontal)
    slider.setRange(0, 360 * 16)
    slider.setSingleStep(16)
    return slider


class ControlPlane(QWidget):
    def __init__(self):
        super(ControlPlane, self).__init__()
        self.initUI()

    def initUI(self):

        self.move(100, 300)

        self.setWindowTitle('ControlPlane')
        self.resize(400, 480)
        initLayout = QHBoxLayout()
        self.setLayout(initLayout)
        left_side_layout = QVBoxLayout()
        right_side_layout = QVBoxLayout()
        initLayout.addLayout(left_side_layout)
        initLayout.addLayout(right_side_layout)

        self.angle = []
        self.time = []
        self.data = []
        self.range = 0

        self.step = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_func)

        self.openfile = QPushButton('Open Folder', self)
        self.openfile.clicked.connect(self.open_file)
        left_side_layout.addWidget(self.openfile)

        self.buttonstart = QPushButton('Start', self)
        self.buttonstart.clicked.connect(self.start_stop_func)
        left_side_layout.addWidget(self.buttonstart)

        self.buttonshow = QPushButton('Show 3D and Video Windows')
        self.buttonshow.clicked.connect(self.show_thdmodel)
        left_side_layout.addWidget(self.buttonshow)

        self.slid_button = QSlider(Qt.Horizontal)
        self.slid_button.setRange(0, 1000)
        self.slid_button.setSingleStep(1)
        self.slid_button.setValue(0)

        self.sensor_num = QLabel('Sensor: ')
        self.sensor_num.setAlignment(Qt.AlignCenter)
        left_side_layout.addWidget(self.sensor_num)

        self.f_label = QLabel('Force: ' + '0.000 ' + 'N')
        self.f_label.setAlignment(Qt.AlignCenter)
        left_side_layout.addWidget(self.f_label)

        self.t_label = QLabel('Time: ' + '0.000 ' + 'Sec')
        self.t_label.setAlignment(Qt.AlignCenter)
        left_side_layout.addWidget(self.t_label)

        self.slid_button.valueChanged.connect(self.value)
        left_side_layout.addWidget(self.slid_button)

        self.r_label = QLabel('Rotate Plate: ' + '0.000 ' + 'Degrees')
        self.r_label.setAlignment(Qt.AlignCenter)
        left_side_layout.addWidget(self.r_label)

        self.ds_label = QLabel('Distance: ' + '0.000 ' + 'mm')
        self.ds_label.setAlignment(Qt.AlignCenter)
        left_side_layout.addWidget(self.ds_label)

        self.button1 = QRadioButton('Sensor_1')
        self.button1.toggled.connect(self.buttonState)
        self.button2 = QRadioButton('Sensor_2')
        self.button2.toggled.connect(self.buttonState)
        self.button3 = QRadioButton('Sensor_3')
        self.button3.toggled.connect(self.buttonState)
        self.button4 = QRadioButton('Sensor_4')
        self.button4.toggled.connect(self.buttonState)
        self.button5 = QRadioButton('Sensor_5')
        self.button5.toggled.connect(self.buttonState)
        self.button6 = QRadioButton('Sensor_6')
        self.button6.toggled.connect(self.buttonState)
        self.button7 = QRadioButton('Sensor_7')
        self.button7.toggled.connect(self.buttonState)
        self.button8 = QRadioButton('Sensor_8')
        self.button8.toggled.connect(self.buttonState)
        self.button9 = QRadioButton('Sensor_9')
        self.button9.toggled.connect(self.buttonState)
        self.button10 = QRadioButton('Sensor_10')
        self.button10.toggled.connect(self.buttonState)
        self.button11 = QRadioButton('Sensor_11')
        self.button11.toggled.connect(self.buttonState)

        self.button12 = QRadioButton('Sensor_12')
        self.button12.toggled.connect(self.buttonState)
        self.button13 = QRadioButton('Sensor_13')
        self.button13.toggled.connect(self.buttonState)
        self.button14 = QRadioButton('Sensor_14')
        self.button14.toggled.connect(self.buttonState)

        right_side_layout.addWidget(self.button1)
        right_side_layout.addWidget(self.button2)
        right_side_layout.addWidget(self.button3)
        right_side_layout.addWidget(self.button4)
        right_side_layout.addWidget(self.button5)
        right_side_layout.addWidget(self.button6)
        right_side_layout.addWidget(self.button7)
        right_side_layout.addWidget(self.button8)
        right_side_layout.addWidget(self.button9)
        right_side_layout.addWidget(self.button10)
        right_side_layout.addWidget(self.button11)
        right_side_layout.addWidget(self.button12)
        right_side_layout.addWidget(self.button13)
        right_side_layout.addWidget(self.button14)

    def open_file(self):
        directory1 = QFileDialog.getExistingDirectory(self, "Open file", "./")
        files = os.listdir(directory1)
        path_data = directory1 + '/' + files[0]
        path_video = directory1 + '/' + files[1]
        if 'door' in directory1 or 'Door' in directory1:
            self.model_type = 'door'
        elif 'drawer' in directory1 or 'Drawer' in directory1:
            self.model_type = 'drawer'
        else:
            model_type = 'None'
        self.angle, self.data, self.time = read_file(path_data, self.model_type)
        self.slid_button.setRange(0, len(self.time) - 1)
        ControlPlane.sensor_window = ForceWindow(self.angle, self.data, self.time)
        ControlPlane.color_window = TDWindow(self.angle, self.data, self.time, self.model_type)
        ControlPlane.th_window = THD_window(self.angle, self.data, self.time, self.model_type)
        ControlPlane.video_window = video_window(path_video)

    def buttonState(self):

        radioButton = self.sender()
        if radioButton.text() == 'Sensor_1':
            if radioButton.isChecked():
                num = 0
                self.sensor_num.setText('{0}: {1}'.format('Sensor', str(num + 1)))
                ControlPlane.sensor_window.draw(num=0)
                ControlPlane.color_window.draw(num=0)
        elif radioButton.text() == 'Sensor_2':
            if radioButton.isChecked():
                num = 1
                self.sensor_num.setText('{0}: {1}'.format('Sensor', str(num + 1)))
                ControlPlane.sensor_window.draw(num=1)
                ControlPlane.color_window.draw(num=0)
        elif radioButton.text() == 'Sensor_3':
            if radioButton.isChecked():
                num = 2
                self.sensor_num.setText('{0}: {1}'.format('Sensor', str(num + 1)))
                ControlPlane.sensor_window.draw(num=2)
                ControlPlane.color_window.draw(num=0)
        elif radioButton.text() == 'Sensor_4':
            if radioButton.isChecked():
                num = 3
                self.sensor_num.setText('{0}: {1}'.format('Sensor', str(num + 1)))
                ControlPlane.sensor_window.draw(num=3)
                ControlPlane.color_window.draw(num=0)
        elif radioButton.text() == 'Sensor_5':
            if radioButton.isChecked():
                num = 4
                self.sensor_num.setText('{0}: {1}'.format('Sensor', str(num + 1)))
                ControlPlane.sensor_window.draw(num=4)
                ControlPlane.color_window.draw(num=0)
        elif radioButton.text() == 'Sensor_6':
            if radioButton.isChecked():
                num = 5
                self.sensor_num.setText('{0}: {1}'.format('Sensor', str(num + 1)))
                ControlPlane.sensor_window.draw(num=5)
                ControlPlane.color_window.draw(num=0)
        elif radioButton.text() == 'Sensor_7':
            if radioButton.isChecked():
                num = 6
                self.sensor_num.setText('{0}: {1}'.format('Sensor', str(num + 1)))
                ControlPlane.sensor_window.draw(num=6)
                ControlPlane.color_window.draw(num=0)
        elif radioButton.text() == 'Sensor_8':
            if radioButton.isChecked():
                num = 7
                self.sensor_num.setText('{0}: {1}'.format('Sensor', str(num + 1)))
                ControlPlane.sensor_window.draw(num=7)
                ControlPlane.color_window.draw(num=0)
        elif radioButton.text() == 'Sensor_9':
            if radioButton.isChecked():
                num = 8
                self.sensor_num.setText('{0}: {1}'.format('Sensor', str(num + 1)))
                ControlPlane.sensor_window.draw(num=8)
                ControlPlane.color_window.draw(num=0)
        elif radioButton.text() == 'Sensor_10':
            if radioButton.isChecked():
                num = 9
                self.sensor_num.setText('{0}: {1}'.format('Sensor', str(num + 1)))
                ControlPlane.sensor_window.draw(num=9)
                ControlPlane.color_window.draw(num=0)
        elif radioButton.text() == 'Sensor_11':
            if radioButton.isChecked():
                num = 10
                self.sensor_num.setText('{0}: {1}'.format('Sensor', str(num + 1)))
                ControlPlane.sensor_window.draw(num=10)
                ControlPlane.color_window.draw(num=0)
        elif radioButton.text() == 'Sensor_12':
            if radioButton.isChecked():
                num = 11
                self.sensor_num.setText('{0}: {1}'.format('Sensor', str(num + 1)))
                ControlPlane.sensor_window.draw(num=11)
                ControlPlane.color_window.draw(num=0)
        elif radioButton.text() == 'Sensor_13':
            if radioButton.isChecked():
                num = 12
                self.sensor_num.setText('{0}: {1}'.format('Sensor', str(num + 1)))
                ControlPlane.sensor_window.draw(num=12)
                ControlPlane.color_window.draw(num=0)
        elif radioButton.text() == 'Sensor_14':
            if radioButton.isChecked():
                num = 13
                self.sensor_num.setText('{0}: {1}'.format('Sensor', str(num + 1)))
                ControlPlane.sensor_window.draw(num=13)
                ControlPlane.color_window.draw(num=0)

    def value(self):
        """Return the current value of the slider"""
        num = self.sensor_num.text()
        sen_num = re.sub(r'Sensor: ', '', num)
        value = self.slid_button.value()
        time_value, force_value = self.data_update(value, int(sen_num) - 1)
        self.t_label.setText('{0}: {1:.3f} {2}'.format('Time', time_value, 'Sec'))
        self.f_label.setText('{0}: {1:.3f} {2}'.format('Force', force_value, 'N'))
        if self.model_type == 'drawer':
            self.ds_label.setText('{0}: {1:.3f} {2}'.format('Distance', self.angle[value], 'mm'))
            ControlPlane.th_window.widget.setTranslate(num=value)
        else:
            self.r_label.setText('{0}: {1:.3f} {2}'.format('Rotate Plate', self.angle[value], 'Degrees'))
            ControlPlane.th_window.widget.setDRotation(num=value)
        ControlPlane.sensor_window.draw(num=int(sen_num) - 1, t=value)
        ControlPlane.color_window.draw(num=value)
        ControlPlane.th_window.widget.changecolor(num=value)

        ControlPlane.video_window.play_video(step=value)

    def update_func(self):
        num = self.sensor_num.text()
        sen_num = re.sub(r'Sensor: ', '', num)
        time_value, force_value = self.data_update(self.step, int(sen_num) - 1)
        self.t_label.setText('{0}: {1:.3f} {2}'.format('Time', time_value, 'Sec'))
        self.f_label.setText('{0}: {1:.3f} {2}'.format('Force', force_value, 'N'))
        if self.model_type == 'drawer':
            self.ds_label.setText('{0}: {1:.3f} {2}'.format('Distance', self.angle[self.step], 'mm'))
        else:
            self.r_label.setText('{0}: {1:.3f} {2}'.format('Rotate Plate', self.angle[self.step], 'Degrees'))
        ControlPlane.sensor_window.draw(num=int(sen_num) - 1, t=self.step)
        ControlPlane.color_window.draw(num=self.step)
        ControlPlane.th_window.widget.changecolor(num=self.step)
        ControlPlane.th_window.widget.setDRotation(num=self.step)
        ControlPlane.th_window.widget.setTranslate(num=self.step)
        ControlPlane.video_window.play_video(step=self.step)
        if self.step < len(self.time) - 1:
            self.step += 1
        else:
            self.step = 0

    def start_stop_func(self):
        if not self.timer.isActive():
            self.buttonstart.setText('Stop')
            # platrate = int(1000 / 60)
            self.timer.start(16)
        else:
            self.buttonstart.setText('Start')
            self.timer.stop()

    def show_thdmodel(self):
        ControlPlane.video_window.show()
        ControlPlane.th_window.show()

    def data_update(self, num, sen_num):
        num = int(num)
        time, force = self.get_data(sen_num)
        return time[num], force[num]

    def get_data(self, sensor_num):
        time_data = []
        for i in range(len(self.time)):
            time_data.append(i)
        force_data = self.data[:, sensor_num] * 0.097656

        return time_data, force_data


if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_mainwindow = ControlPlane()
    the_mainwindow.show()
    sys.exit(app.exec_())
