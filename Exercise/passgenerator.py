# import random
#
# # lower = "abcdefghijklmnopqrstuvwxyz"
# # upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# # numbers= "0123456789"
# # symbols = "`~[]{}/.,;'\|:?><!@#$%^&*"
# #
# # all_chars = lower + upper + numbers + symbols
# # length = int(input("Enter a length of password: "))
# #
# # password = ''.join(random.sample(all_chars,length))
# # print("Generated Password: ",password)
#
# import re
# import random
# import string
#
#
#
#
# def generate_password(length):
#     # Define a regular expression pattern for the password
#     pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{" + str(length) + r",}$"
#
#     while True:
#         # Generate a random password
#         password = ''.join(random.choices(string.ascii_letters + string.digits + '@$!%*#?&', k=length))
#
#         # Check if the password matches the pattern
#         if re.match(pattern, password):
#             break
#     return password
#
#
#
# # Generate a random password with length 8
# password = generate_password(4)
#
#
#
# print("Generated Password:", password)


