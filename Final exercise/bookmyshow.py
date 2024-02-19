import json


class BookMyShow:

    def __init__(self):
        self.users = None
        self.users_file = 'user_data.json'
        self.load_users()

    def load_users(self):
        try:
            with open(self.users_file, 'r') as file:
                self.users = json.load(file)
        except FileNotFoundError:
            self.users = {'admin': {}, 'customer': {}}

    def save_users(self):
        with open(self.users_file, 'a') as file:
            json.dump(self.users, file)

    def sign_up(self, user_type):
        username = input("Enter username: ")
        password = input("Enter password: ")
        self.users[user_type][username] = password
        self.save_users()
        print("Sign up successful!")

    def sign_in(self, user_type):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in self.users[user_type] and self.users[user_type][username] == password:
            print("Sign in successful!")
        else:
            print("Invalid username or password")

    # @staticmethod
    # def admin_menu():
    #     print("Welcome Admin!")
    #
    # @staticmethod
    # def customer_menu():
    #     print("Welcome Customer!")

    def menu(self):
        while True:
            print("Welcome to BookMyShow!")
            print("1. Sign up")
            print("2. Sign in")
            print("3. Admin sign in")
            print("4. Customer sign in")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                user_type = input("Enter user type (admin/customer): ")
                self.sign_up(user_type)
            elif choice == '2':
                user_type = input("Enter user type (admin/customer): ")
                self.sign_in(user_type)
            elif choice == '3':
                self.sign_in('admin')
            elif choice == '4':
                self.sign_in('customer')
            elif choice == '5':
                print("Thank you for using BookMyShow!")
                break
            else:
                print("Invalid choice. Please try again.")


book_my_show = BookMyShow()
book_my_show.menu()




