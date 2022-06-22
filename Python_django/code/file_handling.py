# what is file handling in python?
# file handling is the process of opening, reading, writing and closing files.
#
#opening a file
f = open("test.txt", "r")
#reading a file
print(f.read())

print(f.read(5))
print(f.readlines())
# #closing a file
# f.close()

# #Reading a file line by line
# f = open("test.txt", "r")
# for line in f:
#     print(line)
# f.close()

# #writing to a file
# f = open("test.txt", "w")
# f.write("Hello World")
# f.close()

# #creating a file
# f = open("true.txt", "x")
# f.close()

# # deleting a file
# import os
# os.remove("test.txt")


