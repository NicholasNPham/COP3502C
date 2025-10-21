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

