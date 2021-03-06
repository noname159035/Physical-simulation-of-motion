from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMainWindow
import matplotlib.pyplot as plt
from Resurces import res_rc
from metods import var
from metods import find_angle_x_t, find_angle_y_t
from count import final_count_angle


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
        '''Функция сохраняет начальную скорость в var'''
        try:
            var["angle_U_st"] = float(self.angle_input_speed_start.text())
            self.angle_input_speed_finish.hide()
            self.button_angle_input_speed_finish.hide()

        except ValueError:
            print("[Log] Err: в ячейку подают строку")

    def save_angle(self):
        '''Функция сохраняет угол, под которым тело начинает свое движение, в var'''
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
        '''Функция сохраняет время полета в var'''
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
        '''Функция сохраняет начальную в var'''
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
        '''Функция сохраняет конечную скорость в var'''
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
        '''Функция сохраняет высоту подъема в var'''
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
        '''Функция сохраняет длину пути в var'''
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
        '''Функция сохраняет время падения в var'''
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
        '''сохраняет все значения, запускает метод подсчёта, переходит на окно вывода расчётов'''
        final_count_angle()
        uic.loadUi('Forms\output_angle.ui', self)
        self.angle_out_speed_start.insert(str(var["angle_U_st"]))
        self.angle_out_angle.insert(str(var["angle_d"]))
        self.angle_out_time.insert(str(var["angle_t"]))
        self.angle_out_hight_start.insert(str(var["angle_h_st"]))
        self.angle_out_speed_fin.insert(str(var["angle_U_fin"]))
        self.angle_out_BigH.insert(str(var["angle_H"]))
        self.angle_out_len.insert(str(var["angle_L"]))
        self.angle_out_time_fall.insert(str(var["angle_t_fall"]))

        self.angle_show_graph.clicked.connect(self.get_graph)

    def get_graph(self):
        """генерирует и выводит график"""
        t = 0
        x, y = [], []
        while t < var["angle_t"]:
            x.append(find_angle_x_t(var["angle_U_st_x"], t))
            y.append(find_angle_y_t(var["angle_U_st_y"], t))
            t += 0.1

        plt.plot(x, y)
        plt.show()
