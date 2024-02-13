"""
x = int(input("Enter the number:"))
if x<0:
    x=0
    print("Negative changed to zero")
elif x == 0:
    print("zero")
elif x == 1:
    print("single")
else:
    print("more")
"""
"""
i = ["car","apple","watermelon"]
for w in i:
     print(w, len(w))
"""


"""
users = {'Harshil':'Active', 'Mahesh':'Inactive','Shubhika':'Active'}
for user , status in users.copy().items():
    if status == 'Inactive':
        del users[user]

active_users = {}
for user , status in users.items():
    if status == 'Active':
        active_users[user] = status
print(active_users)
"""

"""
for i in range(5):
    print(i)

print(list(range(5,10)))
print(list(range(0,5,2)))
print(set(range(10)))       
"""
"""
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
"""
"""
num=5
for num in range(2,num*9):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number ", num)
"""
