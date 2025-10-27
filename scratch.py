"""
THIS SCRATCH PAPER DO NOT DELETE
"""

class Employee:

    def __init__(self, first = "Matthew", last):

        self.first = first

        self.last = last

emp = Employee("Tom", "Smith")

emp.first = "Tim"

print(emp.first)
