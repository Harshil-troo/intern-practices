"""
def demo(name="Harshil", age=22):
    print(name, age)


demo()
"""
"""
def func1(*args):
    for i in args:
        print(i)


print("Printing Values:")
func1(20 , 40 , 60)

print("Printing Values:")
func1(80,100)
"""
"""
def calculation(a= 40, b= 10):
    addition = a + b
    subtraction = a - b

    return addition, subtraction

a=20
b=15
res = calculation()
print(res)
"""
"""
def showemployee(name, salary=9000):
    print("Name:", name, "&", "Salary:", salary)


showemployee("Harshil", 12000)
showemployee("Shubhika")
"""
"""
def outer_fun(a, b):
    def addition(a, b):
        return a + b

    
    add = addition(a, b)
    return add + 5

result = outer_fun(5, 10)
print(result)
"""
"""
def outerfunc(a=5, b=10):

    def innerfunc(a, b):
        return a+ b

    add = innerfunc(a,b)

    return add+5
a=10
b=20
result =outerfunc(a, b)
print(result)
"""
"""
def recursive(num =55):
     if num:
         return num + recursive(num -1)
     else:
         return 0


result = recursive()
print(result)
"""
"""
def display_name(name, age):
    print(name, age)

new_name = display_name

new_name("harshil",22)
"""
"""
def even():
    print(list(range(4,30,2)))

even()
"""
"""
def num():
    x = [4,6,22,3,42,5,10]
    print(max(x))
    print(min(x))
num()
"""

# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
# also create a lambda function that multiplies argument x with argument y and prints the result.
"""
add = lambda x:x+15
print(add(10))

multi = lambda x, y: x*y
print(multi(12,4))
"""

# Write a Python program to create a function that takes
# one argument, and that argument will be multiplied with an unknown given number.
"""
def myfunc(n):
    return lambda x:x * n

result = myfunc(2)
print("Double the number of =",result(15))
result = myfunc(3)
print("Triple the number of =",result(15))
result = myfunc(4)
print("Quadraple the number of =",result(15))
result = myfunc(5)
print("Quantiple the number of =",result(15))
"""
# Write a Python program to sort a list of tuples using Lambda.
"""
subject_mark = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("original lists of tuple: ",subject_mark)

subject_mark.sort(key=lambda x:x[1])
print("\nLists after sorting:",subject_mark)
"""
# Write a Python program to add two given lists using map and lambda.
"""
list1= [1,2,3]
list2= [4,5,6]

print("Original Lists:")
print(list1)
print(list2)

add = map(lambda x,y : x + y,list1,list2)
print("Result: after adding two lists using lambda")
print(list(add))
"""
"""
list1=[2,4,5]

res = list(map(lambda x:x * x ,list1))
print(res)
"""

# Document Strings
"""
def myfunc():
    Harshil loves Shubhika
    pass
print(myfunc.__doc__)
"""
