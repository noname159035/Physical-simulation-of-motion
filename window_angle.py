from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMainWindow
from Resurces import res_rc
from metods import var

class Ui_Angle(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('Forms\\angle.ui', self)
        self.button_angle_input_speed_start.clicked.connect(self.save_speed_start)
        self.button_angle_input_angle.clicked.connect(self.save_angle)
        self.button_angle_input_time.clicked.connect(self.save_time)
        self.button_angle_input_hight_start.clicked.connect(self.save_hight_start)
        self.button_angle_input_speed_finish.clicked.connect(self.save_speed_finish)
        self.button_angle_input_bigHieght.clicked.connect(self.save_bigHieght)
        self.button_angle_input_lenght.clicked.connect(self.save_length)
        self.button_angle_input_time_fall.clicked.connect(self.save_time_fall)
        self.button_angle_finish_input.clicked.connect(self.save_val)

    def save_speed_start(self):
        try:
            var["angle_U_st"] = float(self.angle_input_speed_start.text())
            self.angle_input_speed_finish.hide()
            self.button_angle_input_speed_finish.hide()

        except ValueError:
            print("[Log] Err: в ячейку подают строку")

    def save_angle(self):
        try:
            var["angle_d"] = float(self.angle_input_angle.text())
            self.button_angle_input_time_fall.hide()
            self.angle_input_time_fall.hide()

            self.button_angle_input_bigHieght.hide()
            self.angle_input_bigHieght.hide()

            self.button_angle_input_lenght.hide()
            self.angle_input_lenght.hide()

        except ValueError:
            print("[Log] Err: в ячейку подают строку")

    def save_time(self):
        try:
            var["angle_t"] = float(self.angle_input_time.text())
            self.button_angle_input_time_fall.hide()
            self.angle_input_time_fall.hide()

            self.button_angle_input_bigHieght.hide()
            self.angle_input_bigHieght.hide()

            self.button_angle_input_lenght.hide()
            self.angle_input_lenght.hide()
        except ValueError:
            print("[Log] Err: в ячейку подают строку")

    def save_hight_start(self):
        try:
            var["angle_h_st"] = float(self.angle_input_hight_start.text())
            self.button_angle_input_time_fall.hide()
            self.angle_input_time_fall.hide()

            self.button_angle_input_bigHieght.hide()
            self.angle_input_bigHieght.hide()

            self.button_angle_input_lenght.hide()
            self.angle_input_lenght.hide()
        except ValueError:
            print("[Log] Err: в ячейку подают строку")

    def save_speed_finish(self):
        try:
            var["angle_U_fin"] = float(self.angle_input_speed_finish.text())

            self.angle_input_speed_start.hide()
            self.button_angle_input_speed_start.hide()

            self.angle_input_lenght.hide()
            self.button_angle_input_lenght.hide()

            self.button_angle_input_bigHieght.hide()
            self.angle_input_bigHieght.hide()

            self.button_angle_input_time_fall.hide()
            self.angle_input_time_fall.hide()
        except ValueError:
            print("[Log] Err: в ячейку подают строку")

    def save_bigHieght(self):
        try:
            var["angle_H"] = float(self.angle_input_bigHieght.text())

            self.angle_input_speed_finish.hide()
            self.button_angle_input_speed_finish.hide()

            self.angle_input_angle.hide()
            self.button_angle_input_angle.hide()

            self.angle_input_time.hide()
            self.button_angle_input_time.hide()

            self.angle_input_hight_start.hide()
            self.button_angle_input_hight_start.hide()
        except ValueError:
            print("[Log] Err: в ячейку подают строку")

    def save_length(self):
        try:
            var["angle_L"] = float(self.angle_input_lenght.text())
            self.angle_input_speed_finish.hide()
            self.button_angle_input_speed_finish.hide()

            self.angle_input_angle.hide()
            self.button_angle_input_angle.hide()

            self.angle_input_time.hide()
            self.button_angle_input_time.hide()

            self.angle_input_hight_start.hide()
            self.button_angle_input_hight_start.hide()


        except ValueError:
            print("[Log] Err: в ячейку подают строку")

    def save_time_fall(self):
        try:
            var["angle_t_fall"] = float(self.angle_input_time_fall.text())
            self.angle_input_speed_finish.hide()
            self.button_angle_input_speed_finish.hide()

            self.angle_input_angle.hide()
            self.button_angle_input_angle.hide()

            self.angle_input_time.hide()
            self.button_angle_input_time.hide()

            self.angle_input_hight_start.hide()
            self.button_angle_input_hight_start.hide()

        except ValueError:
            print("[Log] Err: в ячейку подают строку")

    def save_val(self):
        print(var)