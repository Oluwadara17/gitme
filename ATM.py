# from ast import While
# import random
# from tkinter.messagebox import YES

  # INPUT CARD PHASE
account = 50000.00
Card = input("IS YOUR CARD INSERTED? ")
userCard = Card.lower()
if userCard == "yes":
    userName = str(input("WHAT IS YOUR NAME? "))
    userName2 = userName.upper()
    Pin = (input(f"Welcome {userName2}, ENTER YOUR FOUR-DIGIT PIN: "))
    userPin = int(Pin)
    userAction = int(input(f"WELCOME {userName2}! WHAT DO YOU WANT TO DO? (Withdraw(1) / Check Balance(2))/ Deposit(3)/ Transfer(4) "))


# USER ACTION PHASE

    if userAction == 1:
        withdrawal = float(input("HOW MUCH DO YOU WANT TO WITHDRAW? "))
        withdrawalConfirm= int(input(f"ARE YOU SURE YOU WANT TO WITHDRAW #{withdrawal:.2f} FROM YOUR ACCOUNT? (CONFIRM(1)/ REJECT(2)) "))
        # WITHDRAWAL

        if withdrawalConfirm == 1:
            if account <= 0:
                print("Insufficient Balance")
            else:
                print(f"WITHDRAWAL OF #{withdrawal:.2f} Successful!!!")
                account-=withdrawal
                newWithdraw = int(input(" WOULD YOU LIKE TO PERFORM ANOTHER TRANSACTION? YES(1) END(2) "))
                if newWithdraw == 1:
                    print("Please you have to,re-run the Programme Again")

                elif newWithdraw == 2:
                    print("REMOVE YOUR CARD PLEASE")

                else : print("INVALID NUMBER INPUTTED \n ReRUN THE PROGRAMME AGAIN")

        else:
            print("Transaction End Immediately")

    # CHECK BALANCE

    elif userAction == 2:
        print(f"YOUR BALANCE IS #{account:.2f}")
        newTrans = input("DO YOU WANT TO PERFORM ANOTHER TRANSACTION? YES(1) END(2) ")

        if newTrans == 1:
            print("Please you have to,re-run the Programme Again")

        elif newTrans == 2:
            print("PLEASE REMOVE YOUR CARD")

        else:
            print("INVALID number")


    #    Deposit
    elif userAction == 3:
        deposit = float(input(f"How much do you want to deposit "))
        name = input("Depositor name ")
        acct = input("Account number ")
        print(f"you have be credited {acct} a sum of  #{deposit:.2f} by {name} today ")
        account+=deposit
        newTrans = input("DO YOU WANT TO PERFORM ANOTHER TRANSACTION? YES(1) END(2) ")

        if newTrans == 1:
            print("Please you have to,re-run the Programme Again")

        elif newTrans == 2:
            print("PLEASE REMOVE YOUR CARD")

        else:
            print("INVALID Input")

    #         Transfer
    elif userAction == 4:
        Transfer = float(input(f"How much do you want to Transfer "))
        dan = input("Destination Account number ")
        account_name = input("Destination Account name ")
        if  account <= 0:
            print("Insufficient Balance")
        else:
            print(f"your transcation of {Transfer:.2f} to {dan} of the bearer {account_name} was successful ")

            account -= Transfer
            newTrans = int(input("DO YOU WANT TO PERFORM ANOTHER TRANSACTION? YES(1) END(2) "))

            if newTrans == 1:
                print(userAction)

            elif newTrans == 2:
                print("PLEASE REMOVE YOUR CARD")

            else:
                print("INVALID Input")

else :
    print("Please insert your card and re-run this programme again")