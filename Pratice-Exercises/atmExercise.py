
# Code ATM Machine

print("Welcome to BRBank")
trials = 3 # the number of times the user can enter a wrong pin
userPin = 1234
userBalance = 200.00

while trials != 0:
    pin = int(input("Please enter your 4 digit Pin Number: "))
    if pin != userPin:
        trials -=1
        print(f"wrong Pin Number. You have {trials} trials left.")
    else:
        userChoice = input("d -> Deposit, w -> Withdraw: or b -> Balance:  ")
        if userChoice == "d":
            userDeposit = float(input("Enter the amount you would like to deposit: "))
            userBalance += userDeposit
            print(f"You have deposited £{userDeposit:.2f} into your account. Your new balance is £{userBalance:.2f}")
            break
        elif userChoice == "w":
            userWithdraw = float(input("Enter the amount you would like to Withdraw: "))
            if userWithdraw > userBalance:
                print(f"Sorry, you cannot proceed, you have {userBalance:.2f} on your balance")
            else:
                userBalance -= userWithdraw
                print(f"You have been withdrawn £{userWithdraw:.2f} from your account. And your current balance is £{userBalance:.2f} ")
                break
        elif userChoice == "b":
            print(f"Your current balance is {userBalance:.2f} ")
            break
        else:
            print("You have choosen the wrong option, we are cancelling your operation.")
            break

              






