# Question 1

def count(x):
    if x == -1:
        return
    print(x, end=" ")
    count(x - 1)

# count(5) # Should print 5 4 3 2 1 0

# Question 2
def reverse_print(n):
    if n == 0:
        return
    reverse_print(n - 1)
    print(n, end=" ")

# reverse_print(3) # should print 1 2 3

# Question 3
def count(n):
    if n == 0:
        return n
    else:
        return count(n - 1)

# print(count(-5)) # RecursionError: Infinite Loop

# Question 4
def sum_even(n):
    if n % 2 == 0:
        return n + sum_even(n-2)
    else:
        return sum_even(n - 1)

# print(sum_even(11)) # results in error

# Question 5
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

# print(fact(4)) # prints 24

# Programming Questions

# Question 1
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# print(factorial(4))
# print(factorial(5))
# print(factorial(1))

# Question 2

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(5))
# print(fibonacci(7))
# print(fibonacci(1))

# Question 3:

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        last = n % 10
        return last + sum_of_digits(n // 10)

# print(sum_of_digits(123))
# print(sum_of_digits(1234))
# print(sum_of_digits(991))

# Question 4:

def reverse_string(string):
    if len(string) == 0:
        return ""
    else:
        return string[-1] + reverse_string(string[:-1])

# string = "hello world!"
# print(reverse_string(string))
#
# string = "COP3502C"
# print(reverse_string(string))
#
#
# string = "i am a caterpillar"
# print(reverse_string(string))

# Question 5:

def count_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', "A", "E", "I", "O", "U"]

    if len(string) == 0:
        return 0
    else:
        if string[0] in vowels:
            return 1 + count_vowels(string[1:])
        else:
            return count_vowels(string[1:])

# print(count_vowels("cat"))
# print(count_vowels("Hello World"))
# print(count_vowels("PYTHON PROGRAMMING"))

# Question 6:

def nested_sum(nest):
    if nest == []:
        return 0

    if isinstance(nest[0], int):
        return nest[0] + nested_sum(nest[1:])
    else:
        return nested_sum(nest[0]) + nested_sum(nest[1:])

print(nested_sum([1, [], 2, [3, 4], [5, [6, 7]]]))
print(nested_sum([[1, 2], [3, [4, [5, 6]]], [7, [8, [9, [10]]]]]))
print(nested_sum([1, [2, [3, [4], 5], [6, [7, [8], 9], 10], 11], 12]))