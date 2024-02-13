from array import array
# a = array('H', [4000, 10, 700, 22222])
# print(sum(a))

import bisect



# scores = [(100,'Harshil'),(300,"Jay"),(400,"khushi")]
# bisect.insort(scores, (200, 'ruby'))
# print(scores)

from heapq import *

# def heapsort(iterable)
#     h = []
#     for value in iterable:
#         heappush(h, value)
#     return [heappop(h) for i in range(len(h))]
#
# print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))


from collections import deque


# d = deque('ghi')
# for elem in d:
# print(elem.upper())
#
# d.append('j')
# d.appendleft('f')
# print(d)
#
# d.pop()
# d.popleft()
# print(list(d))
#
# print(d[0])
# print(d[-1])
#
#
# print(list(reversed(d)))
#
# print('h' in d)
#
# d.extend('jkl')
#
# d.rotate(1)
# print(d)
#
# d.rotate(-1)
# print(d)
#
#
# deque(reversed(d))
#
# d.clear()
# try:
#     d.pop()
#
# except IndexError:
#     print("Index is given wrong.")
#
# d.extendleft("abc")
# print(d)


from decimal import *


# print(round(Decimal('0.70') * Decimal('1.05'), 2))
#
# print(sum([Decimal('0.1')]*10) == Decimal('1.0'))
# print(Decimal(1) / Decimal(7))
#
# print(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 == 1.0)