"""
RECURSION

Iteration -> Loops
- Executing a set of instructions repeatedly until the condition controlling the loop becomes False.
- While Statements

Recursions
- F(n)
- 0, 1, 1, 2, 3, 5, 8, ...
    - nth -> fib --->, nth
    - fib(n) = fib(n-1) + fib(n-2)
        - fib(n-1) = fib(n-2) + fib(n-3)
        - fib(n-2) = fib(n-3) + fib(n-4)
- Find the base case:
    - fib(0) = 0
    - fib(1) = 1

- A mechanism of solving a computational problem where the solution depends on the solution to smaller instances of the same problem.
- def random(n)
    ------
    ------
    ------ :This is the block of code
    ------
    ------
    random(n) :This is calling the function again in the block of code which is recursions

- A repeated application of recursion
- A recursive algorithm references itself as part of the solution:
    - Has one or more base cases (can be computed without self-reference)
    - Has one or more recurrence relations (self-referencing computation)

- Manually trace recursive calls.
- Develop a recursive solution with a different problem setting.

Base Case:
- Always have a base case and a step that brings you closer to the base case:


"""

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2) # This is the recurrence relation.

# print(fibonacci(3)) # Prints 2

# -------------------------------

"""
Case Study: Vertical Numbers
- Design a recursive function that writes positive numbers to the screen with the digits written vertically
- e.g "1234" can be written
    - 1
      2
      3
      4

- Base Case:
    - if n<10, directly write the number n ot the screen.
- Recurrence Relation (Decompose the task into subtask)
    1. Output all the digits except the last digit.
    2. Output the last digits, which is 4 in this case.

"""
def write_vertical(n):
    if n < 10:
        print(n)
        return

    write_vertical(n // 10)
    print(n % 10)

# print(write_vertical(1234))

def mystery(b, e):
    if e == 0:
        return 1
    else:
        return b * mystery(b, e - 1)

# print(mystery(4, 3))

def magic(n):
    if n < 10:
        return n
    return magic(n // 10) + n % 10

# print(magic(24187))

# Getting the factorial of a number using recursion

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# print(factorial(5))

# Palindrome

def is_palindrome(s):
    if len(s) == 0 or len(s) == 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1: len(s) - 1])
    return False

# print(is_palindrome("madam"))

# Memorization Techniques

def fib(n, dict):
    if n in dict:
        return dict[n]

    if n == 0 or n == 1:
        return n

    dict[n] = fib(n - 1, dict) + fib(n - 2, dict)
    return dict[n]


print(fib(7, {}))