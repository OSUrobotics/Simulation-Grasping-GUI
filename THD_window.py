import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt5.QtOpenGL import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from read_file_csv import read_file
from model_data import door_data, drawer_date


class THD_window(QWidget):
    def __init__(self, angle, data, time):
        super(THD_window, self).__init__()

        self.widget = glWidget(angle, data, time)
        #self.setMinimumSize(640, 480)

        self.xSlider = self.createVSlider()
        self.ySlider = self.createHSlider()

        self.xSlider.valueChanged.connect(self.widget.setXRotation)
        self.ySlider.valueChanged.connect(self.widget.setYRotation)

        self.xSlider.setValue(360 * 16)

        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.xSlider)
        self.setLayout(mainLayout)
        right_side_layout = QVBoxLayout()
        mainLayout.addLayout(right_side_layout)

        right_side_layout.addWidget(self.widget)
        right_side_layout.addWidget(self.ySlider)

        self.setWindowTitle("Door Model")

        self.widget.updateGL()

    def createVSlider(self):
        slider = QSlider(Qt.Vertical)
        slider.setRange(0, 360 * 16)
        slider.setSingleStep(16)
        """slider.setPageStep(15 * 16)
        slider.setTickInterval(15 * 16)
        slider.setTickPosition(QSlider.TicksRight)"""
        return slider

    def createHSlider(self):
        slider = QSlider(Qt.Horizontal)
        slider.setRange(0, 360 * 16)
        slider.setSingleStep(16)
        """slider.setPageStep(15 * 16)
        slider.setTickInterval(15 * 16)
        slider.setTickPosition(QSlider.TicksRight)"""
        return slider


class glWidget(QGLWidget):

    def __init__(self, angle, data, time, parent=None):
        QGLWidget.__init__(self, parent)
        self.setMinimumSize(640, 480)
        self.xRot = 0
        self.yRot = 0
        self.zRot = 0
        self.dRot = 0
        self.dist = 0
        self.color_1 = (0, 0, 1)
        self.color_2 = (0, 0, 1)
        self.color_3 = (0, 0, 1)
        self.color_4 = (0, 0, 1)
        self.color_5 = (0, 0, 1)
        self.color_6 = (0, 0, 1)
        self.color_7 = (0, 0, 1)
        self.color_8 = (0, 0, 1)
        self.color_9 = (0, 0, 1)
        self.color_10 = (0, 0, 1)
        self.color_11 = (0, 0, 1)
        self.color_12 = (0, 0, 1)
        self.color_13 = (0, 0, 1)
        self.color_14 = (0, 0, 1)
        self.color_15 = (0, 0, 1)
        self.color_16 = (0, 0, 1)
        self.data = angle
        self.sensor = data
        self.time = time
        self.door_box_vertex = door_data(name='door_box_vertex')
        self.door_plate_vertex = door_data(name='door_plate_vertex')
        self.door_handle_vertex = door_data(name='door_handle_vertex')
        self.plate_sensor1_vertex = door_data(name='plate_sensor1_vertex')
        self.plate_sensor2_vertex = door_data(name='plate_sensor2_vertex')
        self.plate_sensor3_vertex = door_data(name='plate_sensor3_vertex')
        self.plate_sensor4_vertex = door_data(name='plate_sensor4_vertex')
        self.handle_sensor1_vertex = door_data(name='handle_sensor1_vertex')
        self.handle_sensor2_vertex = door_data(name='handle_sensor2_vertex')
        self.handle_sensor3_vertex = door_data(name='handle_sensor3_vertex')
        self.handle_sensor4_vertex = door_data(name='handle_sensor4_vertex')
        self.handle_sensor5_vertex = door_data(name='handle_sensor5_vertex')
        self.handle_sensor6_vertex = door_data(name='handle_sensor6_vertex')
        self.handle_sensor7_vertex = door_data(name='handle_sensor7_vertex')
        self.handle_sensor8_vertex = door_data(name='handle_sensor8_vertex')
        self.handle_sensor9_vertex = door_data(name='handle_sensor9_vertex')
        self.handle_sensor10_vertex = door_data(name='handle_sensor10_vertex')
        self.handle_sensor11_vertex = door_data(name='handle_sensor11_vertex')
        self.handle_sensor12_vertex = door_data(name='handle_sensor12_vertex')
        self.drawer_box_vertex = drawer_date(name='drawer_box_vertex')
        self.drawer_vertex = drawer_date(name='drawer_vertex')
        self.drawer_handle_vertex = drawer_date(name='drawer_handle_vertex')
        self.drawer_sensor1_vertex = drawer_date(name='drawer_sensor1_vertex')
        self.drawer_sensor2_vertex = drawer_date(name='drawer_sensor2_vertex')
        self.drawer_sensor3_vertex = drawer_date(name='drawer_sensor3_vertex')
        self.drawer_sensor4_vertex = drawer_date(name='drawer_sensor4_vertex')
        self.drawer_sensor5_vertex = drawer_date(name='drawer_sensor5_vertex')
        self.drawer_sensor6_vertex = drawer_date(name='drawer_sensor6_vertex')
        self.drawer_sensor7_vertex = drawer_date(name='drawer_sensor7_vertex')
        self.drawer_sensor8_vertex = drawer_date(name='drawer_sensor8_vertex')
        self.drawer_sensor9_vertex = drawer_date(name='drawer_sensor9_vertex')
        self.drawer_sensor10_vertex = drawer_date(name='drawer_sensor10_vertex')
        self.drawer_sensor11_vertex = drawer_date(name='drawer_sensor11_vertex')
        self.drawer_sensor12_vertex = drawer_date(name='drawer_sensor12_vertex')

        self.door_box_edges = door_data(name='door_box_edges')
        self.door_plate_edges = door_data(name='door_plate_edges')
        self.drawer_box_edges = drawer_date(name='drawer_box_edges')
        self.drawer_edges = drawer_date(name='drawer_edges')

        self.door_box_face = door_data(name='door_box_face')
        self.door_plate_face = door_data(name='door_plate_face')
        self.door_handle_face = door_data(name='door_handle_face')
        self.plate_sensor1_face = door_data(name='plate_sensor1_face')
        self.plate_sensor2_face = door_data(name='plate_sensor2_face')
        self.plate_sensor3_face = door_data(name='plate_sensor3_face')
        self.plate_sensor4_face = door_data(name='plate_sensor4_face')
        self.handle_sensor1_face = door_data(name='handle_sensor1_face')
        self.handle_sensor2_face = door_data(name='handle_sensor2_face')
        self.handle_sensor3_face = door_data(name='handle_sensor3_face')
        self.handle_sensor4_face = door_data(name='handle_sensor4_face')
        self.handle_sensor5_face = door_data(name='handle_sensor5_face')
        self.handle_sensor6_face = door_data(name='handle_sensor6_face')
        self.handle_sensor7_face = door_data(name='handle_sensor7_face')
        self.handle_sensor8_face = door_data(name='handle_sensor8_face')
        self.handle_sensor9_face = door_data(name='handle_sensor9_face')
        self.handle_sensor10_face = door_data(name='handle_sensor10_face')
        self.handle_sensor11_face = door_data(name='handle_sensor11_face')
        self.handle_sensor12_face = door_data(name='handle_sensor12_face')
        self.drawer_box_face = drawer_date(name='drawer_box_face')
        self.drawer_face = drawer_date(name='drawer_face')
        self.drawer_handle_face = drawer_date(name='drawer_handle_face')
        self.drawer_sensor1_face = drawer_date(name='drawer_sensor1_face')
        self.drawer_sensor2_face = drawer_date(name='drawer_sensor2_face')
        self.drawer_sensor3_face = drawer_date(name='drawer_sensor3_face')
        self.drawer_sensor4_face = drawer_date(name='drawer_sensor4_face')
        self.drawer_sensor5_face = drawer_date(name='drawer_sensor5_face')
        self.drawer_sensor6_face = drawer_date(name='drawer_sensor6_face')
        self.drawer_sensor7_face = drawer_date(name='drawer_sensor7_face')
        self.drawer_sensor8_face = drawer_date(name='drawer_sensor8_face')
        self.drawer_sensor9_face = drawer_date(name='drawer_sensor9_face')
        self.drawer_sensor10_face = drawer_date(name='drawer_sensor10_face')
        self.drawer_sensor11_face = drawer_date(name='drawer_sensor11_face')
        self.drawer_sensor12_face = drawer_date(name='drawer_sensor12_face')

    def setXRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.xRot:
            self.xRot = -angle
            self.updateGL()

    def setYRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.yRot:
            self.yRot = angle
            self.updateGL()

    """def setZRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.zRot:
            self.zRot = angle
            self.updateGL()"""

    def setDRotation(self, num):
        self.dRot = -self.data[num]
        self.updateGL()

    def setTranslate(self, num):
        self.dist = self.data[num]/100
        self.updateGL()

    def normalizeAngle(self, angle):
        while angle < 0:
            angle += 360 * 16
        while angle > 360 * 16:
            angle -= 360 * 16
        return angle

    def get_data(self, sensor_num):
        time_data = []
        for i in range(len(self.time)):
            time_data.append(i)
        force_data = self.sensor[:, sensor_num] * 0.097656
        return time_data, force_data

    def get_color(self, data, num):
        y = data[num, 0:13]
        s_color = []
        for i in y:
            i = i * 204.8
            if 0 <= i <= 255:
                force_color = [0, i / 255, 1]
            elif 256 <= i <= 511:
                force_color = [0, 1, (511 - i) / 255]
            elif 512 <= i <= 767:
                force_color = [(i - 512) / 255, 1, 0]
            elif 768 <= i <= 1023:
                force_color = [1, (1023 - i) / 255, 0]
            s_color.append(force_color)
        return s_color

    def changecolor(self, num):
        self.color_1 = self.get_color(self.sensor, num)[0]
        self.color_2 = self.get_color(self.sensor, num)[1]
        self.color_3 = self.get_color(self.sensor, num)[2]
        self.color_4 = self.get_color(self.sensor, num)[3]
        self.color_5 = self.get_color(self.sensor, num)[4]
        self.color_6 = self.get_color(self.sensor, num)[5]
        self.color_7 = self.get_color(self.sensor, num)[6]
        self.color_8 = self.get_color(self.sensor, num)[7]
        self.color_9 = self.get_color(self.sensor, num)[8]
        self.color_10 = self.get_color(self.sensor, num)[9]
        self.color_11 = self.get_color(self.sensor, num)[10]
        self.color_12 = self.get_color(self.sensor, num)[11]
        self.updateGL()

    def paintdoor(self):

        # Door box
        glBegin(GL_QUADS)
        glColor3fv((0.75, 0.7, 0.7))
        for face in self.door_box_face:
            for vertex in face:
                glVertex3fv(self.door_box_vertex[vertex])
        glEnd()

        glBegin(GL_LINES)
        glColor3fv((0, 0, 0))
        for edge in self.door_box_edges:
            for vertex in edge:
                glVertex3fv(self.door_box_vertex[vertex])
        glEnd()

        # Door plate
        glRotated(self.dRot, 0.0, 0.0, 1.0)
        glBegin(GL_QUADS)
        glColor3fv((0.75, 0.7, 0.7))
        for face in self.door_plate_face:
            for vertex in face:
                glVertex3fv(self.door_plate_vertex[vertex])
        glEnd()

        glBegin(GL_LINES)
        glColor3fv((0, 0, 0))
        for edge in self.door_plate_edges:
            for vertex in edge:
                glVertex3fv(self.door_plate_vertex[vertex])
        glEnd()

        # Door plate sensor
        glBegin(GL_TRIANGLES)
        glColor3fv(self.color_13)
        for face in self.plate_sensor1_face:
            for vertex in face:
                glVertex3fv(self.plate_sensor1_vertex[vertex])
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3fv(self.color_14)
        for face in self.plate_sensor2_face:
            for vertex in face:
                glVertex3fv(self.plate_sensor2_vertex[vertex])
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3fv(self.color_15)
        for face in self.plate_sensor3_face:
            for vertex in face:
                glVertex3fv(self.plate_sensor3_vertex[vertex])
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3fv(self.color_16)
        for face in self.plate_sensor4_face:
            for vertex in face:
                glVertex3fv(self.plate_sensor4_vertex[vertex])
        glEnd()

        # Handle
        glBegin(GL_TRIANGLES)
        glColor3fv((0, 0, 0))
        for face in self.door_handle_face:
            for vertex in face:
                glVertex3fv(self.door_handle_vertex[vertex])
        glEnd()

        # Handle Sensor
        glBegin(GL_TRIANGLES)
        glColor3fv(self.color_1)
        for face in self.handle_sensor1_face:
            for vertex in face:
                glVertex3fv(self.handle_sensor1_vertex[vertex])
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3fv(self.color_2)
        for face in self.handle_sensor2_face:
            for vertex in face:
                glVertex3fv(self.handle_sensor2_vertex[vertex])
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3fv(self.color_3)
        for face in self.handle_sensor3_face:
            for vertex in face:
                glVertex3fv(self.handle_sensor3_vertex[vertex])
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3fv(self.color_4)
        for face in self.handle_sensor4_face:
            for vertex in face:
                glVertex3fv(self.handle_sensor4_vertex[vertex])
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3fv(self.color_5)
        for face in self.handle_sensor5_face:
            for vertex in face:
                glVertex3fv(self.handle_sensor5_vertex[vertex])
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3fv(self.color_6)
        for face in self.handle_sensor6_face:
            for vertex in face:
                glVertex3fv(self.handle_sensor6_vertex[vertex])
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3fv(self.color_7)
        for face in self.handle_sensor7_face:
            for vertex in face:
                glVertex3fv(self.handle_sensor7_vertex[vertex])
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3fv(self.color_8)
        for face in self.handle_sensor8_face:
            for vertex in face:
                glVertex3fv(self.handle_sensor8_vertex[vertex])
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3fv(self.color_9)
        for face in self.handle_sensor9_face:
            for vertex in face:
                glVertex3fv(self.handle_sensor9_vertex[vertex])
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3fv(self.color_10)
        for face in self.handle_sensor10_face:
            for vertex in face:
                glVertex3fv(self.handle_sensor10_vertex[vertex])
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3fv(self.color_11)
        for face in self.handle_sensor11_face:
            for vertex in face:
                glVertex3fv(self.handle_sensor11_vertex[vertex])
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3fv(self.color_12)
        for face in self.handle_sensor12_face:
            for vertex in face:
                glVertex3fv(self.handle_sensor12_vertex[vertex])
        glEnd()

    def paintdrawer(self):

        # drawer_box
        glBegin(GL_TRIANGLES)
        glColor3fv((0.75, 0.7, 0.7))
        for face in self.drawer_box_face:
            for vertex in face:
                glVertex3fv(self.drawer_box_vertex[vertex])
        glEnd()

        # drawer
        glTranslate(self.dist, 0.0, 0.0)
        glBegin(GL_TRIANGLES)
        glColor3fv((0.0, 0.7, 0.7))
        for face in self.drawer_face:
            for vertex in face:
                glVertex3fv(self.drawer_vertex[vertex])
        glEnd()

        # handle
        glBegin(GL_TRIANGLES)
        glColor3fv((0.0, 0.0, 0.0))
        for face in self.drawer_handle_face:
            for vertex in face:
                glVertex3fv(self.drawer_handle_vertex[vertex])
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3fv(self.color_1)
        for face in self.drawer_sensor1_face:
            for vertex in face:
                glVertex3fv(self.drawer_sensor1_vertex[vertex])
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3fv(self.color_2)
        for face in self.drawer_sensor2_face:
            for vertex in face:
                glVertex3fv(self.drawer_sensor2_vertex[vertex])
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3fv(self.color_3)
        for face in self.drawer_sensor3_face:
            for vertex in face:
                glVertex3fv(self.drawer_sensor3_vertex[vertex])
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3fv(self.color_4)
        for face in self.drawer_sensor4_face:
            for vertex in face:
                glVertex3fv(self.drawer_sensor4_vertex[vertex])
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3fv(self.color_5)
        for face in self.drawer_sensor5_face:
            for vertex in face:
                glVertex3fv(self.drawer_sensor5_vertex[vertex])
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3fv(self.color_6)
        for face in self.drawer_sensor6_face:
            for vertex in face:
                glVertex3fv(self.drawer_sensor6_vertex[vertex])
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3fv(self.color_7)
        for face in self.drawer_sensor7_face:
            for vertex in face:
                glVertex3fv(self.drawer_sensor7_vertex[vertex])
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3fv(self.color_8)
        for face in self.drawer_sensor8_face:
            for vertex in face:
                glVertex3fv(self.drawer_sensor8_vertex[vertex])
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3fv(self.color_9)
        for face in self.drawer_sensor9_face:
            for vertex in face:
                glVertex3fv(self.drawer_sensor9_vertex[vertex])
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3fv(self.color_10)
        for face in self.drawer_sensor10_face:
            for vertex in face:
                glVertex3fv(self.drawer_sensor10_vertex[vertex])
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3fv(self.color_11)
        for face in self.drawer_sensor11_face:
            for vertex in face:
                glVertex3fv(self.drawer_sensor11_vertex[vertex])
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3fv(self.color_12)
        for face in self.drawer_sensor12_face:
            for vertex in face:
                glVertex3fv(self.drawer_sensor12_vertex[vertex])
        glEnd()

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glLoadIdentity()
        # Set the camera view
        glTranslatef(-2, 0.0, -15.0)
        glPolygonMode(GL_FRONT, GL_FILL)
        # Rotate model by slider bar
        glRotated(self.xRot / 16.0, 1.0, 0.0, 0.0)
        glRotated(self.yRot / 16.0, 0.0, 1.0, 0.0)

        # Rotate model to the front view
        glRotatef(-120, 0, 1, 0)
        glRotatef(270, 1, 0, 0)

        # self.paintdoor()
        self.paintdrawer()

        glFlush()

    def initializeGL(self):
        # glClearDepth(1.0)
        glClearColor(1.0, 1.0, 1.0, 1.0)
        # glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_FLAT)

    def resizeGL(self, w: int, h: int):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        # glOrtho(-5, 5, 5, -5, 4.0, 7.0)
        gluPerspective(45.0, w/h, 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = THD_window()
    viewer.show()
    sys.exit(app.exec_())