import math
import random
import string


# WAP find quadratic root of equation
# quadratic equation : a x2 + b x + c =0



# def quadratic(a,b,c):
#     if a == 0:
#         print("It is not a quadratic equation.")
#     else:
#         discriminant = b ** 2 - 4 * a * c
#         if discriminant < 0:
#             print("No real roots are present")
#         elif discriminant == 0:
#             root = -b / 2 * a
#             print(f"only one real root is present :{root}")
#
#         else:
#             positiveroot = (-b + math.sqrt(discriminant)) / 2 * a
#             negativeroot = (-b - math.sqrt(discriminant)) / 2 * a
#             print(f"Two roots present {positiveroot} and -{negativeroot}")
#
# a = float(input("Enter value of co-efficient of x2: "))
# b = float(input("Enter value of co-efficient of x: "))
# c = float(input("Enter value of constant: "))
#
# quadratic(a,b,c)

# WAP to calculate Sine,Cosine and Tan degree


# def trignometry(degree):
#     rad = math.radians(degree)
#     sine = math.sin(rad)
#     cosine = math.cos(rad)
#     tan = math.tan(rad)
#     print(f"Sine {degree}: {sine}")
#     print(f"Cosine {degree}: {cosine}")
#     print(f"Tan {degree}: {tan}")
# degree = int(input("Enter your Degree: "))
# trignometry(degree)


# WAP to generate OTP/Captcha

# def randomotp(length):
#     letters = string.digits
#     temp = []
#     for i in range(length):
#         x = random.choice(letters)
#         temp.append(x)
#     return "".join(temp)
#
#
# length = int(input("Enter the length of OTP: "))
#
#
# otp = randomotp(length)
# print(f"Your Random OTP is : {otp}")
#
# def captcha(len):
#     lettersd = string.digits + string.ascii_letters
#     temp = []
#     for i in range(len):
#         x = random.choice(lettersd)
#         temp.append(x)
#     return "".join(temp)
#
#
# len = int(input("Enter the length of captcha: "))
#
# captcha = captcha(len)
# print(f"Your Random captcha is : {captcha}")


# WAP : Random Password Generation

# length = 16
# def randompassword(length):
#     upper = string.ascii_uppercase
#     lower = string.ascii_lowercase
#     numbers = string.digits
#     special = string.punctuation
#     password = [random.choice(upper),random.choice(lower),
#                 random.choice(numbers),random.choice(special)]
#
#     allcharacter = upper + lower + numbers + special
#     for i in range(length - len(password)):
#         temp = random.choice(allcharacter)
#         password.append(temp)
#
#     random.shuffle(password)
#     password_str = "".join(password)
#     print(f"Random Password using Random Module: {password_str}")
#
# randompassword(length)

