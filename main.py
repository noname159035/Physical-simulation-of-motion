# Обозначение переменных
#
#движ по окружности
# circle_U - скорость
# circke_w - угловая сакорость
# circke_R - радиус
# circke_t - время
# circke_S_way - путь
# circke_a_o - нормальн ускорение
#
#линейное движ
#
# line_U_st - начальн скорость
# line_a - ускорение
# line_t - время
# line_U_fin - кончен скорость
# line_S_mov - перемещения
# line_L - путь
#
#под углом
#
# angle_U_st - начальн скорость
# angle_d - угол альфа
# angle_t - время
# angle_h_st - начальн высота
# angle_U_fin - конечн скорость
# angle_H - макс высота подъема
# angle_L - длинна пути (горизонтальн)
# angle_t_fall - время падения
#

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget

from window_circle import Ui_Circle
from window_line import Ui_Line
from window_angle import Ui_Angle




class MainWindow(QMainWindow):
    global window_main

    def __init__(self):
        super().__init__()
        uic.loadUi('Forms\\win_main.ui', self)
        self.choose_move1.clicked.connect(self.go_to_circle)
        self.choose_move2.clicked.connect(self.go_to_line)
        self.choose_move3.clicked.connect(self.go_to_angle)

    def go_to_circle(self):
        window_main.close()
        window_circle.show()

    def go_to_line(self):
        window_main.close()
        window_line.show()

    def go_to_angle(self):
        window_main.close()
        window_angle.show()


from Resurces import res_rc

if __name__ == '__main__':
    app = QApplication([])
    window_main = MainWindow()
    window_circle = Ui_Circle()
    window_line = Ui_Line()
    window_angle = Ui_Angle
    window_main.show()
    app.exec_()