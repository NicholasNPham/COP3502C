# Output Prediction 1
class Calculator:
   def __init__(self, initial_value):
       self.value = initial_value

   def add(self, num):
       self.value += num

   def multiply(self, num):
       self.value *= num

   def get_value(self):
       return self.value

# Create an instance
calc = Calculator(5)

# Perform operations
calc.add(3)
calc.multiply(2)
calc.add(1)

# What will be the output of the following line?
# print(calc.get_value()) # returns 17

# Output Prediction 2
class Rectangle:
   def __init__(self, length, width):
       self.length = length
       self.width = width

   def perimeter(self):
       return 2 * (self.length + self.width)

   def area(self):
       return self.length * self.width


r1 = Rectangle(4, 5)
r2 = Rectangle(3, 7)

# print(r1.perimeter()) # returns 18
# print(r2.area()) # returns 21

# Output Prediction 3
class Counter:
   def __init__(self, start=0):
       self.count = start

   def increment(self):
       self.count += 1
       return self.count

   def decrement(self):
       self.count -= 1
       return self.count

   def reset(self):
       self.count = 0
       return self.count

counter1 = Counter(5)
counter2 = Counter()

# print(counter1.increment())  # Output: 6
# print(counter2.increment())  # Output: 1
# print(counter2.reset())  # Output: 0
# print(counter1.decrement())  # Output: 5
# print(counter1.reset())  # Output: 0
# print(counter2.increment())  # Output: 1

# Output Prediction 4
class MyClass:
   x = 9 # class variable

   def __init__(self, x = 2, y = 1):
       self.y = y
       self.x = x # instance variable

m = MyClass(4)
# print(m.x) # this returns 4 because m is initialized with myclass 4 overriding the x = 9

# Output Prediction 4:
class MyClass:
   x = 9

   def __init__(self, x = 2, y = 1):
       self.y = y
       self.x = x

m = MyClass(4)
# print(MyClass.x) # returns 9

# Output Prediction 5
class MyClass:
   x = 9

   def __init__(self, x = 2, y = 1):
       self.y = y # 1
       self.x = x # 4

   def sum_nums(self):
       self.y += self.x # 1 + 4 = 5
       return self.y # 5

m = MyClass(4) # starts with 4
# print(m.sum_nums()) # returns 5

# Output Prediction 6
class Stud:
   pass

class Monster:
  def __init__(self, level=1, name="Monster"):
      self.level = level
      self.name = name

  def __eq__(self, other):
      print("Hi")
      if isinstance(other, Monster):
          return True
      return 123

m = Stud()
n = Monster()
# print(n == m) # Hi 123

# Output Prediction 7
class Car:
   wheels = 4

   def __init__(self, brand, model):
       self.brand = brand
       self.model = model

toyota = Car("Toyota", "Camry")
honda = Car("Honda", "Civic")

# print(toyota.wheels, honda.wheels) # prints (4, 4)

Car.wheels = 5

# print(toyota.wheels, honda.wheels) # prints (5, 5)

toyota.wheels = 3

# print(toyota.wheels, honda.wheels) # prints (3, 5)

# Output Prediction 8
class Calculator:
   z = 10

   def __init__(self, x=5, y=3):
       self.x = x
       self.y = y

   def multiply(self):
       self.z *= self.x
       return self.z


c = Calculator(4) # x=4, y=3
# print(c.multiply()) # 10 * 4 = 40

# Output Prediction 9
class Player:
   def __init__(self, score):
       self.score = score # 20

   @staticmethod
   def add_bonus(player, bonus):
       player.score += 10
       bonus = 5


p1 = Player(20) # 20
bonus = 3

Player.add_bonus(p1, bonus)
print(p1.score, bonus)



# Free Response Question 1
class Gradebook:

    def __init__(self, grades):
        self.grades = grades

    def average(self):
        average =  sum(self.grades) / len(self.grades)
        return average

    def find_median(self):
        sorted_grades = sorted(self.grades)
        if len(sorted_grades) % 2 == 1:
            median =  sorted_grades[len(sorted_grades) // 2]
        else:
            mid = len(sorted_grades) // 2
            median = (sorted_grades[mid] + sorted_grades[mid - 1]) / 2
        return median

    def averages(self):
        return (self.average(), self.find_median())

list_of_grades = [80, 90, 94]
gradebook = Gradebook(list_of_grades)
# print(gradebook.averages())


