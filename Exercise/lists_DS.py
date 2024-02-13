"""
list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)
"""
"""
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

list3 = [i + j for i,j in zip(list1,list2)]
print(list3)
"""
"""
numbers = [1, 2, 3, 4, 5, 6, 7]
imp = []
for i in numbers:
     imp.append(i * i)

print(imp)
"""

"""
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

print([(x + y ) for x in list1 for y in list2])
"""

# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# list2.reverse()
# for x, y in zip(list1, list2):
#     print(x, y)

# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# print([list(filter(None,list1))])

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)

# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub_list = ["h", "i", "j"]
#
# list1[2][1][2].extend(sub_list)
# print(list1)

# list1 = [5, 20, 15, 20, 25, 50, 20]
# def remove(sample,val):
#     return [i for i in sample if i != val]
#
#
# res = remove(list1,20)
# print(res)

# list1 = [5, 10, 15, 20, 25, 50, 20]
# index = (list1.index(20))
# list1[index] = 200
# print(list1)
