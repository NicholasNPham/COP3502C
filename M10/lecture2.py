"""
Operator Overloading
- Methods - Overloaded Operator
    - __it__(self, other) - Less than <
    - __le__(self, other) - Less than or equal to <=
    - __gt__(self, other) - Greater >
    - __ge__(self, other) - Greater than or equal to >=
    - __eq__(self, other) - Equal to ==
    - __ne__(self, other) - Not equal to !=


"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self): # This is implicitly invoked now
        return f'{self.name} is {self.age} years old'

p1 = Person("Alice", 30)
# print(p1) # can be used to call p1 alone
# print(p1.__str__()) # does not need __str__ now

class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.isbn == other.isbn


b1 = Book("Programming", 123)
b2 = Book("Programming", 123)
# print(b1 == b2) # Was False because of no __eq__ now it is True

# b3 = b1
# print(b1 == b3)

class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.name < other.name

    def __str__(self):
        return f"{self.name} - {self.age} - {self.major}"

    def __repr__(self):
        return self.__str__()

student1 = Student("Jose", 21, "Biology")
student2 = Student("Rob", 18, "Env, Sciences")
student3 = Student("Kevin", 20, "Computer Science")
stud = [student1, student2, student3]
stud.sort()
# print(stud)

# Practice Problem

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
print(n == m) # Prints Hi \n 123
print(m == n) # This will check if it as an __init in either one
