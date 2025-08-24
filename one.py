# f-strings
name = "Nicholas Pham"
stringName = f'My name is {name}'
print(stringName)

# calling round (round function is also known as banker's round)
a = 2.5
b = 3.5
print(round(a))
print(round(b))

# the modulo operator %
intOne = 10
intTwo = 3
print(intOne % intTwo) # the remainder of this equation is 1 printing 1

# Using int() and float()
first = float(input("First number: "))
second = float(input("Second number: "))
print(first + second)

# Practice Problem: Write a program to calculate the final grade of the course
test = float(input("Test Score Average: "))
quiz = float(input("Quiz Score Average: "))
assignment = float(input("Assignment Score Average: "))
project = float(input("Project Score Average: "))

finalGrade = test * .4 + quiz * .3 + assignment * .1 + project * .2
print(finalGrade)

"""
this is very fundamental comparing to the project posted on this github especially comparing to the notionAIOptimizer project, good to learn fundamentals on an institutional level though.
"""