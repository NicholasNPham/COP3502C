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