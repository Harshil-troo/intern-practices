"""
numbers = [12, 75, 150, 510, 145, 560, 25]
for i in numbers:
    if i > 500:
        break
    elif i > 150:
        continue
    elif i % 5 == 0:
        print(i)
"""
"""
number = 2521045
count = 0
while number != 0:
    number = number//10
    count = count + 1
print("the number of digits are:", count)
"""
"""
n= 5
k= 5
for i in range(0, n+1):
    for j in range(k-i, 0, -1):
        print(j, end="")
    print()
"""
"""
list= [10, 20, 30, 40, 50]

new_list = reversed(list)
for i in new_list:
    print(i)
"""
"""
for i in range(-10,0,1):
    print(i)
"""
"""
for i in range(5):
    print(i)
else:
    print("Done!")
"""
"""
start = 25
end = 50

print("Prime numbers between", start ,"and", end ,"are:")
for num in range(start,end+1):
    if num >1:
        for i in range(2,num):
            if(num % i)==0:
                break

        else:
            print(num)
"""
"""
num1 = 0
num2 = 1
print("Fibonacci Series:")
for i in range(10):
    print(num1,end=' ')

    z = num1+num2

    num1= num2
    num2= z
"""
"""
num = 5
factorial = 1
if num<0:
    print("the factorial does not exist.")

elif num == 0:
    print("the factorial is 1.")

else:
    for i in range(1,num+1):
        factorial= factorial* i
    print("the factorial of", num ,"is:",factorial)
"""
'''
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in my_list[::2]:
    print(i,end=" ")'''

'''input = 6
for i in range(1,input+1):
    print("the number is ",i , "and the cube is:", i**3 )'''
"""
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")
"""
"""
text = "Hello,\rWorld!"
print(text)

print("rgvnvi,\rvvsv")
"""
"""
n = 5
# first number of sequence
start = 2
sum_seq = 0

# run loop n times
for i in range(0, n):
    print(start, end="+")
    sum_seq += start
    # calculate the next term
    start = start * 10 + 2
print("\nSum of above series is:", sum_seq)
"""
