# class Student:
#     def __init__(self):
#         self.name = "harshil"
#         self.age = "21"
#         self.city = "mumbai"
#
#     def person(self):
#         print("My Name is " + self.name +" . I am " + self.age +" years old. I am born in " + self.city + ".")
#
#
# object =Student()
# object.person()

# class GFG:
#     def __init__(self, name, company):
#         self.name = name
#         self.company = company
#
#     def __str__(self):
#         return f"My name is {self.name} and I work in {self.company}."
#
#
# my_obj = GFG("John", "GeeksForGeeks")
# print(my_obj)

# class Addition:
# 	first = 0
# 	second = 0
# 	answer = 0
#
# 	# parameterized constructor
# 	def __init__(self, f, s):
# 		self.first = f
# 		self.second = s
#
# 	def display(self):
# 		print("First number = " + str(self.first))
# 		print("Second number = " + str(self.second))
# 		print("Addition of two numbers = " + str(self.answer))
#
# 	def calculate(self):
# 		self.answer = self.first + self.second
#
#
# # creating object of the class
# # this will invoke parameterized constructor
# obj1 = Addition("Harshil", "Sidapara")
#
# # creating second object of same class
# obj2 = Addition(10, 20)
#
# # perform Addition on obj1
# obj1.calculate()
#
# # perform Addition on obj2
# obj2.calculate()
#
# # display result of obj1
# obj1.display()
#
# # display result of obj2
# obj2.display()


# class Dog:
#     breed = "Labrador"
#
#     def __init__(self,name):
#         self.name = name
#
#
# e = Dog("Pew")
# f = Dog("Tim")
#
# print(e.breed)
# print(f.breed)
# print(e.name, f.name)

# class Dog:
#     tricks=[]
#
#     def __init__(self,name):
#         self.name = name
#         self.tricks = []
#
#     def add_tricks(self,trick):
#         self.tricks.append(trick)
#
#
# d =Dog("Buido")
# e = Dog("Fido")
# d.add_tricks("play dead")
# e.add_tricks("self rover")
# print(d.tricks)

# class Dog:
#     animal = "Dog"
#
#     def __init__(self,breed,color):
#         self.breed = breed
#         self.color = color
#
#
# Rodger =Dog ("Pug","Brown")
# Buzo = Dog("BullDog","Black")
#
# print("Rodger Details:")
# print("Rodger is a ",Rodger.animal)
# print("Breed:",Rodger.breed)
# print('Color: ', Rodger.color)
#
# print('\nBuzo details:')
# print('Buzo is a', Buzo.animal)
# print('Breed: ', Buzo.breed)
# print('Color: ', Buzo.color)
#
# print("\nAccessing class variable using class name")
# print(Dog.animal)

# class Dog:
#     animal = 'Dog'
#
#     def __init__(self,breed):
#
#         self.breed = breed
#
#     def setColor(self,color):
#         self.color = color
#
#     def getColor(self):
#         return self.color
#
#
# Rodger = Dog("Pug")
# Rodger.setColor("Brown")
# print(Rodger.getColor())

