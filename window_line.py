from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMainWindow
from Resurces import res_rc
from metods import var
from count import final_count_line

SpeedStartIsVisible = True
SpeedFinishIsVisible = True
MovingInVisible = True

class Ui_Line(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('Forms\line.ui', self)
        self.button_line_input_speed_start.clicked.connect(self.save_speed_start)
        self.button_line_input_acceleration.clicked.connect(self.save_acceleration)
        self.button_line_input_mov.clicked.connect(self.save_mov)
        self.button_line_input_time.clicked.connect(self.save_time)
        self.button_line_input_speed_finish.clicked.connect(self.save_speed_finish)
        self.button_line_finish_input.clicked.connect(self.save_val)


    def save_speed_start(self):
        '''Функция сохраняет начальную скорость в var'''
        try:
            var["line_U_st"] = float(self.line_input_speed_start.text())
            global SpeedStartIsVisible
            SpeedStartIsVisible = False
            self.line_input_speed_finish.hide()
            self.button_line_input_speed_finish.hide()

            self.line_input_mov.hide()
            self.button_line_input_mov.hide()
        except ValueError:
            print("[Log] Err: в ячейку подают строку")


    def save_acceleration(self):
        '''Функция сохраняет ускорение в var'''
        try:
            var["line_a"] = float(self.line_input_acceleration.text())
            global SpeedFinishIsVisible, SpeedStartIsVisible, MovingInVisible
            if not(SpeedStartIsVisible):
                self.line_input_speed_finish.hide()
                self.button_line_input_speed_finish.hide()

                self.line_input_mov.hide()
                self.button_line_input_mov.hide()

            if not(SpeedFinishIsVisible):
                self.line_input_speed_start.hide()
                self.button_line_input_speed_start.hide()

                self.line_input_mov.hide()
                self.button_line_input_mov.hide()

            if not(MovingInVisible):
                self.line_input_speed_finish.hide()
                self.button_line_input_speed_finish.hide()

                self.line_input_speed_start.hide()
                self.button_line_input_speed_start.hide()
        except ValueError:
            print("[Log] Err: в ячейку подают строку")

    def save_time(self):
        '''Функция сохраняет время в var'''
        try:
            var["line_t"] = float(self.line_input_time.text())
            global SpeedFinishIsVisible, SpeedStartIsVisible, MovingInVisible
            if not(SpeedStartIsVisible):
                self.line_input_speed_finish.hide()
                self.button_line_input_speed_finish.hide()

                self.line_input_mov.hide()
                self.button_line_input_mov.hide()

            if not(SpeedFinishIsVisible):
                self.line_input_speed_start.hide()
                self.button_line_input_speed_start.hide()

                self.line_input_mov.hide()
                self.button_line_input_mov.hide()

            if not(MovingInVisible):
                self.line_input_speed_finish.hide()
                self.button_line_input_speed_finish.hide()

                self.line_input_speed_start.hide()
                self.button_line_input_speed_start.hide()
        except ValueError:
            print("[Log] Err: в ячейку подают строку")

    def save_speed_finish(self):
        '''Функция сохраняет конечную скорость в var'''
        try:
            global SpeedFinishIsVisible
            SpeedFinishIsVisible = False
            self.line_input_speed_start.hide()
            self.button_line_input_speed_start.hide()

            self.line_input_mov.hide()
            self.button_line_input_mov.hide()
        except ValueError:
            print("[Log] Err: в ячейку подают строку")

    def save_mov(self):
        '''Функция сохраняет пройденный путь в var'''
        try:
            global MovingInVisible
            MovingInVisible = False

            self.line_input_speed_start.hide()
            self.button_line_input_speed_start.hide()

            self.line_input_speed_finish.hide()
            self.button_line_input_speed_finish.hide()
        except ValueError:
            print("[Log] Err: в ячейку подают строку")

    def save_val(self):
        '''Функция сохраняет все значения, запускает метод подсчёта, переходит на окно вывода расчётов'''
        final_count_line()
        uic.loadUi('Forms\output_line.ui', self)
        self.line_out_speed_start.insert(str(var["line_U_st"]))
        self.line_out_mov.insert(str(var["line_S_mov"]))
        self.line_out_speed_fin.insert(str(var["line_U_fin"]))
        self.line_out_L.insert(str(var["line_L"]))