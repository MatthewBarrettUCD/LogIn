import sys

usernames = []
dict_of_users = {}

class account:
    def __init__(self, name, password):
        self.name = name
        self.password = password
    
    def set_password(self, password):
        self.__password = password

def main():
    i = 4
    while i > 0:
        i -= 1
        login()
    exit

def login():
    loginchoice = input("What would you like to do? \n 1) Login to an existing account \n 2) Create a new account \n 3) Exit \nPlease enter a number: ")
    if loginchoice == "1":
        print("\nYou have chosen to log in to an existing account\n")
        existingaccount()
    elif loginchoice == "2":
        print("\nYou have chosen to create a new account")
        newaccount()
    elif loginchoice == "3":
        print("\nGoodbye!\n")
        sys.exit()
    else:
        print("Please pick a valid option \n")
        login()

def newaccount():
    while True:
        username = input("Please enter your username: ")
        if username not in usernames:
            usernames.append(username)
            break
        print("That username is already taken. Please try again.\n")

    while True:
        password1 = input("\nPlease enter your password: ")
        password2 = input("\nPlease enter your password again: ")

        if password1 == password2:
            break
        print("Your passwords must match, please try again.\n")

    username = account(username,password1)
    dict_of_users[username] = account(username,password1)
    mainbox(dict_of_users[username],password1)
    
def mainbox(name,password):
    while True:
        mainchoice = input("Welcome " + name.name + " what would you like to?\n 1) Print my username\n 2) Change my password\n 3) Logout\n")
        if mainchoice == "1":
            print(name.name)
            print("")
        elif mainchoice == "2":
            print("You have chosen to to change your password\n")

            while True:
                password1 = input("\nPlease enter your new password: ")
                password2 = input("\nPlease enter your new password again: ")

                if password1 == password2:
                    break
                print("Your passwords must match, please try again.\n")

            name.set_password(password1)

        elif mainchoice == "3":
            print("Thank you, goodbye!\n")
            break
        else:
            print("Please pick a valid option \n")

def existingaccount():
    while True:
        while True:
            username = input("Please enter your username: \n")
            if username not in dict_of_users:
                break
        password = input("Please enter your password: \n")
        if dict_of_users[username].name == dict_of_users[username].password:
            break
        else:
            print("Wrong username or password, please try again\n")
    mainbox(dict_of_users[username],password)

    

main()