"""
File System and OS Module
- A Program needs to interact with the computer's file system to get the size of a file or open a file in a different directory.
- The Computer's operating system, such a windows or MacOS, controls the file system, and a program must use functions supplied by the operating system to interact with files.
- The Python standard library's OS module provides an interface to operating system function calls.

Walking Directories
- Use os.walk() method to walk directories
"""

# OS Module Example
import os
my_file = open('/M14/COP3502/hello.txt', 'r')
file_info = os.stat('/M14/COP3502/hello.txt')
print(file_info)
my_file.close()
# os.remove('E:/PycharmProjects/COP3502C/M14/COP3502/hello.txt') # This Deletes the file.

import os
path = os.path.join('//')
for dir_name, sub_dirs, files, in os.walk(path):
    # print(dir_name, 'contains subdirectories:', sub_dirs, end="  ")
    # print("and the files:", files)
    pass

