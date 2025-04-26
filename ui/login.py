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
        self.main = main
        self.loginLayout = QGridLayout()
        self._generateLoginPage()
        self._updateMain()

    def _generateLoginPage(self):
        """
        Generates the login page for the application.

        This function sets the contents margins of the login layout to 5 pixels on the top and 0 pixels on the left and right.
        It creates a QLabel widget with the text "Not Enough Time" and a font size of 48 pixels.
        The text is aligned horizontally and vertically at the center.
        It creates two QPushButton widgets with the labels "Log In" and "Sign Up", respectively.
        The font size of the buttons is set to 32 pixels.
        The clicked signals of the login button and sign up button are connected to the _login and _signup methods, respectively.
        The QLabel and QPushButton widgets are added to the login layout at specific positions.
        A QPixmap object is created from an image file named "images/loginImage.jpg".
        A QLabel widget is created and the QPixmap is set as the pixmap of the label.
        The label is set to scale its contents to fit the size of the widget.
        The QLabel widget is added to the login layout at specific positions.
        The row stretch factors for rows 0, 1, and 2 are set to 2, 1, and 1, respectively.
        The column stretch factor for column 3 is set to 1.

        Parameters:
        - self: The instance of the class.

        Return:
        - None
        """
        self.loginLayout.setContentsMargins(5, 0, 0, 0)
        loginText = QLabel()
        loginFont = QFont("VCR OSD Mono")
        loginFont.setPointSize(48)
        loginText.setText("GRINDIFY")
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
        """
        Initializes the login layout for the user interface.

        This function sets up the login layout for the user interface. It creates a QGridLayout object and sets its contents margins to 5 pixels on the top and 0 pixels on the left and right. It then creates QLabel and QLineEdit widgets for the username and password fields, respectively. The font size of the labels is set to 24 pixels and the placeholder text for the username and password fields is set. The QLineEdit widgets are set to have a fixed size of 200x50 pixels. The QLabel and QLineEdit widgets are added to the login layout at specific positions. A QPushButton widget is created for the login button and its font size is set to 24 pixels. The clicked signal of the login button is connected to the _checkPassword method. A QPixmap object is created from an image file named "images/loginImage.jpg" and a QLabel widget is created. The QPixmap is set as the pixmap of the label and the label is set to scale its contents to fit the size of the widget. The QLabel widget is added to the login layout at specific positions. Finally, the _updateMain method is called.

        Parameters:
        - self: The instance of the class.

        Return:
        - None
        """
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
        """
        Initializes the signup layout for the user interface.

        This function sets up the signup layout for the user interface. It creates a QGridLayout object and sets its contents margins to 5 pixels on the top and 0 pixels on the left and right. It then creates QLabel and QLineEdit widgets for the username and password fields, respectively. The font size of the labels is set to 24 pixels and the placeholder text for the username and password fields is set. The QLineEdit widgets are set to have a fixed size of 200x50 pixels. The QLabel and QLineEdit widgets are added to the signup layout at specific positions. A QLabel is created for the confirm password field and its font size is set to 24 pixels. The QLineEdit widget for the confirm password field is set to have a fixed size of 200x50 pixels and its echo mode is set to password. The QLabel and QLineEdit widgets for the confirm password field are added to the signup layout at specific positions. A QPushButton widget is created for the signup button and its font size is set to 24 pixels. The clicked signal of the signup button is connected to the _createAccount method. A QPixmap object is created from an image file named "images/loginImage.jpg" and a QLabel widget is created. The QPixmap is set as the pixmap of the label and the label is set to scale its contents to fit the size of the widget. The QLabel widget is added to the signup layout at specific positions. Finally, the _updateMain method is called.

        Parameters:
        - self: The instance of the class.

        Return:
        - None
        """
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
        """
        Creates a new account for the user.

        This function retrieves the username, password, and confirm password from the corresponding QLineEdit widgets.
        If the password and confirm password do not match, a QMessageBox is displayed with the message 'Passwords do not match'.
        Otherwise, the `createPassword` function is called with the username and password as arguments.
        A QMessageBox is then displayed with the message 'Account created successfully'.
        The `login` function is called with the username as an argument.
        Finally, the `override` method of the `main` attribute of the current object is called.

        Parameters:
        - self: The instance of the class.

        Return:
        - None
        """
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        confirm_password = self.lineEdit_confirm_password.text()

        if password != confirm_password:
            msg = QMessageBox()
            msg.setText('Passwords do not match')
            msg.exec()
            return

        createPassword(username, password)

        msg = QMessageBox()
        msg.setText('Account created successfully')
        msg.exec()

        login(username=self.lineEdit_username.text())
        self.main.override(self.lineEdit_username.text())

    def _checkPassword(self):
        """
        Checks the password entered by the user and displays a QMessageBox accordingly.

        This function retrieves the username and password from the corresponding QLineEdit widgets.
        It then calls the `checkPassword` function with the username and password as arguments.
        If the password is correct, a QMessageBox with the text 'Success' is displayed.
        Otherwise, a QMessageBox with the text 'Incorrect Password' is displayed.
        After displaying the QMessageBox, the `login` function is called with the username as an argument.

        Parameters:
        - self: The instance of the class.

        Return:
        - None
        """
        msg = QMessageBox()
        if checkPassword(self.lineEdit_username.text(), self.lineEdit_password.text()):
            msg.setText('Success')
            msg.exec()
            self.main.override(self.lineEdit_username.text())
        else:
            msg.setText('Incorrect Password')
            msg.exec()

        login(username=self.lineEdit_username.text())


    def _updateMain(self):
        updateWidget = QWidget()
        updateWidget.setLayout(self.loginLayout)
        self.main.setCentralWidget(updateWidget)



