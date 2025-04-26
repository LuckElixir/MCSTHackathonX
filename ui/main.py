import PyQt6
import os
import numpy
import matplotlib.pyplot as plt
import sys
from login import Login
sys.path.append("../")
import filesave.main as fs
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

class initWindow(QMainWindow):
    def __init__(self, font)-> None:
        super().__init__()
        self.setWindowTitle("The Anti-Procrastination App")
        self.font = font

    def checkSave(self):
        login = fs.checkLogin()
        if login:
            self.loginPage = Login(self)







# debug:
if __name__ == "__main__":
    print(os.getcwd())
    app = QApplication(sys.argv)
    window = initWindow("Times new roman")
    window.show()

    app.exec()
