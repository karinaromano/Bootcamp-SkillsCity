def withdrawMoney(pin, amount):
    userPin = "1234"
    userBalance = 100.00
    if pin == userPin:
        if amount < userBalance:
            userBalance = userBalance - amount
            print(f"£{amount:.2f} successfully withdrawn")
        else:
            print("Insufficient funds")
        print(f"Current balance: £{userBalance:.2f}")
    else:
        print("Incorrect PIN")

enteredPin = input("Please enter your PIN: ")
withdrawalAmount = float(input("Please enter an amount to withdraw: £"))
withdrawMoney(enteredPin, withdrawalAmount)