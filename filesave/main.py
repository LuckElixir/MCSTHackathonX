import hashlib
import numpy
import os
global saveRows

def createFile():
    with open("filesave/savefile.txt", "w+") as savefile:
        savefile.write("")


def logOut():
    with open("filesave/savefile.txt", "w+") as savefile:
        savefile.write("")

def checkLogin():
    if not os.path.isfile("filesave/savefile.txt"):
        createFile()
    login: bool
    with open("filesave/savefile.txt", "r") as savefile:
        loginLine = savefile.readline()
        if loginLine != "1\n":
            login = False
        else:
            login = True

    return login

def getUsername():
    if not os.path.isfile("filesave/savefile.txt"):
        createFile()
    with open("filesave/savefile.txt", "r") as savefile:
        savefile.readline()
        username = savefile.readline()

    return username[:-1]

def login(username):
    replaceLine(0, "1")
    replaceLine(1, username)


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
            saveText = savefile.write(row + "\n")


def checkPassword(username: str, inputPassword):
    with open(f"filesave/{username}.txt", "r") as passwords:
        passwords = passwords.readline()

    encoded_string = inputPassword.encode('utf-8')

    # Using SHA-256
    hash_object = hashlib.sha256(encoded_string)
    hex_digest = hash_object.hexdigest()
    if (hex_digest + "\n") == passwords:
        return True
    return False


def createPassword(username: str, password: str):
    """
    Creates a password file for a given username and password.

    Args:
        username (str): The username for which to create the password file.
        password (str): The password to be hashed and stored in the file.

    Returns:
        None

    This function encodes the password using UTF-8 encoding, hashes it using SHA-256, and then writes the hashed value and a default value of 0 to a file named after the username in the "filesave" directory.
    """

    encoded_string = password.encode('utf-8')

    # Using SHA-256
    hash_object = hashlib.sha256(encoded_string)
    hex_digest = hash_object.hexdigest()
    with open(f"filesave/{username}.txt", "w") as passwords:
        passwords.write(hex_digest + "\n" + "0")


def getPoints(username):
    """
    Retrieves the points associated with a given username from the "filesave" directory.

    Args:
        username (str): The username for which to retrieve the points.

    Returns:
        int: The points associated with the given username.

    Raises:
        FileNotFoundError: If the file containing the points for the given username does not exist.
        ValueError: If the file contains less than two lines or the second line cannot be converted to an integer.
    """
    with open(f"filesave/{username}.txt", "r") as user:
        points = int(user.readlines()[1])

    return int(points)

def setPoints(username: str, newPoints: int):
    """
    Updates the points associated with a given username in the "filesave" directory.

    Args:
        username (str): The username for which to update the points.
        newPoints (int): The new points value to set for the given username.

    Returns:
        None

    Raises:
        FileNotFoundError: If the file containing the points for the given username does not exist.
        ValueError: If the file contains less than two lines or the second line cannot be converted to an integer.

    This function reads the first line of the file associated with the given username, hashes it using SHA-256, and then writes the hashed value followed by the new points value to the same file.
    """
    # Using SHA-256
    with open(f"filesave/{username}.txt", "r") as user:
        points = user.readlines()[0:1]

    encoded_string = points[0].encode('utf-8')

    # Using SHA-256
    hash_object = hashlib.sha256(encoded_string)
    hex_digest = hash_object.hexdigest()
    with open(f"filesave/{username}.txt", "w") as passwords:
        passwords.write(hex_digest + "\n" + str(newPoints))