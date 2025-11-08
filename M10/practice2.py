
# MCQ 1
"""
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

print(student2.calc_grade() * student1.calc_grade())
"""

# MCQ 2
"""
class Gator:
    name = "Albert"

gator1 = Gator()
print(gator1.name, end=" ")
Gator.name = "Alberta"
print(gator1.name)
"""

# MCQ 3
"""
class Parent:
    def __init__(self):
        self.value = 10
    def method(self):
        return self.value

class Child(Parent):
    def __init__(self):
        self.value = 20
    def method():
        return super().method() * 2
    
    obj = Child()
    print(obj.method())
"""

# MQC 4
"""
class Animal():
    def __init__(self):
        self.name = ""

    def print(self):
        print("animal", end=" ")

class Cat(Animal):
    def print(self):
        print("cat", end=" ")

class Dog(Animal):
    def woof(self):
        print("woof", end="")

animal = Animal()
cat = Cat()
dog = Dog()
animal.print()
cat.print()
dog.print()
# animal cat animal
"""
# MCQ 5
"""
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


digital_edition = Ebook('1984', 'George Orwell', 2)
print(digital_edition.get_info())
# Ebook: 1984 by George Orwell, Size 2MB
"""
# MCQ 6
"""
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
print(car1.get_car_info())
"""

# FRQ 1

class Airplane:
    def __init__(self, model, capacity):
        self.model = model
        self.capacity = capacity

class AirportLog:

    def __init__(self):
        self.airplane_log = {}

    def add_airplane(self, time, model, capacity):
        plane = Airplane(model, capacity)
        if time not in self.airplane_log:
            self.airplane_log[time] = []
        self.airplane_log[time].append(plane)

    def print_airplanes_at_time(self, time):
        for airplane in self.airplane_log[time]:
            print(airplane.model, end=" ")

# Need to do this problem again need to really learn this problem

# port = AirportLog()
# port.add_airplane(1, "delta", 40)
# port.add_airplane(1, "disney", 100)
# port.print_airplanes_at_time(1)

# FRQ 2:

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

class Car(Vehicle):
    def __init__(self, make, model, year, miles_per_gallon):
        super().__init__(make, model, year)
        self.miles_per_gallon = miles_per_gallon

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Miles Per Gallon: {self.miles_per_gallon}")

# new_vehicle = Vehicle("Toyota", "Camry", 2010)
# new_vehicle.display_info()
#
# new_car = Car("Toyota", "Rav4", 2015, 26)
# new_car.display_info()

# FRQ 3

class Book:

    def __init__(self, title, author):

    def get_info(self):

    def is_classic(self):

    def get_num_books(cls):

class FictionBook(Book):

    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre 