# def division(x,y):
#     try:
#         result = x / y
#         print("The answer is:", result)
#
#     except ZeroDivisionError:
#         print("No number can divide by zero.")
#
#
# division(12,0)

# def get_value():
#
#     try:
#         value = int(input("Enter a value:"))
#         print("The",value, "you entered is appropriate.")
#         return value
#     except ValueError:
#         print("Please give appropriate value.")
#
#
# get_value()

# def open_file(filename):
#     try:
#         file = open(filename,'r')
#         contents = file.read()
#         print(contents)
#         file.close()
#
#     except FileNotFoundError:
#         print("The file does not exist.")
#
#
# file_name = input("Input a file name: ")
#
# open_file(file_name)

# def value_fun():
#     try:
#         value1 = float(input("Enter a first input:"))
#         value = float(input("Enter a second input:"))
#
#         return value,value1
#     except ValueError:
#         print("Please give numerical value.")
#
#
# value_fun()

# def open_file(filename):
#     try:
#         with open(filename,'w') as file:
#             contents = file.read()
#             print(contents)
#             file.close()
#
#     except PermissionError:
#         print("Permission denied to open these file.")
#
#
# file_name = input("Input a file name: ")
#
# open_file(file_name)

# def test(data,index):
#     try:
#         result =data[index]
#         print("Result:",result)
#
#     except IndexError:
#         print("the index is out of range.")
#
#
# nums = [1,2,3,4,5]
# index = int(input("Input the index: "))
# test(nums,index)

# try:
#     n = input("Enter a string: ")
#     print("You Entered: ",n)
#
# except KeyboardInterrupt:
#     print("\n Input is cancelled.")

# def division(dividend,divisor):
#     try:
#         result = dividend / divisor
#         print("The answer is: ",result)
#
#     except ArithmeticError:
#         print("You have got arithmatic error.")
#
#
# dividend = float(input("Give the dividend:"))
# divisor = float(input("Give the Divisor:"))
#
# division(dividend,divisor)
