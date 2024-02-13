# while True print('Hello world')

# print(10 * (1/0))

# print(4 + spam*3)

# print(2+2)

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")\

# class B(Exception):
#     pass
#
# class C(B):
#     pass
#
# class D(C):
#     pass
#
# for cls in [D, B]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")

# try:
#     x = int(input("Please enter a number: "))
#     result = 10 / x
#     print("The result is:", result)
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# try:
#     raise Exception('spam', 'eggs')
# except Exception as inst:
#     print(type(inst))    # the exception type
#     print(inst.args)     # arguments stored in .args
#     print(inst)          # __str__ allows args to be printed directly,
#                          # but may be overridden in exception subclasses
#     x, y = inst.args     # unpack args
#     print('x =', x)
#     print('y =', y)

# import sys
# breakpoint()
# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error:", err)
# except ValueError:
#     print("Could not convert data to an integer.")
# except Exception as err:
#     print(f"Unexpected {err=}, {type(err)=}")
#     raise

# import sys
# breakpoint()
# for arg in sys.argv[1:]:
#     try:
#         f = open('myfile.txt', 'r')
#     except OSError:
#         print('cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readlines()), 'lines')
#         f.close()

# def this_fails():
#     x = 1/0
#
#
# try:
#     this_fails()
# except ZeroDivisionError as err:
#     print('Handling run-time error:', err)

# try:
#     amount = 3000
#     if amount < 2999:
#
#         # raise the ValueError
#         raise ValueError("please add money in your account")
#     else:
#         print("You are eligible to purchase DSA Self Based course")
#
#     # if false then raise the value error
# except TypeError :
#     print("Please give valid value.")
#
# print("Good Morning")

# raise NameError('HiThere')


# If you need to determine whether an exception was raised but don’t intend
# to handle it, a simpler form of the raise statement allows you to re-raise the exception:
# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise


# try:
#     open("database.sqlite")
# except OSError:
#     raise RuntimeError("unable to handle error")

# def func():
#     raise ConnectionError
#
# try:
#     func()
# except ConnectionError as exc:
#     raise RuntimeError('Failed to open database') from exc
#
# try:
#     open('database.sqlite')
# except OSError:
#     raise RuntimeError from None

# try:
#     for i in range(0,11):
#         print(i-1,i+1,i*1,i/1)
#
# except ZeroDivisionError:
#     print("You have entered wrong syntax.")
#
# else:
#     print("okk!!! It was a great answer.")
#
# finally:
#     print("Bye Bye!! Have a Nice Day")

# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print("division by zero!")
#     else:
#         print("result is", result)
#     finally:
#         print("executing finally close")
#
#
# divide (3,2)

# for line in open("myfile.txt",):
#     print(line, end="")


# with open("myfile.txt") as f:
#     for line in f:
#         print(line, end="")


# def f():
#     excs = [OSError('error 1'), SystemError('error 2')]
#     raise ExceptionGroup('there were problems', excs)
#
#
# f()

# try:
#     raise TypeError('bad type')
# except Exception as e:
#     e.add_note('Add some information')
#     e.add_note('Add some more information')
#     raise

# def f():
#     raise OSError('operation failed')
#
# excs = []
# for i in range(3):
#     try:
#         f()
#     except Exception as e:
#         e.add_note(f'Happened in Iteration {i+1}')
#         excs.append(e)
#
# raise ExceptionGroup('We have some problems', excs)


# class CustomException(Exception):
#     def __init__(self,message):
#         self.message = message
#
# try:
#         raise CustomException("This is a custom exception.")
# except CustomException as e:
#         print(e.message)


dict1 = {"name": "john","age": 20}

try:
    print(dict1["address"])

except KeyError:
    print("Please give accurate key.")


# class CustomException(Exception):
#     def __init__(self, message):
#         self.message = message
#
#
# try:
#     age = int(input("Enter your age: "))
#     if age < 0 or age >= 120:
#         raise CustomException(" Wrong age.")
#     print(f"You are {age} years old.")
#
# except ValueError:
#     print("Invalid.. please give value in integer", )
#
# except CustomException as e:
#     print("Sorry Mate",e)


