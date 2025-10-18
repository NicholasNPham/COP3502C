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

def temperature():

    temps = []
    while len(temps) < 7:
        temps.append(input("Temperatures: "))

    average = 0
    for temp in temps:
        average += int(temp)
    average /= len(temps)

    print(f"Average Temperature: {average:.2f}°C")
    print(f"Highest Temperature: {max(temps)}")
    print(f"Lowest Temperature: {min(temps)}")

    if average < 15:
        print("It's quite cold. Consider indoor activities.")
    elif 15 < average < 25:
        print("Perfect weather for outdoor activities like hiking.")
    else:
        print( "It's warm. A good time for swimming or beach visits.")

# temperature()

# Question 2:
def find_mountains(mountain_list, min_height):

    acceptable_heights = []

    for mountain_height in mountain_list:
        if mountain_height >= min_height:
            acceptable_heights.append(mountain_height)

    print(acceptable_heights)

# find_mountains([25, 50, 10, 12, 23, 7, 27], 23)
# find_mountains([1, 4, 6, 7], 12)
# find_mountains([10, 22, 9], 20)

# Question 3:
def remove_four(numbers):

    string_numbers = []
    for number in numbers:
        string_numbers.append(str(number))

    result = []

    for i in range(len(string_numbers)):
        if string_numbers[i] == 4:
            result.append("replaced")
        elif len(string_numbers[i]) > 1 and "4" in string_numbers[i]:
            result.append("replaced")
        else:
            result.append(numbers[i])


    return result

print(remove_four([1,2,45,54,99]))
print(remove_four([5,34,44,67,45,87]))
print(remove_four([94]))