"""
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a , end=' ')
        a, b = b, a+b
    print()


fib(10)
"""
"""
def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


x = fib2(100)
print(x)
"""
"""
def f(a, L=[]):
    L.append(a)
    return L

print(f(3))
print(f(2))
print(f(1))
"""
"""
# A sample function that takes 4 arguments
# and prints the,
def fun(a, b, c, d):
	print(a, b, c, d)

# Driver Code
my_list = [1, 2, 3, 4,5]

# Unpacking list into four arguments
fun(*my_list)
"""

"""
def mySum(*args):
    return sum(args)


# Driver code
print(mySum(1, 2, 3, 4, 5))
print(mySum(10, 20,56,25,14,78,15,12))
"""
"""
def fun(a, b, c):
    print(a, b, c)
    
    
d = {'a': 2, 'b': 4, 'c': 10}
fun(**d)
"""
"""
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    greeting =func("Harshil")
    print(greeting)

greet(shout)
greet(whisper)
"""
"""
def add(x=10):
    def adder(y=12):
        return x+y
    return adder
addi = add()
print(addi(10))
"""
# Modifying list variable using global keyword.
"""
arr = [10,20,30]

def fun():
    global arr
    arr = [20,30,40]

print("the array before executing function", arr)
fun()
print("the array after executing function", arr)
"""
# Python program showing a use of global in nested function
"""
def add():
    x = 15
    def change():
        global x
        x = 20
    print("value before change:",x)
    change()
add()
print("value after change:", x)
"""

# lambda function
"""
double = lambda x:x+2
avg = lambda x,y,z: (x+y+z)/3
print(double(3))
print(int(avg(3,6,9)))
"""
"""
def myfunc(n):
  return lambda a : a * n

doubler = myfunc(2)
tripler = myfunc(3)

print(doubler(11))
print(tripler(11))
"""

