# user registration signin and signup

from database import *
import random
from customer import *
from bank import Bank

def SignUp():
    username = input("Create Username: ")
    temp = db_query(f"SELECT username FROM customers where username ='{username}'")
    if temp:
        print("Username already exists.")
        SignUp()

    else:
        print("Username created.Please proceed.")
        password = input("Enter Your Password: ")
        name = input("Enter Your Name: ")
        age = input("Enter Your Age: ")
        city = input("Enter Your City: ")
        while True:
            account_number = random.randint(10000000, 99999999)
            temp = db_query(f"SELECT account_number FROM customers WHERE account_number = '{account_number}';")
            if temp:
                continue
            else:
                print("Account Number: ",account_number)
                break

    cobj = Customer(username, password, name, age, city, account_number)
    cobj.createuser()
    bobj = Bank(username, account_number)
    bobj.create_transaction_table()

    SignUp()

def SignIn():
    username = input("Enter Username: ")
    temp = db_query(f"SELECT username FROM customers where username = '{username}';")
    if temp:
        while True:
            password = input(f"Welcome {username.capitalize()} !!..\nEnter Password: ")
            temp = db_query(f"SELECT password FROM customers where username = '{username}';")
            # print(temp[0][0])
            if temp[0][0] == password:
                print("Sign IN Successfully")
                return username
            else:
                print("Wrong Password. Try Again!!!")
                continue
    else:
        print("Enter Valid Username")
        SignIn()