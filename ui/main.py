
import PyQt6
import os
import numpy
import matplotlib.pyplot as plt
import sys

from backend.main import Profile
from ui.login import Login
sys.path.append("../")
import filesave.main as fs
import ui.profile as profile
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from filesave.main import *

class initWindow(QMainWindow):
    def __init__(self, font)-> None:
        super().__init__()
        self.setWindowTitle("Grindify: Make Life a Game")
        self.font = font
        self.profile: Profile = None
        self.checkSave()

    def checkSave(self) -> None:
        login = fs.checkLogin()
        if not login:
            self.loginPage = Login(self)
        if login:
            self.override(getUsername())

    def override(self, username):
        self.profile = Profile(username, points=getPoints(username))
        self.profilePage = profile.HomePage(self)








