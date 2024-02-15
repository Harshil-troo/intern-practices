import re


# WAP to check password  validity between
# length 8 to 16
# at least 1 capital, 1 small and 1 special symbol (@#$)


# password = input("Enter your password: ")
#
# x =True
# while x:
#         if len(password)<8 or len(password) > 16:
#             break
#
#         elif not  re.search("[A-Z]",password):
#             break
#         elif not re.search("[a-z]",password):
#             break
#         elif not re.search("[0-9]",password):
#             break
#         elif not re.search("[@#$%^&*():.!]",password):
#             break
#         else:
#             print("Password is a valid password")
#             x = False
#             break
#
# if x :
#     print("Password is Invalid.")



# WAP to get country code using phone number

# numbers = ["+91-98563245690","+1-2456-8965","+22-5638974121"]
#
# def countrycode(numbers):
#     pattern = r'(\+\d+)-'
#     for number in numbers:
#         match = re.findall(pattern,number)
#         if match:
#             print(f"{number} Country code is:{match}")
#
# countrycode(numbers)

# WAP for sum of list using recursion

# size = int(input("Enter the size of list: "))
# list =[]
# for i in range(size):
#     temp = int(input(f"Enter {i} index value: "))
#     list.append(temp)
# print(list)
#
# def listsum(list):
#     if not list:
#         return 0
#     else:
#         return list[0] + listsum(list[1:])
#
# print(listsum(list))


# WAP to get last term of fibonacci series using recursion

# num = int(input("Enter the index of fibonacci series: "))
#
# def fib(num):
#     if num == 0 or num ==1 :
#         return num
#     else:
#         return fib(num-1) + fib(num-2)
#
# print(fib(num))