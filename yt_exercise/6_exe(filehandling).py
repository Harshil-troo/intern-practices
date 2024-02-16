# WAP: to rad file content from a file and file handling

# try:
#     file_loc = "sample.txt"
#     with open(file_loc,"r") as file:
#         content = file.read()
#         print(content)
#         file.close()
#
# except FileNotFoundError:
#     print("OOPS!!File not found.")
#
# except Exception as e:
#     print(f"{e}")

# WAP to count line from file.

# try:
#     file_loc = "sample.txt"
#     with open(file_loc,"r") as file:
#         content = file.read()
#         print(content)
#         file.seek(0)
#         lines_count = 0
#         for line in file:
#             lines_count += 1
#         print(f"No. of lines in file {lines_count}")
#         file.close()
#
# except FileNotFoundError:
#     print("OOPS!!File not found.")
#
# except Exception as e:
#     print(f"{e}")

# WAP to count word frequency

# try:
#     file_loc = "sample.txt"
#     with open(file_loc,"r") as file:
#         content = file.read()
#         print(content)
#         words = content.split()
#         print("Total word in file: ",len(words))
#         word_count = {}
#         for word in set(words):
#             word_count[word] = words.count(word)
#         for key,value in word_count.items():
#             print(key,value)
#         file.close()
#
# except FileNotFoundError:
#     print("OOPS!!File not found.")
#
# except Exception as e:
#     print(f"{e}")

# WAP: to write content in file and use error handling.

try:
    file_loc = "sample1.txt"
    content = input("Enter file Content: ")
    with open(file_loc,"w") as file:
        file.write(content)
        file.close()

except Exception as e:
    print(f"{e}")