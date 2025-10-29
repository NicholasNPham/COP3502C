
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
