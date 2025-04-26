from PyQt6.QtGui import QFont, QPixmap, QPainter, QColor, QBrush, QWindow, QImage
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLineEdit, QMessageBox, QListWidget, \
    QHBoxLayout, QListWidgetItem, QVBoxLayout, QFormLayout, QSpinBox
from PyQt6.QtWidgets import QGridLayout, QLabel
from PyQt6.QtCore import Qt, QRect
import PyQt6.QtGui as QtGui, PyQt6.QtCore as QtCore
from PIL import Image, ImageDraw
from PIL.ImageQt import ImageQt

import backend.main
from filesave.main import *


class HomePage(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.profileLayout = QGridLayout()
        self.profile = self.main.profile
        self._generateMainPage()
        self._updateMain()

    def _updateMain(self):
        updateWidget = QWidget()
        updateWidget.setLayout(self.profileLayout)
        self.main.setCentralWidget(None)
        self.main.setCentralWidget(updateWidget)


    def _addNewTask(self):
        # Create a new window for adding a new task
        window = QWidget()
        layout = QFormLayout()

        # Create input fields for task name, estimated number of hours, and estimated difficulty
        nameInput = QLineEdit()
        taskInput = QLineEdit()
        hoursInput = QSpinBox()
        hoursInput.setMinimum(1)
        difficultyInput = QSpinBox()
        difficultyInput.setMinimum(1)
        difficultyInput.setMaximum(3)

        # Add the input fields to the layout
        layout.addRow("Task Name:", nameInput)
        layout.addRow("Task Type:", taskInput)
        layout.addRow("Estimated Hours:", hoursInput)

        layout.addRow("Estimated Difficulty:", difficultyInput)

        # Create the save button
        saveButton = QPushButton("Save")
        saveButton.clicked.connect(
            lambda: self._saveNewTask(nameInput.text(), taskInput.text(), hoursInput.value(), difficultyInput.value(), window))
        layout.addRow(saveButton)

        # Set the layout for the new window
        window.setLayout(layout)
        window.show()

    def _saveNewTask(self, name, category, hours, difficulty, window):
        # Create a new task dictionary with the input values
        self.main.profile.addTask(name, category, difficulty, hours)

        # Close the new task window
        window.close()
        self._generateMainPage()
        self._updateMain()

    def _generateMainPage(self):
        # Create the account info layout
        accountInfoLayout = QVBoxLayout()
        # Create the account name label
        accountNameLabel = QLabel(f"<h2> Account Name: {self.main.profile.name} <\h2>")
        accountInfoLayout.addWidget(accountNameLabel)

        # Create the points label
        pointsLabel = QLabel(f"<h2> Points: {self.main.profile.points} <\h2>")
        accountInfoLayout.addWidget(pointsLabel)

        # Create the league label
        leagueLabel = QLabel(f"<h2> League: {self.main.profile.league} <\h2>")
        accountInfoLayout.addWidget(leagueLabel)

        # Create the sign out button
        signOutButton = QPushButton("Sign Out")
        signOutButton.clicked.connect(self._signOut)
        accountInfoLayout.addWidget(signOutButton)

        # Create the task list layout
        taskListLayout = QVBoxLayout()
        # Create the task list
        self.tasksList = QListWidget()
        for task in self.main.profile.tasks:
            item = QListWidgetItem(
                f"{task.name} - {task.type} - Effort: {task.effort} - Hours: {task.baseHours}")
            item.setFont(QFont("Consolas"))
            self.tasksList.addItem(item)

            # Create the remove button
            removeButton = QPushButton("Remove")
            removeButton.setFixedSize(50, 20)  # Set a fixed size for the button
            removeButton.clicked.connect(lambda _: self._removeTask(task))
            self.tasksList.setItemWidget(item, removeButton)

        taskListLayout.addWidget(self.tasksList)

        # Create the add task button
        addTaskButton = QPushButton("Add New Task")
        addTaskButton.clicked.connect(self._addNewTask)
        taskListLayout.addWidget(addTaskButton)

        # Create the main layout and add everything to it
        mainLayout = QHBoxLayout()
        mainLayout.addLayout(accountInfoLayout)
        mainLayout.addLayout(taskListLayout)

        self.profileLayout = mainLayout

    def _removeTask(self, task):
        self.main.profile.removeTask(task.name)
        self._generateMainPage()
        self._updateMain()

    def _signOut(self):
        logOut()
        self.main.checkSave()
