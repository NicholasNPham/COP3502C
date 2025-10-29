"""
Instance Methods
- Automatically Receive the instance (self) as first argument
- Can access/modify both instance and class attributes
- Most common method type
- Called on instance of the class

- BOUND TO AN INSTANCE: These methods operate on specific instances (objects) of the class.
- ACCESS: They can access both instance attributes (via self in Python) and class attributes.
- FIRST PARAMETER: In Python, They automatically receive the instance as the first parameter (conventionally named self).
- USAGE: Called on an object of the class (object.method())

Class Method
- Decorated with @classmethod
- Received the class (cls) as first argument
- can access.modify class state but not instance state
- often used for alternative constructors or factory methods

Static Methods
- NO BINDING: Not bound to either the class or instance
- NO AUTOMATIC PARAMETERS: Does not automatically receive self or cls.
- ACCESS: Cannot directly access either instance or class attributes
- DECLARATION: In Python, created using the @staticmethod decorator.
- PURPOSE: For utility functions related to the class but not dependent on class or instance state

When to use Instance Vs. Class Methods
- Instance Methods:
    - WORKING WITH INSTANCE-SPECIFIC DATA: when you need to access or modify attributes that belong to a specific object.
    - REPRESENTING OBJECT BEHAVIOR: when the method represents something this object 'does' or a state it can be in.
    - OBJECT-SPECIFIC OPERATIONS: When the operation makes sense only in the context of a specific instance.
- Class Methods:
    - ALTERNATIVE CONSTRUCTORS: To provide different ways to create objects beyond the standard __init__.
    - WORKING WITH CLASS-LEVEL DATA: When tracking or modifying information about the class itself., like counters or configurations that apply to all instances.
    - OPERATIONS ON THEW CLASS: When an operation pertains to the class as a whole, not any specific instance.

- THE KEY IS TO CONSIDER WHETHER THE METHOD OPERATES ON THE SPECIFIC STATE OF AN INDIVIDUAL OBJECT (INSTANCE METHOD) OR DEALS WITH THE CLASS AS A CONCEPT (CLASS CONCEPT)
"""

# Output Prediction question 1
class Calculator:
    def __init__(self, initial_value):
        self.value = initial_value

    def add(self, num):
        self.value += num

    def multiply(self, num):
        self.value *= num

    def get_value(self):
        return self.value

calc = Calculator(5)

calc.add(3)
calc.multiply(2)
calc.add(1)

# print(calc.get_value()) # This should return 17

# Output Prediction Question 2
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

r1 = Rectangle(4, 5) # This should return 18
r2 = Rectangle(3, 7) # This should return 21 in the prints of course

# print(r1.perimeter())
# print(r2.area())

# Output Prediction Question 3
class Counter:
    def __init__(self, start = 0):
        self.count = start

    def increment(self):
        self.count += 1
        return self.count

    def decrement(self):
        self.count -= 1
        return self.count

    def reset_count(self):
        self.count = 0
        return self.count

counter1 = Counter()
counter2 = Counter(5)

# print(counter1.increment()) # 1
# print(counter2.increment()) # 6
# print(counter2.reset_count()) # 0
# print(counter1.decrement()) # 0
# print(counter1.reset_count()) # 0
# print(counter2.increment()) # 1

# Output Prediction Question 4
# class MyClass:
#     x = 9
#
#     def __init__(self, x = 2, y = 1):
#         self.x = x
#         self.y = y

# m = MyClass(4) # Initialize x as now 4 not default 2
# print(m.x) # returns m.x as 4 and hides y = 1
# print(MyClass.x) # return the class not the instance of m

# Output Prediction Question 5
"""
class MyClass:
    x = 9

    def __init__(self, x = 2, y = 1):
        self.y = y
        self.x = x

    def sum_nums(self):
        self.y += self.x
        return self.y

m = MyClass(4)
print(m.sum_nums())
"""

# Output Prediction Question 6
class MyClass:
    x = 9

    def __init__(self, x = 2, y = 1):
        self.y = y
        self.x = x

    def sum_nums(self):
        self.y += MyClass.x
        return self.y

# m = MyClass(4)
# print(m.sum_nums()) # prints 10

# Output Prediction Question 7
class Stud:
    pass

class Monster:
    def __init__(self, level = 1, name = "Monster"):
        self.level = level
        self.name = name

    def __eq__(self, other):
        print("Hi")
        if isinstance(self, Monster):
            return True
        return 123

# m = Stud()
# n = Monster()
# print(n == m) # prints Hi -> 123

# Accessing Attributes
class Monster:
    def __init__(self, level=1, name="Monster"):
        self.level = level
        self.name = name

    def increase_level(self, amount):
        self.level += amount

pikabu = Monster(2, "Pikabu")

# print(getattr(pikabu, "level")) # 2
# print(getattr(pikabu, "name")) # Pikabu
#
# print(pikabu.level) # 2
# print(pikabu.name) # Pikabu
#
# print(hasattr(pikabu, "increase_level")) # True

# Class Method Example 1:
class Student:
    school_name = "Python High"

    @classmethod
    def change_school(cls, new_name):
        # can modify class state, but not the instance state
        cls.school_name = new_name

Student.change_school("Python Academy")
# print(Student.school_name) # Output: Python Academy

# Static Methods Example 1:
class Student:

    @staticmethod
    def is_passing_grade(grade):
        # utility function that doesn't need access to class or instance state
        return grade >= 60

print(Student.is_passing_grade(75)) # Output: True

# Static or Class method Example 1:
class Example:
    count = 0

    def __init__(self, value):
        self.value = value
        Example.count += 1

    def get_value(self): # Instance Method
        return self.value

    @classmethod
    def get_count(cls): # Class method
        return cls.count

    @staticmethod
    def utility(x, y): # Static Method
        return x + y
