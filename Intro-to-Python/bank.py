acountbal = 50000
choice = input("Please enter 'b' to check balance or 'w' to withdraw: ")
while choice != 'q':
    if choice.lower() in ('w','b'):
        if choice.lower() == 'b':
            print("Your balance is: %d" % acountbal)
            print("Anything else?")
            choice = input("Enter b for balance, w to withdraw or q to quit 1: ")
            print(choice.lower())
        else:
            try:
                withdraw = float(input("Enter amount to withdraw: ").replace(',',''))
                if withdraw <= acountbal:
                    print("here is your: %.2f" % withdraw)
                    acountbal = acountbal - withdraw
                    print("Anything else?")
                    choice = input("Enter b for balance, w to withdraw or q to quit 2: ")
                    #choice = 'q'
                else:
                    print("You have insufficient funds: %.2f" % acountbal)
            except:
                print("Enter amount in digits")
    else:
        print("Wrong choice!")
        choice = input("Please enter 'b' to check balance or 'w' to withdraw: ")