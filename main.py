import sys
balance = 0

def main():
    while True:
        try:
            print("************************************************************")
            print("1. Show Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            print("************************************************************")

            user_start = int(input("Welcome to the Bank Manager! Please select an Action above: "))

            if user_start == 1:
                print(show_balance())

            elif user_start == 2:
                deposit()

            elif user_start == 3:
                withdraw()

            elif user_start == 4:
                exiting()

            else:
                print("Invalid input! Please enter a number 1-4.")
                main()
        except ValueError:
            print("Invalid input! Please enter a number 1-4.")
            main()



def show_balance():
    print("**********************************")
    print(f"Your Bank Balance is {round(balance, 2)}.")
    print("**********************************")

    restarting()


def deposit():
    global balance
    try:
        dep_amount = float(input("How much would you like to deposit?: "))
        if dep_amount <= 0:
            print("Deposit amount must be greater than 0. Please try again.")
            deposit()
        else:
            dep_amount = round(dep_amount, 2)
            balance += dep_amount
            print(f"You have deposited {dep_amount:.2f} and your new balance is {balance:.2f}")
            restarting()
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        deposit()



def withdraw():
    global balance
    try:
        with_amount = float(input("How much would you like to withdraw? If you would like to go back enter 0: "))
        if with_amount < 0:
            print("Withdrawal amount must be greater than 0. Please try again.")
            withdraw()
        elif balance >= with_amount and with_amount!= 0:
            balance -= with_amount
            print(f"Withdrawal successful! Your new balance is: {balance:.2f}")
            restarting()

        elif with_amount == 0:
            main()
        else:
            print("Invalid Withdrawal Amount! Insufficient balance.")
            withdraw()
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        withdraw()


def exiting():
    print("Thanks for using the Bank Manager! Goodbye")
    sys.exit()




def restarting():
    try:
        restart = True

        while restart:
            restart_pro = int(input("Press 1 to return and select another action or press 2 to exit: "))
            if restart_pro == 1:
                restart = False
                main()
            elif restart_pro == 2:
                restart = False
                exiting()
            else:
                print("Sorry that is an invalid input please try again")
                restarting()
    except ValueError:
        print("Sorry that is an invalid input please try again")
        restarting()


main()


