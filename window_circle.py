from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMainWindow
from Resurces import res_rc
from metods import var
from count import final_count_circle

WayIsVisible = True
RadiusIsVisible = True
TimeIsVisivle = True
AngleSpeedIsVisible = True


class Ui_Circle(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('Forms\circle.ui', self)
        self.button_circle_input_speed.clicked.connect(self.save_speed)
        self.button_circle_input_angle_speed.clicked.connect(self.save_angle_speed)
        self.button_circle_input_way.clicked.connect(self.save_way)
        self.button_circle_input_radius.clicked.connect(self.save_radius)
        self.button_circle_input_time.clicked.connect(self.save_time)
        self.button_circle_input_acceleration_start.clicked.connect(self.save_acceleration)
        self.button_circle_finish_input.clicked.connect(self.save_val)

    def save_speed(self):
        '''Функция сохраняет линейную скорость в var'''
        try:
            var["circle_U"] = float(self.circle_input_speed.text())
            self.circle_input_angle_speed.hide()
            self.button_circle_input_angle_speed.hide()

            self.circle_input_way.hide()
            self.button_circle_input_way.hide()

            self.circle_input_acceleration_start.hide()
            self.button_circle_input_acceleration_start.hide()
        except ValueError:
            print("[Log] Err: в ячейку подают строку")

    def save_angle_speed(self):
        '''Функция сохраняет угловую скорость в var'''
        try:
            global AngleSpeedIsVisible, WayIsVisible, TimeIsVisivle, RadiusIsVisible
            var["circle_w"] = float(self.circle_input_angle_speed.text())
            self.circle_input_speed.hide()
            self.button_circle_input_speed.hide()

            self.circle_input_acceleration_start.hide()
            self.button_circle_input_acceleration_start.hide()

            AngleSpeedIsVisible = False

            if not(WayIsVisible):
                self.circle_input_acceleration_start.hide()
                self.button_circle_input_acceleration_start.hide()
                self.circle_input_radius.hide()
                self.button_circle_input_radius.hide()

            elif not(TimeIsVisivle) and RadiusIsVisible:
                self.circle_input_radius.hide()
                self.button_circle_input_radius.hide()
        except ValueError:
            print("[Log] Err: в ячейку подают строку")

    def save_way(self):
        '''Функция сохраняет путь в var'''
        try:
            var["circle_S_way"] = float(self.circle_input_way.text())
            self.circle_input_speed.hide()
            self.button_circle_input_speed.hide()
            global WayIsVisible, RadiusIsVisible, TimeIsVisivle
            WayIsVisible = False


            if not(RadiusIsVisible):
                self.circle_input_angle_speed.hide()
                self.button_circle_input_angle_speed.hide()

                self.circle_input_time.hide()
                self.button_circle_input_time.hide()

            elif not(AngleSpeedIsVisible):
                self.circle_input_radius.hide()
                self.button_circle_input_radius.hide()

            elif not(TimeIsVisivle):
                self.circle_input_radius.hide()
                self.button_circle_input_radius.hide()
        except ValueError:
            print("[Log] Err: в ячейку подают строку")

    def save_radius(self):
        '''Функция сохраняет радиус в var'''
        try:
            print("YS")
            var["circle_R"] = float(self.circle_input_radius.text())
            global RadiusIsVisible
            RadiusIsVisible = False
            if not(WayIsVisible):
                self.circle_input_angle_speed.hide()
                self.button_circle_input_angle_speed.hide()

                self.circle_input_time.hide()
                self.button_circle_input_time()
            elif not(AngleSpeedIsVisible):
                self.circle_input_way.hide()
                self.button_circle_input_way.hide()

            elif not(TimeIsVisivle):
                self.circle_input_way.hide()
                self.button_circle_input_way.hide()
        except ValueError:
            print("[Log] Err: в ячейку подают строку")

    def save_time(self):
        '''Функция сохраняет время в var'''
        try:
            global TimeIsVisivle
            TimeIsVisivle = False
            var["circle_t"] = float(self.circle_input_time.text())
            self.circle_input_acceleration_start.hide()
            self.button_circle_input_acceleration_start.hide()

        except ValueError:
            print("[Log] Err: в ячейку подают строку")

    def save_acceleration(self):
        '''Функция сохраняет центростремительное ускорение в var'''
        try:
            var["circle_a_o"] = float(self.circle_input_acceleration_start.text())
            self.circle_input_time.hide()
            self.button_circle_input_time.hide()

            self.circle_input_angle_speed.hide()
            self.button_circle_input_angle_speed.hide()

            self.circle_input_speed.hide()
            self.button_circle_input_speed.hide()
        except ValueError:
            print("[Log] Err: в ячейку подают строку")

    def save_val(self):
        '''Функция сохраняет все значения, запускает метод подсчёта, переходит на окно вывода расчётов'''
        final_count_circle()
        uic.loadUi('Forms\output_circle.ui', self)
        self.circle_out_angle_speed.insert(str(var["circle_w"]))
        self.circle_out_speed.insert(str(var["circle_U"]))
        self.circle_out_del_way.insert(str(var["circle_delta_s"]))
        self.circle_out_T.insert(str(var["circle_T"]))
        self.circle_out_radius.insert(str(var["circle_R"]))
        self.circle_out_acceleration_start.insert(str(var["circle_a_o"]))
        self.circle_out_del_power.insert(str(var["circle_delta_f"]))

