import random
import string

USER_FILE = "user.txt"


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
            f.write(f"{username} {password}\n")
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


auth = Authentication(USER_FILE)

while True:
    mode = input("Menu:\n Press 1 to register new User:, Press 2 to Login, Press q to quit\n")
    if mode == "1":
        auth.register(input("Username: "), input("Password: "))

    if mode == "2":
        auth.login()

    if mode == "q":
        break
