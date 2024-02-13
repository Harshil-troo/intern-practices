# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [4, 8, 12, 16, 20, 24, 28]
# res = list()
#
# odd_elements = l1[1::2]
# print("the odd elements of l1 are:",odd_elements)
#
# even_elements = l2[0::2]
# print("the even elements of l2 are:", even_elements)
#
# print("Final list are:")
# res.extend(odd_elements)
# res.extend(even_elements)
# print(res)
#
# list1 = [54, 44, 27, 79, 91, 41]
#
# print("the original list are:", list1)
# element = list1.pop(4)
# print("the list after removing element at index 4:",list1)
#
# list1.insert(2,element)
# print("the list after inserting element at index 2",list1)
#
# list1.append(element)
# print("the list after adding element at last:",list1)
#
#
# sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
# print("The original list are: ", sample_list)
#
# length= len(sample_list)
# chunk_size = int(length/3)
# start = 0
# end = chunk_size
#
# for i in range(3):
#     indexes = slice(start,end)
#
#     list_chunk = sample_list[indexes]
#     print("chunk",i,list_chunk)
#
#     print("after reversing it",list(reversed(list_chunk)))
#
#     start = end
#     end += chunk_size
#
# sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
# print("The original list is:", sample_list)
#
# count_dict = dict()
#
# for item  in sample_list:
#     if item  in count_dict:
#         count_dict[item] += 1
#     else:
#         count_dict[item] = 1
#
# print("printing count of each item:",count_dict)
#
# first_list = [2, 3, 4, 5, 6, 7, 8]
# print("First List ", first_list)
#
# second_list = [4, 9, 16, 25, 36, 49, 64]
# print("Second List ", second_list)
#
# result = zip(first_list, second_list)
# result_set = set(result)
# print("result is" ,result_set)
#
#
# first_set = {23, 42, 65, 57, 78, 83, 29}
# second_set = {57, 83, 29, 67, 73, 43, 48}
#
# print("the original first set is:" ,first_set)
# print("the original second set is:",second_set)
#
# intersection = first_set.intersection(second_set)
# print("the intersection is:" , intersection)
# for item in intersection:
#     first_set.remove(item)
#
# print("first set after removing common element is:",first_set)
#
# first_set = {27, 43, 34}
# second_set = {34, 93, 22, 27, 43, 53, 48}
#
# print("The first set is :",first_set)
# print("The second set is:",second_set)
#
# print("First set is subset of second set:",first_set.issubset(second_set))
# print("Second set is subset of First set:",second_set.issubset(first_set))
#
# print("First set is superset of second set:",first_set.issuperset(second_set))
# print("Second set is superset of First set:",second_set.issuperset(first_set))
#
#
# if first_set.issubset(second_set):
#     first_set.clear()
#
# if second_set.issubset(first_set):
#     second_set.clear()
#
# print("The First set is:",first_set)
# print("The Second set is:",second_set)
#
#
# roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
# sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
#
# print("Roll Number:",roll_number)
# print("Dictionary:",sample_dict)
#
# roll_number[:] = [item for item in roll_number if item in sample_dict.values()]
#
# print("After removing unwanted list:",roll_number)


# speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
# print("Dictionary Values:",speed)
#
# speed_list = list()
#
# for val in speed.values():
#     if val not in speed_list:
#         speed_list.append(val)
# print("Unique list:",speed_list)


# sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
# sample_tuple = tuple(set(sample_list))
# print(sample_tuple)
# print("Minimum number from tuple:",min(sample_tuple))
# print("Maximum number from tuple:",max(sample_tuple))

