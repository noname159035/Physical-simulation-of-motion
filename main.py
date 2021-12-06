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