# method overloading

# class A:
#     def sum(self,a=None,b=None,c=None):
#         if a != None and b != None and c != None :
#             print(a+b+c)
#         elif a != None and b != None :
#             print(a+b)
#         else:
#             print(a)
#
#
# a1 = A()
# a1.sum(2,4,6)
# a1.sum(2,3)
# a1.sum(5)

# method overriding

# class Student:
#     def sum(self,m1,m2):
#         print(m1+m2)
#
# class B(Student):
#     # pass
#      def sum(self,m1,m2):
#         print((m1+m2)/10)
#
#
# s1 = Student()
# s1.sum(40,50)
#
# s2 = B()
# s2.sum(20,10)
#
# # In overriding if class has no personal
# # method in it then it take the method of parent class.