import PyQt6
import os
import numpy
import matplotlib.pyplot as plt
import sys
from ui.login import Login
sys.path.append("../")
import filesave.main as fs
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

class initWindow(QMainWindow):
    def __init__(self, font)-> None:
        super().__init__()
        self.setWindowTitle("The Anti-Procrastination App")
        self.font = font
        self.checkSave()

    def checkSave(self):
        login = fs.checkLogin()
        if not login:
            self.loginPage = Login(self)






