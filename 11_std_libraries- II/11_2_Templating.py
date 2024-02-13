from string import Template
import time
import os.path
import struct


# t = Template("I am $name . I am working as an Intern in $company.")
# print(t.substitute(name="Harshil" , company="Trootrech"))


# t = Template('Return the $item to $owner.')
# d = dict(item='unladen swallow', owner="Me")
# print(t.substitute(d))

# t = Template('Return the $item to $owner.')
# d = dict(item='unladen swallow')
# print(t.safe_substitute(d))


# photofiles = ['11_1_output_formatting.py', '11_2_Templating.py']
# class BatchRename(Template):
#     delimiter = '%'
#
#
# fmt = input('Enter rename style (%d-date %n-seqnum %f-format): ')
#
#
# t = BatchRename(fmt)
# date = time.strftime('%d%b%y')
# for i, filename in enumerate(photofiles):
#     base, ext = os.path.splitext(filename)
#     newname = t.substitute(d=date, n=i, f=ext)
#     print('{0} --> {1}'.format(filename, newname))

# STRUCT    MODULE

# packed_data = struct.pack('i f s', 42, 3.14, b'Hello')
#
# # Unpack values from a binary string
# unpacked_data = struct.unpack('i f s', packed_data)
#
#
# # Print the packed and unpacked data
# print("Packed data:", packed_data)
# print(struct.calcsize("s"))
# print("Unpacked data:", unpacked_data)

