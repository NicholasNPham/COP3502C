# Question 1
items = [1, 2, 3, 4, 5] # define a list
items[2] = "three" # change index 2 to "three"
# print(items) # prints [1, 2, 'three', 4, 5]
"""
The first line is missing an equal sign. 
"""

# Question 2
x = [1, 2, 3] # define the list
y = x # y now equals x which is the list
x = 2 # now x is attached to 2 forgets the lists
# print(y, x) # prints [1, 2, 3] 2

# Question 3:
x = ["hello", 2, ["first", "second"]] # defines the list with a list nested in the list
# print(x[0], x[2][1] * x[1]) # prints hello secondsecond

# Question 4:
numbers = [10, 20, 30, 40, 50] # defines the list
numbers.append(60) # appends the int 60 to the end of the list
numbers.insert(2, 25) # 2 is the index (which is now between 20, 30) and the int added is 25 creating the list [10, 20, 25, 30, 40, 50, 60]
# print(sum(numbers)) # the sum function adds all the numbers in the list printing 235

# Question 5:
message = "Hi, welcome to Chili's" # assign a string variable to the string created
# print(message[-5:2:-2]) # [start, stop, step] -> [-5, 2] meaning [ welcome to Chi] the step iterates backwards starting from -5 [iCo mce]

# Question 6:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # define a nested list which is a matrix
result = [row[1] for row in matrix if row[1] % 2 == 0]
"""
for row in matrix:
    if row[1] % 2 == 0:
        print(row) in list 
        
it is a one line for loop with a if condition printing in a list resulting in [2, 8]
"""
# print(result)

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

# print(remove_four([1,2,45,54,99]))
# print(remove_four([5,34,44,67,45,87]))
# print(remove_four([94]))

# Question 4:
def find_prime_factors(n):

    prime_list = [] # empty list to store all prime numbers of n
    prime_factors = [] # empty list to iterate prime list to get unique numbers only
    count = 2 # Starting off if n is modulo of 2

    while n > 1: # while function to stop n from going past 1 downwards
        if n % count == 0: # if n modulo count in iteration
            prime_list.append(count) # append the number if it is modulo
            n /= count # divide the number by the count
        else:
            count += 1 # if it isn't then raise the count my 1 and continue until n is zero

    for num in prime_list: # iterate through the prime list
        if num not in prime_factors: # if the num is not in prime list
            prime_factors.append(num) # append it otherwise skip

    print(prime_factors) # print the list.

# find_prime_factors(100)
# find_prime_factors(29)
# find_prime_factors(56)

# Question 5
def higher_course_level(courses1, courses2):

    course_1_integers = [] # assign a empty list to a variable
    for i in range(len(courses1)): # count step for i with a range of the list from 0 to len(course1)
        if len(courses1[i]) == 7: # if the string count results in 7 "XXXXXXX"
            course_1_integers.append(int(courses1[i][3:])) # strip the letters and keep the numbers and turn it into an int
        else: # if the string count is not 7 looking for 8
            course_1_integers.append(int(courses1[i][3:7])) # strip the letters and keep the numbers and turn it into an int

    course_2_integers = []
    for i in range(len(courses2)):
        if len(courses2[i]) == 7:
            course_2_integers.append(int(courses2[i][3:]))
        else:
            course_2_integers.append(int(courses2[i][3:7]))

    average_1 = sum(course_1_integers) / len(course_1_integers) # find the average when the sum of list and then len of list
    average_2 = sum(course_2_integers) / len(course_2_integers)

    if average_1 > average_2: # if average_1 is higher than average_2 print 1
        print(1)
    elif average_1 < average_2: # if average 1 is less than average_2 print 2
        print(2)
    else: # if they are the same thing print 0
        print(0)

# higher_course_level(["ABC1000", "ABC2000C", "ABC2000C", "ABC2000"], ["ABC1500", "ABC2050C", "ABC2004C", "ABC2003"])
# higher_course_level(["COP3502C", "MAC2313", "IDS2935", "COT3100", "PHY2048"], ["MAC2311", "COP3504C", "IDS2935", "COT3100", "PHY2048"])
# higher_course_level(["COP3502C", "MAC2313", "CDA3101", "EEL4712C"], ["MAC2311", "COP3504C", "IDS2935", "COT3100", "EEL3701C"])

# Question 6:
def unique_in_order(seq):

    unique_list = []
    for char in seq:
        if char not in unique_list:
            unique_list.append(char)

    print(unique_list)

unique_in_order("AAAABBBCCDAABBB")
unique_in_order("ABBCcAD")
unique_in_order("12233")