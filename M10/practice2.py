
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

