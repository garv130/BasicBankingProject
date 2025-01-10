balance = 0

def main():
    print("************************************************************")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("************************************************************")
    user_select = int(input("Welcome to the Bank Manager! Please select an Action above: "))

    if user_select == 1:
        print(show_balance())

    elif user_select == 2:
        deposit()


def show_balance():
    print("**********************************")
    print(f"Your Bank Balance is {round(balance, 2)}.")
    print("**********************************")
    #Create a ting that shows balance and asks if the user wants to do something else 
    main()


def deposit():
    global balance
    dep_amount = float(input("How much would you like to deposit?: "))
    dep_amount = round(dep_amount, 2)
    balance += dep_amount
    print(f"You have deposited {dep_amount} and your new Balance is {balance}")

    restart = True

    while restart:
        restart_pro = int(input("Press 1 to return and select another action or press 2 to exit: "))
        if restart == 1:
            restart = False
            main()
        elif restart == 2:
            restart = False
            exiting()
        else:
            print("Sorry that is an invalid input please try again")


def withdraw():
    pass

def exiting():
    pass


main()

