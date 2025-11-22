"""
Write Files
- Programs often write to a file to store data permanently.
- The file.write() method writes a string to a file.
- The write() method accepts a string argument.
- Open file in write or append mode. Then write a string to a file using file.write() method.

- File Open Mode: Description
    - file.open(filename, 'w'): Opens file for write (deletes previous content)
    - file.open(filename, 'a'): Opens file for append (new data goes after previous contents)

Points to Note
- If the file is missing or does not exist, a new file is crated in 'w' and 'a' modes.
- A programmer can add a '+' character to the end of a mode, like 'r+' and 'w+' to specify an update mode, Update modes allow for both reading and writing of a file at the same time.
"""
# Example 1
"""
out = open('output.txt', 'w')
out.write('Hello World!\n')
out.write('How are you?')
out.close()
"""
"""
output.txt
Hello World!
How are you?
"""

"""
Context Manager
- A with statement can be used to:
    - Open a file
    - Execute a block statements
    - Automatically close the file 
    - Automatically close the file when complete
- It creates a context manager, which manages the usage of files.  

"""
# Example 1
"""
with open("scores.txt", 'r+') as file:
    for line in file.readlines():
        total = 0
        for item in line.strip().split():
            total += int(item)
        file.write(f"\n{total}")
"""       