from PyQt6.QtGui import QFont, QPixmap, QPainter, QColor, QBrush, QWindow, QImage
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLineEdit, QMessageBox
from PyQt6.QtWidgets import QGridLayout, QLabel
from PyQt6.QtCore import Qt, QRect
import PyQt6.QtGui as QtGui, PyQt6.QtCore as QtCore
from PIL import Image, ImageDraw
from PIL.ImageQt import ImageQt
from filesave.main import *



class Login(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main : QMainWindow = main
        self.loginLayout = QGridLayout()
        self._generateLoginPage()
        self._updateMain()

    def _generateLoginPage(self):
        self.loginLayout.setContentsMargins(5, 0, 0, 0)
        loginText = QLabel()
        loginFont = QFont("VCR OSD Mono")
        loginFont.setPointSize(48)
        loginText.setText("Not Enough Time")
        loginText.setFont(loginFont)
        loginText.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        loginButton = QPushButton("Log In")
        loginButton.setFont(QFont("VCR OSD Mono", 32))


        signUpButton = QPushButton("Sign Up")
        signUpButton.setFont(QFont("VCR OSD Mono", 32))


        loginButton.clicked.connect(self._login)
        signUpButton.clicked.connect(self._signup)

        self.loginLayout.addWidget(loginText, 0, 0, 1, 3)
        self.loginLayout.addWidget(loginButton, 1, 0, 1, 3)
        self.loginLayout.addWidget(signUpButton, 2, 0, 1, 3)
        pixmap = QtGui.QPixmap.fromImage(QImage("images/loginImage.jpg"))
        ilabel = QLabel()

        ilabel.setPixmap(pixmap)
        ilabel.setScaledContents(True)
        self.loginLayout.addWidget(ilabel, 0, 3, 5, 8)
        self.loginLayout.setRowStretch(0, 2)
        self.loginLayout.setRowStretch(1, 1)
        self.loginLayout.setRowStretch(2, 1)
        self.loginLayout.setColumnStretch(3, 1)

    def _login(self):
        self.loginLayout = QGridLayout()
        self.loginLayout.setContentsMargins(5, 0, 0, 0)

        label_name = QLabel('<font size="4"> Username: </font>')
        label_name.setFont(QFont("Consolas", 24))
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter your username')
        self.lineEdit_username.setFixedSize(200, 50)
        self.loginLayout.addWidget(label_name, 1, 0, 1, 2)
        self.loginLayout.addWidget(self.lineEdit_username, 1, 2, 1, 2)

        label_password = QLabel('<font size="4"> Password: </font>')
        label_password.setFont(QFont("Consolas", 24))
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit_password.setPlaceholderText('Please enter your password')
        self.lineEdit_password.setFixedSize(200, 50)
        self.loginLayout.addWidget(label_password, 2, 0, 1, 2)
        self.loginLayout.addWidget(self.lineEdit_password, 2, 2, 1, 2)

        button_login = QPushButton('Login')
        button_login.setFixedSize(200, 50)
        button_login.setFont(QFont("Consolas", 24))
        button_login.clicked.connect(self._checkPassword)
        self.loginLayout.addWidget(button_login, 3, 1, 1, 5)

        pixmap = QtGui.QPixmap.fromImage(QImage("images/loginImage.jpg"))
        ilabel = QLabel()

        ilabel.setPixmap(pixmap)
        ilabel.setScaledContents(True)
        self.loginLayout.addWidget(ilabel, 0, 4, 5, 8)

        self._updateMain()

    def _signup(self):
        self.loginLayout = QGridLayout()
        self.loginLayout.setContentsMargins(5, 0, 0, 0)

        label_name = QLabel('<font size="4"> Username: </font>')
        label_name.setFont(QFont("Consolas", 24))
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter your username')
        self.lineEdit_username.setFixedSize(200, 50)
        self.loginLayout.addWidget(label_name, 1, 0, 1, 2)
        self.loginLayout.addWidget(self.lineEdit_username, 1, 2, 1, 2)

        label_password = QLabel('<font size="4"> Password: </font>')
        label_password.setFont(QFont("Consolas", 24))
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Please enter your password')
        self.lineEdit_password.setFixedSize(200, 50)
        self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.loginLayout.addWidget(label_password, 2, 0, 1, 2)
        self.loginLayout.addWidget(self.lineEdit_password, 2, 2, 1, 2)

        label_confirm_password = QLabel('<font size="4"> Confirm Password: </font>')
        label_confirm_password.setFont(QFont("Consolas", 24))
        self.lineEdit_confirm_password = QLineEdit()
        self.lineEdit_confirm_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit_confirm_password.setPlaceholderText('Please confirm your password')
        self.lineEdit_confirm_password.setFixedSize(200, 50)
        self.loginLayout.addWidget(label_confirm_password, 3, 0, 1, 2)
        self.loginLayout.addWidget(self.lineEdit_confirm_password, 3, 2, 1, 2)

        button_signup = QPushButton('Sign Up')
        button_signup.setFixedSize(200, 50)
        button_signup.setFont(QFont("Consolas", 24))
        button_signup.clicked.connect(self._createAccount)
        self.loginLayout.addWidget(button_signup, 4, 1, 1, 5)

        pixmap = QtGui.QPixmap.fromImage(QImage("images/loginImage.jpg"))
        ilabel = QLabel()

        ilabel.setPixmap(pixmap)
        ilabel.setScaledContents(True)
        self.loginLayout.addWidget(ilabel, 0, 4, 7, 8)

        self._updateMain()


    def _createAccount(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        confirm_password = self.lineEdit_confirm_password.text()

        if password != confirm_password:
            msg = QMessageBox()
            msg.setText('Passwords do not match')
            msg.exec_()
            return

        createPassword(username, password)

        msg = QMessageBox()
        msg.setText('Account created successfully')
        msg.exec_()

        login(username=self.lineEdit_username)

    def _checkPassword(self):
        msg = QMessageBox()
        if checkPassword(self.lineEdit_username.text(), self.lineEdit_password.text()):
            msg.setText('Success')
            msg.exec_()
        else:
            msg.setText('Incorrect Password')
            msg.exec_()

        login(username=self.lineEdit_username)

    def _updateMain(self):
        updateWidget = QWidget()
        updateWidget.setLayout(self.loginLayout)
        self.main.setCentralWidget(updateWidget)



