import cv2
import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class video_window(QWidget):
    def __init__(self, path):
        super(video_window, self).__init__()
        self.path = path

        self.setWindowTitle('Video window')
        self.resize(500, 375)
        self.move(550, 550)
        # The display for the graph
        self.video = QLabel()

        self.video_data = cv2.VideoCapture(self.path)
        self.len_video_frame = int(self.video_data.get(cv2.CAP_PROP_FRAME_COUNT))

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        main_layout.addWidget(self.video)

    def play_video(self, step):

        self.video_data.set(cv2.CAP_PROP_POS_FRAMES, step * int(self.len_video_frame/66))
        rval, frame = self.video_data.read()
        # transfer channel
        frame = cv2.resize(frame, (480, 360), interpolation=cv2.INTER_AREA)
        RGBImg = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # transfer the format
        image = QImage(RGBImg.data, RGBImg.shape[1], RGBImg.shape[0], QImage.Format_RGB888)
        self.video.setPixmap(QPixmap.fromImage(image))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    path = 'C:/Users/Haonan Yuan/Documents/Oregon state University/Python_workspace/data_visualization/drawer_tests/trial_one_tests/trial_2/trial_2.avi'
    the_mainwindow = video_window(path)
    the_mainwindow.show()
    sys.exit(app.exec_())

