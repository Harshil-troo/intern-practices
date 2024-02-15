# take comma separated string from user and
# generate list and tuple of those separated values

# a = input("Enter a comma separated values:")
# lst = a.split(",")
# print(lst)
# tpl = tuple(lst)
# print(tpl)

# Arithmatic Progression and Geometric Progression

# a = int(input("Enter the Starting value of series: "))
# d = int(input("Enter the difference between two values in AP: "))
# r = int(input("Enter the ratio between two values in GP: "))
#
# ap = [a]
# gp = [a]
# temp = a
# for i in range(a,a+9):
#     a = a+d
#     ap.append(a)
# print("AP: ",ap)
#
# for i in range(temp,temp+9):
#     temp = temp*r
#     gp.append(temp)
# print("GP: ",gp)


# Check is it palindrome or not?

# def palindrome(str):
#     for i in range(0,int(len(str)/2)):
#         if str[i] != str[len(str)-i-1]:
#             return False
#
#     return True
#
# str = input("Enter a string: ").lower()
#
# if palindrome(str):
#     print("It is palindrome.")
#
# else:
#     print("It is not.")


# write a sum of prime number till 1000 number.

# def sumprime():
#     lst = []
#     for j in range(2,1000):
#         for i in range(2,j):
#             if j % i == 0:
#                 break
#
#         else:
#             # print("Prime")
#             lst.append(j)
#     return lst
# temp =sumprime()
# print(temp)
#
# print(sum(temp))