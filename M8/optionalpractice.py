def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

# print(factorial(1))

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)

# print(fib(1))

def sumOfDigits(n):
    if n == 0:
        return 0
    return sumOfDigits(n // 10) + n % 10

# print(sumOfDigits(991))

def reverse_string(string):
    if len(string) == 0:
        return string
    return string[-1] + reverse_string(string[:-1])

# print(reverse_string("i am a caterpillar"))

def countVowels(string):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    if len(string) == 0:
        return 0

    if string[-1] in vowels:
        return 1 + countVowels(string[:-1])
    else:
        return countVowels(string[:-1])

# print(countVowels("PYTHON PROGRAMMING"))

def nested_sum(nest):
    if nest == []:
        return 0

    if isinstance(nest[0], int):
        return nest[0] + nested_sum(nest[1:])
    else:
        return nested_sum(nest[0]) + nested_sum(nest[1:])

print(nested_sum([[1, 2], [3, [4, [5, 6]]], [7, [8, [9, [10]]]]]))








