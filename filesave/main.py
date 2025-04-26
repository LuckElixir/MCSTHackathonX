import numpy
import os


def createFile():
    with open("filesave/savefile.txt", "w+") as savefile:
        savefile.write("")


def checkLogin():
    if not os.path.isfile("filesave/savefile.txt"):
        createFile()
    login: bool
    with open("filesave/savefile.txt", "r") as savefile:
        loginLine = savefile.readline(0)
        if loginLine != "1\n":
            login = False
        else:
            login = True

    return login


def login(username):
    replaceLine(0, "1\n")


def replaceLine(rowNum, new):
    with open("filesave/savefile.txt", "r") as savefile:
        saveText = savefile.read()

    saveRows = saveText.split("\n")
    try:
        saveRows[rowNum] = new
    except IndexError:
        saveRows.append(new)

    with open("filesave/savefile.txt", "w") as savefile:
        for row in saveRows:
            saveText = savefile.write(row)


def checkPassword(username: str, inputPassword):
    with open(f"filesave/{username}.txt", "r") as passwords:
        passwords = passwords.read()

    if str(hash(inputPassword)) == passwords:
        return True
    return False


def createPassword(username: str, password: str):
    with open(f"filesave/{username}.txt", "w") as passwords:
        passwords.write(str(hash(password)))
