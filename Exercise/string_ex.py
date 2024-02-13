# str1 = 'Shubhika'
# print("Original String:",str1)
# res = str1[0]
#
# mid= int(len(str1)/2)
#
# res = res + str1[mid]
#
# res = res + str1[len(str1)-1]
# print("new String:", res)

# def get_middle_three_chars(str1):
#     print("Original String:", str1)
#     mid = int(len(str1) / 2)
#     res = str1[mid -1:mid +2]
#     print("The Middle three Chars are:",res)
#
#
# get_middle_three_chars("JohnDipPeta")
# get_middle_three_chars("jaSonAy")

# s1 = "Ault"
# s2 = "Kelly"

# def append(str1,str2):
#     print("original string:",str1,str2)
#     mid = int(len(str1) / 2)
#     x= s1[:mid:]
#     x = x + s2
#     x = x+ s1[mid:]
#     print("after appending new string in middle:",x)
#
#
# append("Ault","Kelly")

# def mix_string(s1,s2):
#     # get first character from both string
#     first_char = s1[0] + s2[0]
#
#     # get middle character from both string
#     middle_char = s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + s2[int(len(s2) / 2):int(len(s2) / 2) + 1]
#     last_char = s1[len(s1) - 1] + s2[len(s2) - 1]
#     res = first_char + middle_char + last_char
#     print("Mix String is ", res)
#
#
# s1 = "America"
# s2 = "Japan"
# mix_string(s1, s2)

# str1="SHUharsBHIhilKA"
# print("Original String:", str1)
#
# lower=[]
# upper=[]
#
# for char in str1:
#     if char.islower():
#         lower.append(char)
#
#     else:
#         upper.append(char)
#
# sorted = "".join(lower + upper)
# print("The Sorted String is:", sorted)
#
# def find_char_digit_sp_symbl(str1):
#     char_count = 0
#     digit_count = 0
#     sp_symbol = 0
#     for char in str1:
#         if char.isalpha():
#             char_count += 1
#         elif char .isdigit():
#             digit_count += 1
#
#         else:
#             sp_symbol += 1
#     print("\n chars=",char_count ,"\n digit=",digit_count,"\n sp_symbol=",sp_symbol)
#
#
# str1 = "P@#yn26at^&i5ve"
# print("total count of chars,digit and special symbols \n")
# find_char_digit_sp_symbl(str1)


