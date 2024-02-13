"""
squares = [1, 4, 9, 16, 25]
squares[3] = 20
print(squares)
print(squares[0])
squares.append(350)
squares.append(7 ** 2)
print(squares)
print(squares[0:3:1])
print(squares[-4:])
print(squares + [12,45,25,78])
"""

# example of nested lists
"""
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n] # a lists containing other lists as item.
print(x)
"""
# methods of lists
"""
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count("apple"))
print(fruits.count("chickoo"))
print(fruits.index("pear"))
print(fruits.index("banana",4))
fruits.reverse()
print(fruits)
fruits.append("strawberry")
print(fruits)
fruits.sort()
print(fruits)
fruits.pop(4)
print(fruits)
fruits.remove("apple")
print(fruits)
"""
# using list as queue

"""
from collections import deque

queue = deque(["Eric","John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)
"""

# LISTS COMPREHENSIONS
"""
squares = [x ** 2  for x in range(11) if x % 2 ==0]
print(squares)
"""

"""
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])
"""

# NESTED LISTS COMPREHENSIONS

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
#
# print([[row[i]for row in matrix]for i in range(4)])

# del statement

# a = [-1, 1, 66.25, 333, 333, 1234.5]
# del a[0]
# print(a)
# del a[:4:1]
# print(a)
# del a[:]
# print(a)

    

