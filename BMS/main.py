from register import *
from bank import *
from database import *

status = False

print("Welcome to Swiss Bank.....")
while True:
    try:
        register = int(input("1. SignUp\n"
                             "2. SignIn"))
        if register == 1 or register == 2:
            if register == 1:
                SignUp()
            if register == 2:
                user = SignIn()
                status = True
                break
        else:
            print("Please select from options only.")
            continue

    except ValueError:
        print("Sorry!!! Not Available...")


account_number = db_query(f"SELECT account_number FROM customers WHERE username = '{username}';")

while status:
    print(f"Welcome {usernamne.capitalize()} Choose Your Banking Service\n")

    try:
        facility = int(input("1. Balance Enquiry\n"
                             "2. Cash Deposit\n"
                             "3. Cash Withdraw\n"
                             "4. Fund Transfer\n "
                             ))

        if 1 <= facility <= 4:
            if facility == 1:
                bobj = Bank(username, account_number[0][0])
                bobj.balanceequiry()
            elif facility == 2:
                while True:
                    try:
                        amount = int(input("Enter Amount to Deposit"))
                        bobj = Bank(username, account_number[0][0])
                        bobj.deposit(amount)
                        mydb.commit()
                        status = False
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue

            elif facility == 3:
                while True:
                    try:
                        amount = int(input("Enter Amount to Withdraw"))
                        bobj = Bank(username, account_number[0][0])
                        bobj.withdraw(amount)
                        mydb.commit()
                        status = False

                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue
            elif facility == 4:
                while True:
                    try:
                        receive = int(input("Enter Receiver Account Number"))
                        amount = int(input("Enter Money to Transfer"))
                        bobj = Bank(username, account_number[0][0])
                        bobj.fundtransfer(receive, amount)
                        mydb.commit()
                        status = False
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue
            else:
                print("Please Enter Valid Input From Options")
                continue

    except ValueError:
        print("Invalid Input Try Again with Numbers")
        continue

cursor.close()