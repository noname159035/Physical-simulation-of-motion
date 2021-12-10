from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMainWindow
from Resurces import res_rc

class Ui_Line(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('Forms\\line.ui', self)
        self.button_line_input_speed_start.clicked.connect(self.save_speed_sart)
        self.button_line_input_acceleration.clicked.connect(self.save_acceleration)
        self.button_line_input_mov.clicked.connect(self.save_mov)
        self.button_line_input_time.clicked.connect(self.save_time)
        self.button_line_input_speed_finish.clicked.connect(self.save_speed_finish)
        self.button_line_input_way.clicked.connect(self.save_way)


    def save_speed_sart(self):
        pass

    def save_acceleration(self):
        pass

    def save_mov(self):
        pass

    def save_time(self):
        pass

    def save_speed_finish(self):
        pass

    def save_way(self):
        pass