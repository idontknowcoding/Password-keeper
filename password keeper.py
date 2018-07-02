
#This program lets you store and create passwords

import random
import shelve




print("Welcome to the account saver!")


def random_password():
    """Creates a new random password"""
    print('\n')
    account = input("Account: ")
    username = input("Username: ")
    digits_in_pass = input("Length of password: ")
    while not digits_in_pass.isdigit():
        print( "Incorrect input!")
        digits_in_pass = input("Length of password: ")
    password = gen_password(int(digits_in_pass))
    entry = finish_new_account(account, password, username)
    print( entry + '\n')


def manual_input():
    """Manually input a password"""
    print('\n')
    account = input("Account: ")
    username = input("Username: ")
    password = input("Password: ")
    entry = finish_new_account(account, password, username)
    print( entry + '\n')


def find_account():
    """Find an existing account"""
    print( '\n')
    search = input("For which account are you searching: ")
    f = shelve.open("accounts.dat")
    if search in f:
        account = f[search]
        print( account)
    else:
        print( "I'm sorry we could not find any account related to " + search)
    print( '\n')
    f.close()


def finish_new_account(account, password, username):
    """Sends entry to save() and returns a message"""
    entry = create_entry(account, password, username)
    save(account, entry)
    return "Save successful. " + "\n" + str(entry) + "\n"


def create_entry(account, password, username):
    """Creates the entry"""
    return "Account: " + account + " - Username: " + username + " - Password: " + password


def save(account, entry):
    """Saves account"""
    f = shelve.open("accounts.dat")
    saves = [entry]
    f[account] = saves
    f.sync()
    f.close()


def delete_account():
    """Deletes an account"""
    print('\n')
    account = input("What account do you want to delete?: ")
    f = shelve.open("accounts.dat")
    if account in f:
        confirm_deletion = input("Are you sure you want to delete " + account + "?: ")
        if confirm_deletion.lower() in ('yes', 'y'):
            del f[account]
            print( "This account has been deleted.")
        else:
            print( "Canceled... ")
    else:
        print( "I'm sorry we could not find any account related to " + account)
    print( '\n')
    f.close


def all_accounts():
    """print(s all accounts: A hidden command"""
    f = shelve.open("accounts.dat")
    klist = f.keys()
    f.close()
    print( klist)
    print( "\n")


def gen_password(digits_in_pass):
    """Returns a randomly generated password"""
    alphanumeric_chars = ["0123456789",
                          "abcdefghijklmnopqrstuvwxyz",
                          "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    return make_password(digits_in_pass, *alphanumeric_chars)


def make_password(length, *collections_of_characters):
    """Creates a random password"""
    characters = set()
    for collection in collections_of_characters:
        characters.update(str(c) for c in collection)
    characters = list(characters)

    password = [random.choice(characters) for _ in range(0, length)]
    return "".join(password)


def program_start():
    """MAIN"""
    choice = ''
    while choice != "5":
        choice = input("""Press 1 to manually input an account
Press 2 to generate a password
Press 3 to search for an existing account
Press 4 to delete an account
Press 5 to exit
""")
        if choice == "1":
            manual_input()
        elif choice == "2":
            random_password()
        elif choice == "3":
            find_account()
        elif choice == "4":
            delete_account()
        elif choice == "all accounts":
            all_accounts()
        else:
            print( " ")
program_start()
