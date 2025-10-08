import json
import re
import random
import time


class Site:
    def __init__(self):
        # Main loop flag
        self.running = True
        # Load data from JSON (if exists)
        self.data = self.load_data()

    def menu(self):
        """Show main menu and validate selection."""
        def validate(choice):
            if re.search("[^1-3]", choice):
                raise Exception("Please enter a value between 1 and 3")
            elif len(choice) != 1:
                raise Exception("Please enter a value between 1 and 3")

        while True:
            try:
                choice = input(
                    "\nHello. Welcome to the Beydan Site.\n\nPlease select the operation you want to perform...\n\n[1]- Login\n[2]- Register\n[3]- Exit\n\n"
                )
                validate(choice)
            except Exception as err:
                print("{}".format(err))
                time.sleep(3)
            else:
                break
        return choice

    def program(self):
        choice = self.menu()

        if choice == "1":
            print("\nRedirecting to login menu")
            for i in range(5):
                print(".", end="", flush=True)
                time.sleep(.5)
            time.sleep(.7)
            self.login()

        if choice == "2":
            print("\nRedirecting to registration menu")
            for i in range(5):
                print(".", end="", flush=True)
                time.sleep(.5)
            time.sleep(.7)
            self.register()

        if choice == "3":
            print("\nExiting")
            for i in range(5):
                print(".", end="", flush=True)
                time.sleep(.5)
            time.sleep(.7)
            self.exit_program()

    # ----- Login flow -----
    def login(self):
        while True:
            username = input("\nPlease enter a username: ")
            password = input("Please enter your password: ")

            result = self.login_check(username, password)

            if result is True:
                self.login_successful()
                break

            else:
                self.login_failed()
                break

    def login_check(self, username, password):
        """Check provided credentials against stored data."""
        try:
            self.data = self.load_data()
            users = self.data["Users"]  # May raise KeyError if structure not present

            for user in users:
                if user["username"] == username and user["password"] == password:
                    return True

        except KeyError:
            print("No users found in the database.")

        return False

    def login_successful(self):
        print("\nVerifying login")
        for i in range(5):
            print(".", end="", flush=True)
            time.sleep(.5)
        print("\nWelcome to the JSON Database")
        time.sleep(.7)
        # Stop the main loop and set result flag
        self.result = False
        self.running = False

    def login_failed(self):
        print("\nVerifying login")
        for i in range(5):
            print(".", end="", flush=True)
            time.sleep(.5)
        time.sleep(.7)
        print("\nLogin failed")
        time.sleep(2)

        while True:
            register_choice = input(
                "\nWe couldn't find an account with the provided details. Don't have an account?\nRegister - [1]\nGo back to main menu - [2]\n"
            )
            if register_choice == "1":
                print("\nRedirecting to registration menu...")
                for i in range(5):
                    print(".", end="", flush=True)
                    time.sleep(.5)
                time.sleep(.7)
                self.register()
                return
            elif register_choice == "2":
                print("\nReturning to main menu...")
                for i in range(5):
                    print(".", end="", flush=True)
                    time.sleep(.5)
                time.sleep(.7)
                return
            else:
                print("Please enter a valid selection.")

    # ----- Registration flow -----
    def register(self):
        def validate_username(username):
            if len(username) < 8:
                raise Exception("Your username must be at least 8 characters long")
            if not username.isalpha():
                raise Exception("Your username must consist of letters only")

        while True:
            try:
                username = input("\nPlease enter a username: ")
                validate_username(username)
            except Exception as err:
                print(err)
            else:
                break

        def validate_password(password):
            birth_year = "2005"
            special_chars_regex = r"[\\@€\+\*\?!]"

            if len(password) < 8:
                raise Exception("Your password must be at least 8 characters long")
            elif not re.search("[a-z]", password):
                raise Exception("Password must contain at least one lowercase letter")
            elif not re.search("[0-9]", password):
                raise Exception("Password must contain at least one digit")
            elif not re.search(special_chars_regex, password):
                raise Exception("Password must contain at least one special character (e.g. @, €, +, *, ?, !)")
            elif not re.search("[A-Z]", password):
                raise Exception("Password must contain at least one uppercase letter")
            elif re.search(birth_year, password):
                raise Exception("You cannot include your birth year in the password")

        while True:
            try:
                password = input("\nPlease enter a password: ")
                validate_password(password)
            except Exception as err:
                print(err)
            else:
                break

        def validate_email(email):
            if not ("@gmail.com" in email or "@hotmail.com" in email):
                raise Exception("Your email must include '@gmail.com' or '@hotmail.com'")

        while True:
            try:
                email = input("\nPlease enter your email: ")
                validate_email(email)
            except Exception as err:
                print(err)
            else:
                break

        email_exists = self.email_exists(email)
        if email_exists == False:

            username_exists = self.username_exists(username)
            if username_exists == False:

                activation_code = self.send_activation()
                activated = self.activation_check(activation_code)
                while True:
                    if activated == True:
                        self.save_data(username, password, email)
                        print("\n-- Your account has been created --")
                        time.sleep(3)
                        return

                    else:
                        print("Your activation code is incorrect")
                        time.sleep(5)
                        return
            else:
                print("\nThis username is already taken...")
        else:
            print("\nThis email is already in use...")

    def email_exists(self, email):
        self.data = self.load_data()

        try:
            for e in self.data["Users"]:
                if e["email"] == email:
                    return True
        except KeyError:
            return False
        return False

    def username_exists(self, username):
        self.data = self.load_data()

        try:
            for u in self.data["Users"]:
                if u["username"] == username:
                    return True
        except KeyError:
            return False
        return False

    def send_activation(self):
        # Simulated activation code sending. No real email is sent.
        with open("C:/Users/user/Desktop/Activation.txt", "w", encoding="utf8") as f:
            activation = str(random.randint(10000, 99999))
            f.write("Your activation code:" + activation)

        return activation

    def activation_check(self, activation):
        entered = input("\nPlease enter the activation code that was sent to your email: ")
        if activation == entered:
            return True

        else:
            return False

    def load_data(self):
        try:
            with open("C:/Users/user/Desktop/Users.json", "r", encoding="utf8") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open("C:/Users/user/Desktop/Users.json", "w", encoding="utf8") as f:
                f.write("{}")
            with open("C:/Users/user/Desktop/Users.json", "r", encoding="utf8") as f:
                data = json.load(f)
        return data

    def save_data(self, username, password, email):
        self.data = self.load_data()
        try:
            self.data["Users"].append({"username": username, "password": password, "email": email})
        except KeyError:
            self.data["Users"] = list()
            self.data["Users"].append({"username": username, "password": password, "email": email})

        with open("C:/Users/user/Desktop/Users.json", "w", encoding="utf8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)  

    def exit_program(self):
        print("Exiting site...")
        time.sleep(3)
        self.running = False
        exit()


if __name__ == "__main__":
    system = Site()
    while system.running:
        system.program()
