#! /usr/bin/python3 python3
#
# Above is called a shebang. The path is for unix based OS
# and python3 is the executable when not on unix based OS
#
# Prompt user to login or make an account and login
# Program then stores user details so they can login again

def login():
    user_check = input("Enter Username: ")
    password_check = input("Enter password: ")
    acc_check_file_name = str(user_check) + ".txt"
    acc_check = open(acc_check_file_name, "r")
    acc_check_data = acc_check.read()
    acc_check_arr = acc_check_data.split("\n")
    user_file_ref = acc_check_arr[0]
    pass_file_ref = acc_check_arr[1]

    if user_check == user_file_ref and password_check == pass_file_ref:
        print("Congrats you logged in :^)")
    else:
        incorrect_login = (
            input("Oh no looks like your details are wrong, try again?: "))
        if incorrect_login in ["Yes", "yes"]:
            login()
        elif incorrect_login in ["No", "no"]:
            print('Okay seeya next time uwu')
        # This case was not handled. Don't leave a conditional hanging
        # because it will be the bug you find out later on
        else:
            print('Bruv, speak english bubs')

    acc_check.close()


def make_acc():
    new_user = input("Enter new username: ")
    new_user_pass = input("Enter new password: ")
    new_user_pass_confirm = input("Confirm new password: ")
    acc_file_name = str(new_user) + ".txt"
    if new_user_pass != new_user_pass_confirm:
        make_acc()
    elif new_user_pass == new_user_pass_confirm:
        acc_file = open(acc_file_name, "w")
        acc_file.write("%s" % new_user + "\n%s" % new_user_pass)
        acc_file.close()
        print("Your details have been stored, you may now login")
        login()


# Where applicable, define functions before they're used.
# This was at the top, is now towards the bottom.
# The exception is when two functions reference each other (recursion)
def have_acc():
    have_account = input("Do you already have an account: ")
    if have_account in ["yes", "Yes"]:
        login()
    elif have_account in ["no", "No"]:
        make_acc()
    else:
        have_acc()


# Only calls the main function if this file is the executable.
#
# Libraries and modules usually don't have this,
# because their entry point SHOULD be functions and variables.
if __name__ == "__main__":
    have_acc()
