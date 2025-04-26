import ui.main
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from ui.main import initWindow
import sys

app = QApplication(sys.argv)
window = initWindow("Times new roman")
window.show()

app.exec()