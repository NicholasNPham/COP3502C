"""
Function: A block of organized, reusable code used to perform a single related action
    - We can establish that a function requires parameters.
    - Values passed in during function invocation are known as arguments.
    - Functions and methods can also have multiple parameters.

Method: A function within a class

Return Values:
    - Some functions and methods can have a return value.
    - The function will return None if there is no return statement in the function definition.

Method Overloading:
    - Python des not support "Method Overloading".
    - In Python, we may define many methods of the same name and different arguments, but 'only the latest' defined method is used.

Global Variables: Defined outside of the function.
    - The 'global' statement must be used to change the value of global variables inside the function.
    - Should generally be 'avoided'
    - Should only be used to define constants independent of functions.

Function as Objects and Higher Order Functions
    - Everything in Python is an "Object".
    - Python Functions Have:
        1. Value: The exact value it has.
        2. Type: Int, Str, Float, Boolean
        3. Identity: The unique ID that every object has.

Scopes: Block of code where name is visible.
        /-------------------------------------\
        |    Built-In Scope                   |
        /-------------------------------\     |
        |    Global Scope               |     |
        /-------------------------\     |     |
        |    Local Scope          |     |     |
        |                         |     |     |
        \_________________________|_____|_____|

Built-In Functions:
    input()
    print()
    str()
    int()
User-Defined Functions:
    With def Keyword

Different Types of Function Arguments
    - Passed by object reference which is also known as "pass-by-assignment"
    - If the object is 'immutable (e.g., string or integer), the passing is like 'pass-by-value'
    - if the object is mutable (e.g., list), the passing is like pass-by-reference.

Arguments:
    - Positional arguments
    - Keywork Arguments
        1. Allows arguments to map to parameters "by name" rather than position/
        2. Can be mixed with positional arguments, but the keyword arguments should come last.

"""
# Function Examples
"""
def say_hello(name): # name is the Parameter
    print("Hello, im " + name + ".")

# say_hello("Batman") # "Batman is the Argument

def say_hello(first, last): # first is the 1st Parameter, last is the 2nd Parameter
    print("Hello, im " + first + " " + last + ".")

# say_hello("Bat", "Man") # "Bat" is the 1st Argument, "Man" is the 2nd Argument
"""
# Return Value Example
"""
def increment(x, z):
    x += 1
    z += 3
    # print(x) # simply printing x in the function, when calling it does not return anything
    return z # This gives back and returns a value after function

y = 4
a = 6
val = increment(y, a)
print(val)
"""

# Method Overloading Example
"""
# 1st Function
def myAdd(a, b):
    return a + b

d = myAdd(4, 8)
print(d)

2nd Function
def myAdd(a, b):
    print(a + b)

myAdd(4, 8)
e = myAdd(4, 8) # This is using calling the function that is the latest which is the 2nd function not the 1st function
print(e)

# Example of Function as Objects
def sayHello(first, last):
    print("Hello, im " + first + " " + last + ".")

# Function can be used in an assignment like other objects, e.g. int
hello = sayHello
hello("Bat", "Man") # New Function calling with new name. Crazy! but what purpose is this for?
"""
# Global Variables Example
"""
a, b = 2, 3
def magic():
    global a # tells Python: use the global variable 'a'
    a = "two" # modifies the global a
    b = "three" # this creates a *local* variable b inside the function

print(a, b) # Prints "2 3"
magic() # calling magic() envokes change to global variable
print(a, b) # Prints "two 3"

x, y = 300, 200

def minus(z):
    return z - y

x = minus(x)
print(x) # Will print "200"

"""
# Types of Arguments in Functions Example
"""
def add(a, b): # Known as "Passing By Assignment" e.g. a -> x -> 10
    return a+b

y = 10
myList = [1, 2, 3, 4]
myList[0] = 99
print(myList) # will print [99, 2, 3, 4]
# add(myList, y) # myList references to the list and y references to the y variable, will result in type error

x = 10
y = 5
print(add(x, y))

def plus(x):
    x[0] = x[0] + 1

y = [1, 2, 3]
plus(y)

print(y) # will result in [2, 2, 3]
"""
# Knowledge Check
"""
def magic(num, aList):
    num += 4
    aList[1]= 4
    aList = [100, 102]

x = 2
seqNums = [6,9,12]
magic(x, seqNums) # this only converts seqNums of [6, 9, 12] -> [6, 4, 12] because in the function it changes index 1
print(x, seqNums) # x = 2 will stay 2 only because inside function num points to 6 but never leaves function
# aList = [100, 102] is garbage only because it is created in the function but never leaves scope
"""
# Keyword Argument Example
"""
def team(name, project):
    print(name, "is working on", project)

team("david", "Blackjack") # Original
team(name = "david", project = "Blackjack") # Same as original
team(project = "Blackjack", name = "david") # Same as original
# team(project = "Blackjack", "david") results in syntaxError because name is after project
team("david", project = "Blackjack") # same as original
"""

# Return Tmrw at 19:12 part 2 lecture