# WAP to Find Area of Circle, Square, Triangle
# using OOPs and abstraction

from abc import ABC,abstractmethod
import math
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi*self.radius*self.radius
#
# class Square(Shape):
#     def __init__(self,side):
#         self.side = side
#
#     def area(self):
#         return self.side ** 2
#
# class Triangle(Shape):
#     def __init__(self,base,height):
#         self.base = base
#         self.height = height
#
#     def area(self):
#         return (self.height*self.base)/2
#
# shapes = [Circle(5),Square(12),Triangle(4,6)]
#
# for shape in shapes:
#     area = shape.area()
#     print(f"Area of {type(shape).__name__} is {area}")


# WAP for Banking System of withdrawal and deposit
# using Encapsulation

# class Bank:
#     def __init__(self, balance=0):
#
#         self.__balance = balance
#
#
#
#     def deposit(self,dep):
#         self.__balance = self.__balance + dep
#         print(f"Your money is successfully deposit.\nCurrent balance is {self.__balance}")
#
#     def withdraw(self,wep):
#
#         if self.__balance < wep:
#             print("Insufficient Balance...")
#
#         else:
#             self.__balance = self.__balance - wep
#             print(f"Your money is successfully withdraw.\nCurrent balance is {self.__balance}")
#
#     def balance(self):
#         print(f"Your Current balance is : {self.__balance}")
#
#
#
# obj = Bank()
# obj.balance()
# dep = int(input("Enter amount you want to deposit: "))
# obj.deposit(dep)
# wep = int(input("Enter amount you want to withdraw: "))
# obj.withdraw(wep)
# print("Thank you for using service..")

# WAP to Implement Inheritance of Vehicles, Cars & Bikes

# class Vehicle:
#     def __init__(self,brand,model,year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#
#     def showdetails(self):
#         print(f"Vehicles {self.brand} {self.model} {self.year}")
#
#
# class Car(Vehicle):
#     def __init__(self,brand,model,year,seats):
#         super().__init__(brand,model,year)
#         self.seats = seats
#
#     def showdetails(self):
#         super().showdetails()
#         print(f"Car seats are {self.seats}")
#
# class Bike(Vehicle):
#     def __init__(self,brand,model,year,mileage):
#         super().__init__(brand,model,year)
#         self.mileage = mileage
#
#     def showdetails(self):
#         super().showdetails()
#         print(f"Bike mileage  is  {self.mileage}")
#
# carobj = Car("Audi","A6",2024,5)
# bikeobj = Bike("Royal Enfield","Himalayan",2024,20)
# carobj.showdetails()
# bikeobj.showdetails()
