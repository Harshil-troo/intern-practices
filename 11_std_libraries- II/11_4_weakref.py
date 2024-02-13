import weakref
import sys



# class Person:
#     def __init__(self, name):
#         self.name = name
#
# person = Person("Alice")
# weak_ref = weakref.ref(person)
#
# print(weak_ref())
# del person
#
# print(weak_ref())

#
# my_var = "Harshil"
# a = "Harshil"
# b = "Harshil"
# c = "Harshil"
# # z = "DhavaL"
# # ref_count = sys.getrefcount("Dhaval")
#
# print(f"Reference count: {ref_count}")



# list1 = "harshil"
#
# ref_count = sys.getrefcount("harshil")

# print(f"Reference count: {ref_count}")





class GFG(list):
    pass


obj = GFG("Geeks")

normal_list = obj
print(f"This is a normal object: {normal_list}")

weak_list = weakref.ref(obj)
weak_list_obj = weak_list()
print(f"This is a object created using weak reference: {weak_list_obj}")

proxy_list = weakref.proxy(obj)
print(f"This is a proxy object: {proxy_list}")

for objects in [normal_list, weak_list_obj, proxy_list]:
    print(f"Number of weak references: {weakref.getweakrefcount(objects)}")