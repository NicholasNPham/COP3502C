"""
Lecture 1

Overview:
- Read data from files
- Write data to new/existing files
- Handle data with different file formats
    - Text files
    - Comma separated values files (csv)
    - Binary files
- Understanding of interacting with file systems in your OS
- How to plot and style aggregate data using matplotlib Python Module
"""
"""
Lecture 2

Reading Files:
- Input information could be obtained from a file using the built-in open() method:
- File object supports iteration to iterate over each line of the file.
- use try-except-finally block to handle exceptions.

file = open(filename)

- Method: Description
    - file.read(): Read file's entire contents as a string
    - file.readline(): Read next line from file as a string
    - file.readlines(): Read a file's content as a list of lines
    - file.close(): Closes the file, after which no more reads or writes are allowed

- file.read() reads the entire file as a string. Each line in the file ends with '\n'

Removing the Whitespace
- To remove all whitespace from the start and end of a string, we can use strip()
"""
# Example 1
"""
scores.txt
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1


file = open('scores.txt')
contents = file.read()
file.close()

for lines in content:
    print(line, end="")
print()
"""
# Example 2 (Whitespace)
"""
file = open("scores.txt")
lines = file.readlines()
file.close()
print(lines)

for line in lines:
print(line.strip())
"""
# Example 3 (tef)
"""
file = None
try:
    file = open("scores.txt")
    contents = file.read()
    print(contents)
    
except OSError:
    print("Some OS Error, e.g. I/O or file not found")
    
finally:
    file.close() if file else print("File was never opened")
"""
