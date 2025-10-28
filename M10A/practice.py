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

# Programming Questions
# Programming Question 1:

class Airplane:
    def __init__(self, model, capacity):
        self.model = model
        self.capacity = capacity

class AirportLog:
    def __init__(self):
        self.logbook = {}

    def add_airplane(self, time, model, capacity):
        plane = Airplane(model, capacity)
        if time not in self.logbook:
            self.logbook[time] = []
        self.logbook[time].append(plane)

    def print_airplanes_at_time(self, time):
        for airplane in self.logbook[time]:
            print(airplane.model, end= " ")

port = AirportLog()
port.add_airplane(1, "delta", 40)
port.add_airplane(1, "disney", 100)
# port.print_airplanes_at_time(1)

# Programming Question 2
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}\n\nModel: {self.model}\n\nYear: {self.year}")

class Car(Vehicle):
    def __init__(self, make, model, year, mpg):
        super().__init__(make, model, year)
        self.mpg = mpg

    def display_info(self):
        super().display_info()
        print(f"\nMiles Per Gallon: {self.mpg}")


new_vehicle = Vehicle("Toyota", "Camry", 2010)
# new_vehicle.display_info()
new_car = Car("Toyota", "Rav4", 2015, 26)
# new_car.display_info()

# Programming Question 3:
class Book:

    id_counter = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.id_counter += 1
        self.id = Book.id_counter

    def get_info(self):
        return f"ID: {self.id}, Title: {self.title}, Author: {self.author}"

    @staticmethod
    def is_classic(title):
        return "a" in title.lower()

    @classmethod
    def get_num_books(self):
        return Book.id_counter

class FictionBook(Book):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre

    def get_info(self):
        return f"{super().get_info()}, Genre: {self.genre}"

class NonFictionBook(Book):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre

    def get_info(self):
        return f"{super().get_info()}, Genre: {self.genre}"

# book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
# print(book1.get_info())
# book2 = Book("The Hunger Games", "Suzanne Collins")
# print(book2.get_info())
# print("Number of Books:", Book.get_num_books())
#
# fiction_book1 = FictionBook("1984", "George Orwell", "Dystopian")
# print(fiction_book1.get_info())
# print("Is Classic:", Book.is_classic(fiction_book1.title))
#
# nonfiction_book1 = NonFictionBook("A Brief History of Time", "Stephen Hawking", "Science")
# print(nonfiction_book1.get_info())
# print("Is Classic:", Book.is_classic(nonfiction_book1.title))




