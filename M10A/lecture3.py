
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

print(r1.perimeter())
print(r2.area())

# Accessing Attributes
class Monster:
    def __init__(self, level=1, name="Monster"):
        self.level = level
        self.name = name

    def increase_level(self, amount):
        self.level += amount

pikabu = Monster(2, "Pikabu")

print(getattr(pikabu, "level")) # 2
print(getattr(pikabu, "name")) # Pikabu

print(pikabu.level) # 2
print(pikabu.name) # Pikabu

print(hasattr(pikabu, "increase_level")) # True
