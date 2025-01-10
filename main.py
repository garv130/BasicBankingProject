balance = 0

def main():
    print("************************************************************")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("************************************************************")
    user_select = input("Welcome to the Bank Manager! Please select an Action above: ")

    if user_select == 1:
        print(show_balance())

    elif user_select == 2:
        pass


def show_balance():
    print("**********************************")
    print(f"Your Balance is {round(balance, 2)}.")
    print("**********************************")


def deposit():
    pass

def withdraw():
    pass

def exiting():
    pass


main()

