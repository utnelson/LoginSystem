import random
import string
from cryptography.fernet import Fernet

USER_FILE = "user.txt"


"""def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)"""


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def random_string(length):
    """ Generiert einen Random string mit bestimmter Anzahl Zeichen"""

    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for _ in range(length))
    return result_str


class Authentication:
    """ User System mit Register, Login Funktionen"""

    def __init__(self, file_path):
        self.file_path = file_path

    def register(self, username, password):
        """Neuen Nutzer regestrieren: Eingabe Name & Password"""

        with open(self.file_path, "a") as f:
            f.write(f"{username} {self.encrypt(password)}\n")
        print(f"{username} wurde erfolgreich angelegt!")

    def login(self):
        """ Eingabe der Login Daten"""

        username = input("Bitte Nutzernamen eingeben: ")
        pwd = input("Bitte Password eingeben: ")
        # Jede Zeile durchsuchen und in eine Liste splitten. Danach vergleich mit Eingabe daten
        for line in open(self.file_path, "r").readlines():
            login_info = line.split()
            if username == login_info[0] and pwd == login_info[1]:
                print("Login success")
                return True
        print("Login failed")
        return False

    def random_user(self, count):
        """ Fügt eine bestimmte Anzahl User an die Txt Datei"""

        for i in range(0, count):
            self.register(random_string(6), random_string(8))

    def encrypt(self, password):
        pwd = fer.encrypt(password.encode()).decode()
        # print(pwd)
        return pwd

    def decrypt(self):
        pass


auth = Authentication(USER_FILE)

while True:
    mode = input("Menu:\n Press 1 to register new User:, Press 2 to Login, Press q to , 3 for writing the key\n")
    if mode == "1":
        auth.register(input("Username: "), input("Password: "))

    if mode == "2":
        auth.login()

    if mode == "3":
        auth.encrypt("Test")

    if mode == "q":
        break
