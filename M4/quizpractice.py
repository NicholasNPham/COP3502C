# Practice Question 1:
"""
def sum(*args):

    value = 0.0

    for arg in args:
        value += arg

    print(value)

sum(-2.5, 2.5, -1.0, 0.5, 0.5)
"""
# Practice Question 2:
"""
def print_range(start, end):
    start = start
    end = end

    while start < end:
        print(start, end=', ')
        start += 1

    if start == end:
        print(start)

print_range(90,99)
"""
# Practice Question 3:
"""
def sum_of_digits(numbers):
    sum = 0
    for number in str(numbers):
        sum += int(number)

    return sum

print(sum_of_digits(765434567))
"""