# num = int(input("Enter a number:"))
# sum_result = sum(range(1,num+1))
# print("The sum of 1 to", num , "is",sum_result)

# def is_palindrome(s):
#     return s == s[::-1]
#
#
# string = input("Enter a string:")
# if is_palindrome(string):
#     print("it is palindrome")
# else:
#     print("it is not palindrome")

# def count_vowels(s):
#     vowels = "aeiouAEIOU"
#     return sum(1 for char in s if char in vowels )
# string = input("Enter a string:")
# print("number of vowels in", string ,":",count_vowels(string))

# lst = [1,2,3,4,5]
# lst.reverse()
# print(lst)

# lst = [1,2,3,4,4,5,5,5,6,7]
# rmv_duplicat = list(set(lst))
# print(rmv_duplicat)

# Explanation
# Explanation


# def is_prime(num):
#     if num <= 1:
#         return False
#
#     for i in range(2, int(num**0.5) + 1):
#         breakpoint()
#         if i == 0:
#             return False
#     return True
#
#
# num = int(input("Enter a number: "))
# if is_prime(num):
#     print("Prime")
#     print("Prime")
#
# else:
#     print("Not prime")

# import math
# radius = float(input("Enter the radius of a circle:"))
# area = math.pi * radius**2
#
# print("Area of a circle:",area)

# def are_anagrams(str1,str2):
#     return sorted(str1) == sorted(str2)
#
#
# string1 = input("Enter the string:")
# string2 = input("Enter the string:")
# if are_anagrams(string1,string2):
#     print("is anagrams")
# else:
#     print("not anagrams")

# sentence = input("Enter a sentence: ")
# words = sentence.split()
# max_length = max(len(word) for word in words)
# print("Length of the longest word:", max_length)


# def is_sqr_root(num):
#     return int(num ** 0.5)** 2 == num
#
#
# num = int(input("Enter a number:"))
# if is_sqr_root(num):
#     print("It is perfect square  of",num ** 0.5)
# else:
#     print("It is not perfect square number.")

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# common  = list(set(list1) &  set(list2))
# print("Common Element are:",common)

# sentence = "hii i am harshil sidapara"
# capital = sentence.title()
# print("sentence after capitalizing initial:",capital)

# def fibonacci(n):
#     fib_seq= [0,1]
#     while len(fib_seq) < n:
#         fib_seq.append(fib_seq[-1] + fib_seq[-2])
#     return fib_seq
#
#
# num_terms = int(input("Enter the number of terms:"))
# fibonacci_seq = fibonacci(num_terms)
# print("Fibonacci series:",fibonacci_seq)




