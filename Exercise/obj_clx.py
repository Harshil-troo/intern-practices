# class Vehicle:
#
#     def __init__(self,max_speed,mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#
# ModelX = Vehicle("280","12")
# print(ModelX.max_speed,ModelX.mileage)

# class Vehicle:
#     pass

# class Vehicle:
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# class Bus(Vehicle):
#     pass
#
#
# School_Bus = Bus("Volvo Bus",120,10)
# print("Vehicle Name:",School_Bus.name,"| Max_Speed:",School_Bus.max_speed,"| Mileage:",School_Bus.mileage)

# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"
#
# class Bus(Vehicle):
#     def seating_capacity(self, capacity=50):
#         return super().seating_capacity(capacity=50)
#
#
# School_bus = Bus("School Volvo", 180, 12)
# print(School_bus.seating_capacity())

# class Vehicle:
#     color = "White"
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     def Automobile(self):
#         print(f"Color:{self.color}, Vehicle name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage  }")
#
#
# School_bus =Vehicle("School Volvo", 180, 12)
# car =Vehicle("Audi Q5", 240, 18)
#
# School_bus.Automobile()
# car.Automobile()

# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
#     def fare(self):
#         return self.capacity * 100
#
# class Bus(Vehicle):
#     def fare(self):
#         amount = super().fare()
#         amount += amount * 10/100
#         return amount
#
#
# School_bus = Bus("School Volvo", 12, 50)
# print("Total Bus fare is:", School_bus.fare())


# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
# class Bus(Vehicle):
#     pass
#
#
# School_bus = Bus("School Volvo", 12, 50)
# print(type(School_bus))


# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
# class Bus(Vehicle):
#     pass
#
#
# School_bus = Bus("School Volvo", 12, 50)
# print(isinstance(School_bus,Vehicle))
# import sys
# def create():
#     list = []
#     i = 1
#
#     while i <= 200:
#         list.append(i)
#         i +=1
#
#     return list
# #
# #
# # print(create())
#
#
# def creater1():
#     i=1
#     while i <=200:
#         yield i
#         i += 1
#
#
# print(creater1())
# x = creater1()
# print(next(x))
# print(next(x))
# print(next(x))
# print(list(x))




