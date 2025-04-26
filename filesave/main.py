import numpy

def createFile():
    with open("savefile.txt", "w+") as savefile:
        savefile.write("")

def checkLogin():
    login: bool
    with open("savefile.txt", "r") as savefile:
        loginLine = savefile.readline(0)
        if loginLine != "1\n":
            login = False
        else:
            login = True

    return login

def replaceLine(rowNum, new):

    with open("savefile.txt", "r") as savefile:
        saveText = savefile.read()

    saveRows = saveText.split("\n")
    saveRows[rowNum] = new

    with open("savefile.txt", "w") as savefile:
        for row in saveRows:
            saveText = savefile.write(row)

    
