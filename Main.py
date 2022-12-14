
#importing BankAccounts class
from BankAccounts import BankAccounts

##List of bank accounts
bankAccountsCollections=[]
#variable to store count of entered accounts
count=1

#function to open a new account
def opennewAccount():
    name=str(input("Please enter the name on the account: "))
    obj=BankAccounts(name)
    bankAccountsCollections.append(obj)
    global count
    count+=1

#function to close an account
def closeAccount():
    account_number=int(input("\nPlease enter the account number that you would like to close: "))
    global count
    try:
        for i in range(count):
            if bankAccountsCollections[i].getAccountNumber() == account_number:
                print("\nYou have chosen to eliminate the following Bank Account: ")
                bankAccountsCollections[i].display()
                bankAccountsCollections.remove(bankAccountsCollections[i])
                count -= 1
                break


    except  ValueError as ve:
#This allows me to print out the type of exeption the program may experience
        print("Please enter a valid account number containing only numbers.")
    except IndexError as e:
        print("That bank account does not exist.")

#function to display an account details
def displayAccountDetails():

    global count
    try:
        account_number = int(input("Please enter the account number for which you'd like to display its details: "))
        for i in range(count):
            if bankAccountsCollections[i].getAccountNumber() == account_number:
                print("\nThe Account Details for the selected bank account are: ")
                bankAccountsCollections[i].display()
                break


    except  ValueError as ve:
        print("Please enter a valid account number containing only numbers.")
    except IndexError as e:
        print("That bank account does not exist.")

#function to deposit  an amount by asking the user to input an account number in which to make the deposit
def depositAmount():

    global count
    try:
# then inside a for loop I traverse my bank account list and compare the bank # entered with the ones stored in the list
# if there is a match, I display that account info and ask for the amount to be deposited into it
        account_number = int(input("Please enter the account number for which you'd like to to make a deposit: "))
        for i in range(count):
            if bankAccountsCollections[i].getAccountNumber() == account_number:
                print("\nThe Account Details for the selected bank account are: ")
                bankAccountsCollections[i].display()
                amount = int(input("\nPlease enter the amount that you'd like to deposit: "))
                if(amount>0):
                    bankAccountsCollections[i].addAmount(amount)
                else:
                    print("\nThe amount to be deposited must be greater than 0!")
                break


    except  ValueError as ve:
        print("Please enter a valid account number containing only numbers.")
    except IndexError as e:
        print("That bank account does not exist.")


#function to withdraw an amount by asking the user to input an account number from which to withdraw
def withdrawAmount():

    global count
    try:
# then inside a for loop I traverse my bank account list and compare the bank # entered with the ones stored in the list
# if there is a match, I display that account info and ask for the amount to be withdrawn
        account_number = int(input("Please enter the account number for which you'd like to make a withdraw: "))
        for i in range(count):
            if bankAccountsCollections[i].getAccountNumber() == account_number:
                print("\nThe Account Details for the selected bank account are: ")
                bankAccountsCollections[i].display()
                amount = int(input("\nPlease enter the amount that you'd like to withdraw: "))
                if(amount>0):
                    bankAccountsCollections[i].withdrawAmount(amount)
                else:
                    print("\nThe amount to be withdrawn must be greater than 0!")
                break


    except  ValueError as ve:
        print("Please enter a valid account number containing only numbers.")
    except IndexError as e:
        print("That bank account does not exist.")

#main function to be called from main containing the menu displaying the different choices for the user
def main():

    option=0
    while True:
        try:
            option = int(input("Welcome to the Banking System. Please select one of the following options: "
                           "\n1)Open new account "
                           "\n2)Close an account "
                           "\n3)Display all account details "
                           "\n4)Deposit an amount "
                           "\n5)Withdraw an amount "
                           "\n6)Exit "
                           ))

            if (option == 1):
                opennewAccount()
            elif (option == 2):
                closeAccount()
            elif (option == 3):
                displayAccountDetails()
            elif (option == 4):
                depositAmount()
            elif (option == 5):
                withdrawAmount()
            elif (option == 6):
                break
            else:
                print("Please enter one of the available choices!")
        except  ValueError as ve:
            print("Please enter a valid account number containing only numbers.")
        except IndexError as e:
            print("That bank account does not exist.")


if __name__ == "__main__":
    main()

