from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMainWindow
from Resurces import res_rc

class Ui_Circle(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('Forms\\circle.ui', self)
