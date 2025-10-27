# Practice Problem 1
class Student:
   def __init__(self, grade, major):
       self.grade = grade
       self.major = major

   def calc_grade(self):
       if self.major == "CS":
           return self.grade // 10
       else:
           return self.grade // 5

student1 = Student(90, "CS")
student2 = Student(100, "ART")

# print(student2.calc_grade() * student1.calc_grade()) # This should print 180

# Practice Problem 2:
class Gator:
    name = "Albert"

gator1 = Gator()
# print(gator1.name, end=" ") # Albert
Gator.name = "Alberta"
# print(gator1.name) # Alberta --> Albert Alberta

# Practice Problem 3:
class Parent:
    def __init__(self):
        self.value = 10
    def method(self):
        return self.value

class Child(Parent):
    def __init__(self):
        self.value = 20
    def method(self):
        return super().method() * 2

obj = Child()
# print(obj.method()) # Resulted in Error without self in line 37

# Practice Problem 4:
class Animal():
   def __init__(self):
       self.name = ""

   def print(self):
       print("animal", end=" ")

class Cat(Animal):
   def print(self):
       print("cat", end=" ")

class Dog(Animal):
   def woof(self): # The reason this prints animal because it doesnt have a print function, if it was woof() it would print.
       print("woof", end=" ")

animal = Animal()
cat = Cat()
dog = Dog()
# animal.print()
# cat.print()
# dog.print()

# Practice Problem 5:
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_info(self):
        return f"Book: {self.title} by {self.author}"

class Ebook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    def get_info(self):
        return f"EBook: {self.title} by {self.author}, Size {self.file_size}MB"

digital_edition = Ebook("1984", 'George Orwell', 2)
# print(digital_edition.get_info())

# Practice Problem 6:
class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def get_speed(self):
        return f"{self.name} speed: {self.speed}km/h"

class Car(Vehicle):
    def __init__(self, name, speed, fuel_type):
        super().__init__(name, speed)
        self.fuel_type = fuel_type

    def get_car_info(self):
        return f"{self.get_speed()}, Fuel type: {self.fuel_type}"

car1 = Car("Toyota", 180, "Petrol")
# print(car1.get_car_info())

