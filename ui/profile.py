from PyQt6.QtGui import QFont, QPixmap, QPainter, QColor, QBrush, QWindow, QImage
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLineEdit, QMessageBox
from PyQt6.QtWidgets import QGridLayout, QLabel
from PyQt6.QtCore import Qt, QRect
import PyQt6.QtGui as QtGui, PyQt6.QtCore as QtCore
from PIL import Image, ImageDraw
from PIL.ImageQt import ImageQt
from filesave.main import *

class Profile(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main : QMainWindow = main
        self.profileLayout = QGridLayout()
        self._generateMainPage()
        self._updateMain()

    def _updateMain(self):
        updateWidget = QWidget()
        updateWidget.setLayout(self.profileLayout)
        self.main.setCentralWidget(updateWidget)

    def _generateMainPage(self):
        pass
