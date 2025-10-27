"""
Object-Oriented Programming

Overview:
- Class, Instance
- Different Attributes in Class
- Different Methods in Class
- Operator Overloading
- Inheritance and Composition

Basics of Classes
- A class is a blueprint or template for creating objects. It defines a set of attributes and methods that characterize any object of that class. Classes encapsulate data for the object and method to manipulate that data.
- An object is a concrete instance of a clas. It's a self-contained component of a program that contains data and procedures to manipulate that data. Objects are created based on the structure defined by the class.

Constructors
- We can initialize a new object using a constructor specifying the initial state.
- When a class is called, a new instance of that class is created.
- The __init__ method of the class is called with the new object as its first argument (named self), along with any additional arguments provided in the call expression.

Constructor Default Parameters
- Constructor Parameters can have default values using the name=value syntax


"""

class Person: # This allows the class to be made
    def __init__(self, name, age): # Initial Construction of Attributes
        self.name = name
        self.age = age

    def change_age(self, new_age):
        self.age = new_age

p1 = Person("John", 21)
# print(p1.age) # prints 21

# p1.job = "Teacher" # Can add new attributes outside of initial constructor
# print(p1.job)

p1.change_age(78)
# print(p1.age) # prints 78


# p2 = Person("David", 60)
# print(p2.age) # <instance>.<attribute>
# print(p1.age + p2.age)

# class Student: # Makes us write it over and over
#     pass

class Student:

    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

s1 = Student("Jack", 18, "Biology")
# s1.name = "Jack"
# s1.age = 18
# s1.major = "Biology"

s2 = Student("David", 22, "Chemistry")
# s2.name = "David"
# s2.age = 22
# s2.major = "Chemistry"

# print(s1.major)

# Basics of Classes Example 1:

class Monster:
    def __init__(self, level, name):
        self.level = level
        self.name = name

    def increase_level(self, amount):
        self.level += amount

m = Monster(0, "ChuChu")
m.increase_level(2)
# print(m.level) # This will print 2
# print(m.name) # prints ChuChu

# Constructor Default Parameters Example:

class Monster:
    def __init__(self, level = 1, name = "Monster"):
        self.level = level
        self.name = name

    def increase_level(self, amount):
        self.level += amount

m = Monster()
m.increase_level(2)
# print(m.level) # This will print 3
# print(m.name) # prints Monster
