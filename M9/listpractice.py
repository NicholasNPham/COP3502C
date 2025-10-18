# Question 1
items = [1, 2, 3, 4, 5] # define a list
items[2] = "three" # change index 2 to "three"
print(items) # prints [1, 2, 'three', 4, 5]
"""
The first line is missing an equal sign. 
"""

# Question 2
x = [1, 2, 3] # define the list
y = x # y now equals x which is the list
x = 2 # now x is attached to 2 forgets the lists
print(y, x) # prints [1, 2, 3] 2

# Question 3:
x = ["hello", 2, ["first", "second"]] # defines the list with a list nested in the list
print(x[0], x[2][1] * x[1]) # prints hello secondsecond

# Question 4:
numbers = [10, 20, 30, 40, 50] # defines the list
numbers.append(60) # appends the int 60 to the end of the list
numbers.insert(2, 25) # 2 is the index (which is now between 20, 30) and the int added is 25 creating the list [10, 20, 25, 30, 40, 50, 60]
print(sum(numbers)) # the sum function adds all the numbers in the list printing 235

# Question 5:
message = "Hi, welcome to Chili's" # assign a string variable to the string created
print(message[-5:2:-2]) # [start, stop, step] -> [-5, 2] meaning [ welcome to Chi] the step iterates backwards starting from -5 [iCo mce]

# Question 6:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # define a nested list which is a matrix
result = [row[1] for row in matrix if row[1] % 2 == 0]
"""
for row in matrix:
    if row[1] % 2 == 0:
        print(row) in list 
        
it is a one line for loop with a if condition printing in a list resulting in [2, 8]
"""
print(result)

### List Programming Questions
