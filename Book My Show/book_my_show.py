import json
from datetime import datetime, timedelta
import time
import code


class BookMyShow:

    def __init__(self):
        self.users = None
        self.ahead = None
        self.users_file = 'harshil_data.json'
        self.load_users()

    def load_users(self):
        try:
            with open(self.users_file, 'r') as file:
                self.users = json.load(file)
        except FileNotFoundError:
            self.users = {'admin': {}, 'customer': {}, 'movies': {}}

    def save_users(self):
        with open(self.users_file, 'w') as file:
            json.dump(self.users, file)

    def sign_up(self, user_type):
        username = input("Enter username: ").capitalize()
        password = input("Enter password: ")
        if user_type in self.users and username in self.users[user_type] and self.users[user_type][username] == password:
            print("User Already Exists!!")
        else:
            self.users[user_type][username] = password
            self.save_users()
            print("Sign up successful!")

    def sign_in(self, user_type):
        username = input("Enter username: ").capitalize()
        password = input("Enter password: ")
        if username in self.users[user_type] and self.users[user_type][username] == password:
            print("Sign in successful!")
            return True
        else:
            print("Invalid username or password")
            return False

    def menu(self):
        print("Welcome to BookMyShow")
        print("1. Sign up")
        print("2. Sign in")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            user_type = input("Enter user type (admin/customer): ")
            self.sign_up(user_type)
        elif choice == '2':
            user_type = input("Enter user type (admin/customer): ")
            if self.sign_in(user_type):
                if user_type == 'admin':
                    self.admin_menu()
                elif user_type == 'customer':
                    self.customer_menu()
        elif choice == '3':
            print("Thank you for using BookMyShow!")
        else:
            print("Invalid choice. Please try again.")

    def admin_menu(self):
        print("Welcome Admin!")
        print("1. Register Movie")
        print("2. Add Slots for Movie")
        print("3. Add Available Days for Slots")
        print("4. Logout")
        choice = input("Enter your choice: ")
        if choice == '1':
            self.register_movie()
            self.ahead = input("You want to continue ahead(y/n): ")
            if self.ahead == 'y':
                self.admin_menu()

        elif choice == '2':
            self.add_slots()
            self.ahead = input("You want to continue ahead(y/n): ")
            if self.ahead == 'y':
                self.admin_menu()

        elif choice == '3':
            self.add_available_days()
            self.ahead = input("You want to continue ahead(y/n): ")
            if self.ahead == 'y':
                self.admin_menu()

        elif choice == '4':
            print("Logged out from admin account.")

    def register_movie(self):
        movie_name = input("Enter movie name: ").capitalize()
        self.users['movies'][movie_name] = {'slots': [], 'available_days': []}
        self.save_users()
        print(f"Movie '{movie_name}' registered successfully.")
        self.ahead = input("You want to continue ahead(y/n): ")
        if self.ahead == 'y':
            self.admin_menu()


    def add_slots(self):
        movie_name = input("Enter movie name: ").capitalize()
        if movie_name in self.users['movies']:
            slots = self.users['movies'][movie_name]['slots']
            while True:
                slot = input("Enter slot (in 24-hour format, e.g., 10:00-11:00): ")
                try:
                    start_time, end_time = slot.split('-')
                    start_time_obj = time.strptime(start_time, '%H:%M')
                    end_time_obj = time.strptime(end_time, '%H:%M')
                    if start_time_obj < end_time_obj:
                        slots.append(slot)
                        another = input("Do you want to add another slot? (y/n): ")
                        if another.lower() != 'y':
                            break
                    else:
                        print("End time should be after start time.")
                except ValueError:
                    print("Invalid time format. Please use HH:MM-HH:MM.")
            self.save_users()
        else:
            print("Movie not found.")
        self.ahead= input("You want to continue ahead(y/n): ")
        if self.ahead == 'y':
            self.admin_menu()


    def add_available_days(self):
        movie_name = input("Enter movie name: ").capitalize()
        if movie_name in self.users['movies']:
            available_days = self.users['movies'][movie_name]['available_days']
            while True:
                start_date = input("Enter start date for movie showing (YYYY-MM-DD): ")
                end_date = input("Enter end date for movie showing (YYYY-MM-DD): ")
                try:
                    start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
                    end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')

                    if start_date_obj <= end_date_obj:
                        date_range = [start_date_obj + timedelta(days=i) for i in
                                      range((end_date_obj - start_date_obj).days + 1)]
                        available_days.extend([date.strftime('%Y-%m-%d') for date in date_range])
                        print("Movie will be showing from", start_date, "to", end_date)
                    else:
                        print("End date should be after or equal to start date.")
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")

                another = input("Do you want to add another range of dates? (y/n): ")
                if another.lower() != 'y':
                    break
            self.save_users()
        else:
            print("Movie not found.")
        self.ahead = input("You want to continue ahead(y/n): ")
        if self.ahead == 'y':
            self.admin_menu()

    def customer_menu(self):
        print("Welcome Customer!")
        print("1. View Available Movies")
        print("2. Book Movie Ticket")
        print("3. Logout")
        choice = input("Enter your choice: ")
        if choice == '1':
            self.view_available_movies()

        elif choice == '2':
            self.book_ticket()
        elif choice == '3':
            print("Logged out from customer account.")

    def view_available_movies(self):
        movies = self.users['movies']
        if movies:
            print("Available Movies:")
            for movie in movies:
                print(movie)
        else:
            print("No movies available.")
        self.ahead = input("You want to continue ahead(y/n): ")
        if self.ahead == 'y':
            self.customer_menu()


    def book_ticket(self):
        movie_name = input("Enter movie name: ").capitalize()
        if movie_name in self.users['movies']:
            available_days = self.users['movies'][movie_name]['available_days']
            if available_days:
                print("Available days for booking:")
                start_date = min(available_days)
                end_date = max(available_days)
                print(f"Movie will be showing from {start_date} to {end_date}")
                selected_day = input("Enter the day for booking (YYYY-MM-DD): ")
                try:
                    selected_day_date = datetime.strptime(selected_day, '%Y-%m-%d')
                    start_date = min(available_days)
                    end_date = max(available_days)
                    start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
                    end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
                    # Check if the selected day falls within the range of available days
                    if start_date_obj <= selected_day_date <= end_date_obj:
                        slots = self.users['movies'][movie_name]['slots']
                        if slots:
                            print("Available slots for booking on", selected_day + ":")
                            for slot in slots:
                                print(slot)
                            selected_slot = input("Enter the slot for booking: ")
                            if selected_slot in slots:
                                # Remove the booked slot from the list of available slots
                                print("Ticket booked successfully!")
                                print("Thank you for using Book My Show")
                                slots.remove(selected_slot)
                                self.save_users()
                            else:
                                print("Invalid slot.")
                        else:
                            print("No slots available for this movie on", selected_day)
                    else:
                        print("Selected day is not within the range of available days.")
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
            else:
                print("No available days for booking for this movie.")
        else:
            print("Movie not found.")


def main():
    book_my_show = BookMyShow()
    book_my_show.menu()


if __name__ == "__main__":
    main()
