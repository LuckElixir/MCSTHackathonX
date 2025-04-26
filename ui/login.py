from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtWidgets import QGridLayout


class Login(QWidget):
    def __init__(self, main):
        self.main = main
        self.generateLoginPage()
        self.loginLayout = QGridLayout()

    def generateLoginPage(self):
        pass
