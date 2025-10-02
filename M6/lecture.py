"""
Number Systems:

Decimal -> (10)^(0-9) digits (We Use base 10 Systems)
- Example: 217 = (2/10^2)(1/10^1)(7/10^0) = 2 * 100 + 1 * 10 + 7 * 1

Binary  -> (2)^(0,1) digit
- Example: 101 = (1/2^2)(0/2^1)(1/2^0) = 1 * 4 + 0 * 2 + 1 * 1 = 5 <- this 5 represents the decimal representation of binary 101

Decimal -> Binary
- Example: Look at Notes for Example

Octal -> (8)^(0-7) digits
- Example: 207 = (2/8^2)(0/8^1)(7/8^0) = 2 * 64 + 0 * 8 + 7 * 1 =  135 <- this 135 represents the decimal representation of octal 207

Hexadecimal -> (16)^(0-15) digits
(0-15) = (1, 2, 3, 4, 5, 6, 7, 8, 9, (10=A), (11=B), (12=C), (13=D), (14=E), (15=F))
Example: 5A = = (5/16^1)(A/16^0) = 5 * 16 + 10 * 1 = 81 <- this 81 represents the decimal representation of hexadecimal 5A

Number Systems:
- In Mathmatics, a base is the number of different digits or combinations of digits and letters that a system of counting uses to represents numbers

Binary Representation:
- Computers use binary for all data. Numbers are stored using binary numbering
- Characters are  stored as numbers which represent their symbols

Practice Question: Convert binary number 01001001 to decimal number.

Octal and Hexadecimal:
Binary to Octal: Group 3 bits at a time
Binary to Hexadecimal: Group 4 bits at a time
- By convention, octal is prefixed with '0', while hex is prefixed with '0x'. Binary Numbers are prefixed with '0b'.

Practice Question: Look at notebook for information.

When converting binary to octal or binary or hexadecimal: Convert with powers of two because it starts with binary.

NUMERIC & ITERABLE TYPES

Overview of Built-In Types
- Most built-in types are one of...
    - Numeric (Number)
    - Sequence (Ordered collection of objects)
    - Container (Unordered)
- All Python values are one of...
    - Mutable (Changeable)
    - Immutable (Fixed)

Numbers: Numbers can be manipulated using arithmetic operators.

String: A string is a sequence of characters. String is immutable

ASCII Code
- ASCII stands for America nStandard Code for Information Interchange. ASCII code is the numerical representation  of a
  character such as a "a" or "@" or an action of some sort.
    - ASCII code is used to represent every possible character as a unique number, known as code point.
    - We could convert between a text character and encoded value using ord() or chr().

Overview of Built-In Types
- Most Built-in types are one of...
    - Numeric (number)
    - Sequence (ordered collection of objects)
    - Container (unordered)
- All Python values are one of...
    - Mutable (Changeable)
    - Immutable (Fixed)

Lists:
- Lists (mutable) can be indexed from its front or back. Typically, lists are surrounded with brackets [].
- A Slice can be obtained using [m:n], where "m" is the inclusive starting point and "n" is the exclusive ending point.

Assignment to Slicing
- Assignment to slices can change the size of the list or clear it entirely. We assign only iterable and not a single element to a slice.

Built-In Functions in Lists
- list.append(#)
- list.extend(#,#,#)
- list.insert(index, #)
- list.remove(#)
- list.pop(index)
- list.clear()

List Comprehensions:
List comprehension provides a shorter syntax to create a new list by iterating over another iterable and modifying each element.

List Nesting:
Embedding a list inside another list is known as list nesting.

Two-Dimensional Lists:
Two-dimensional list is a list within a list. It represents a table with rows and columns.

Shallow Copy:
A shallow copy constructs a new collection object and then populate it with references to the child objects found in the original.

"""
# String Example
"""
str = "Python"

# str[1] = "x" # Results in TypeError because string is immutable.

print(str[1:4:2]) # This gets a specific part of the immutable string and adds a step to get only "y" and "h"
print(str[-1:-4:-1]) # This gets the last index and a specific part of the string backwards in a -1 step.
print(str[:5]) # This gets the first 5 index starting from 0 to 4.
print(str[::-1]) # This reverses the string.
print(str[1:]) # This gets the last 5 index starting from 1 to 5. 
"""
# ASCII Example
"""
str = "A"
print(ord(str)) # prints 65
print(chr(69)) # prints letter E
"""
# List Example
"""
var = 56
my_list = [23, 45, 67, 89] # index = [0, 1, 2, 3] or index = [-4, -3, -2, -1]
print(my_list) # prints [23, 45, 67, 89]
print(my_list[1]) # prints 45
print(my_list[-1]) # prints 89
print(my_list[0:3]) # prints [23, 45, 67] 
print(my_list[0:3:2]) # prints [23, 67]
print(my_list[-1:-3:-1]) # prints [89, 67]
print(my_list[:] # prints the same list but a copy of it
"""
# List Example 2
"""
my_list = [23, 56, 43, 78, 99]
my_list[0] = 100 # changes the first index value
print(my_list) # prints [100, 56, 43, 78, 99]

# my_list = [23, 56, 43, 78, 99]
# my_list[0:2] = 100
# print(my_list) # Results in typeError cannot change the value with a range

my_list = [23, 56, 43, 78, 99]
my_list[0:2] = [100] # the brackets in the new value allow for mutable change
print(my_list) # prints [100, 43, 78, 99] because its changes index 0, 1

my_list = [23, 56, 43, 78, 99]
my_list[0:2] = [100, 200, 300, 400, 500] # the brackets in the new value allow for mutable change
print(my_list) # prints [100, 43, 78, 99] because its changes index 0, 1

# my_list = [23, 56, 43, 78, 99]
# my_list[0:4:2] = [100, 200, 300, 400, 500]
# print(my_list) # results in TypeError because it cannot match 5 values to only two positions with a step

my_list = [23, 56, 43, 78, 99]
my_list[0:4:2] = [100, 200] # the brackets in the new value allow for mutable change
print(my_list) # prints [100, 56, 200, 78, 99] in iterations of index 0 and index 2

# my_list = [23, 56, 43, 78, 99]
# my_list[0:4:2] = [100]
# print(my_list) # returns value error because it cannot 1 value with two positions with a step.
"""
# List Example 3
"""
a = [1, 2, 3, 4]
b = [5, 6]
c = a + b
print(c) # prints [1, 2, 3, 4, 5, 6]
a.extend(b)
print(a, b) # prints [1, 2, 3, 4, 5, 6] [5, 6]

d = [6] * 10
print(d) # prints [6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
"""
# Nesting Lists
"""
nestedList = [[23, 45, 67],[34, 56], [78, 67, 89]] # index = [[0], [1], [2]]
print(nestedList) # prints [[23, 45, 67], [34, 56], [78, 67, 89]]
print(nestedList[0]) # prints [23, 45, 67]
print(nestedList[0][1]) # prints 45
print(nestedList[0][1:]) # prints [45, 67]
"""
# Nested List example 2:
"""
nestedList = [[23, 45, 67],[34, 56], [78, 67, 89], [12, 45, 67]]

res = []
for sublist in nestedList:
    res.append(sum(sublist))

print(res) # [135, 90, 234, 124]

res2 = [sum(sublist) for sublist in nestedList]
print(res2)
"""
# Two Dimensional Lists
"""
numRows, numCols = 3, 4
board = []

for rows in range(numRows): # dictates how many indexes
   r = [] # Introduce an empty list
   for cols in range(numCols): # How many indexes per index
       r.append("-")
   board.append(r)
print(board)

board2 = [["-" for cols in range(numCols)] for rows in range(numRows)]
print(board2)
"""