"""
Software Engineering

Assertions
- Assert statements in Python are used for debugging and testing purposes.
- They are typically used to check if certain conditions or assumptions about  the code are true. If not, they raise an AssertionError to indicate that something unexpected has happened.
- They can be used for checking pre- and post-conditions, validating function arguments and checking invariants.
- Assertions are statements that is used to set sanity check during the development process. The assert keyword is used in python for assertions.

Exception Handling
- In Python, the try and a except statements are used for exception handling. They allow you to catch and handle exceptions (errors) that may occur during a program's execution.
- The try block contains the code that might raise an exception, and the except block specifies the code to be executed if a particular exception occurs.
- Python uses the try and except construct of exception handling.

Common Exceptions
- Some Python Built-in Exceptions
    - EOFError: input() hits an end-of-file condition (EOF) without reading any input
    - KeyError: A dictionary key is not found in the set of keys
    - ZeroDivisionError: Divide by zero Error
    - ValueError: Invalid Value (e.g., input mismatch)
    - IndexError: Index out of bounds

Multiple Exception Handlers
- Multiple exception handlers can be added to a try block by adding additional except blocks and specifying the specific type of exceptions.

Raising Exceptions
- A raise statement causes immediate exit from the try block and execution exception handler.

Unit Test
- Unit testing is a software testing method by which each individual units of code are put under various tests to determine whether they are fit for use.

Version Control: Why?
- Because programmers are awesome brilliant and Human and must work together.
- We must plan to fail. Version control (revision control, source control) protects us from our own stupidity and faulty nature by storing changes.

Version Control Basics:
- Version Control
    - Is based on commits
    - can have branches
    - support merges

Git: Distributed Version Control
- Git is a distributed version control system.
    - Everyone has a copy of the repository
    - May or may not have central repository
    - Commits are local until they are pushed
    - "Commit early and often" (low cost)

Distributed VCS: Clone
- A Clone operation makes a copy of a repository locally.
Distributed VCS: Commit
- Performing a commit creates a changeset from one version to another.
Distributed VCS: Push
- A push operation pushes any changes up to a remote repository
Distributed VCS: Pull
- A pull operation pulls down any changes made to the remote repository



"""
# Assertion Example
a = 12
b = 0
# assert b != 0
# print("The division is: ", a/b)

# Assertion Example 2
def calculate_average(numbers):
    assert len(numbers) > 0, "The list cannot be empty"
    total = sum(numbers)
    average = total / len(numbers)
    assert average >= 0, "The average cannot be negative"
    return average

# print(calculate_average([]))

# Exception Handling
"""
try:
    a = 12
    b = 0
    print("The result of division: ", a/b)
except:
    print("Zero Division Error")
"""

# Raising Exception
print("Welcome to the number guessing game!")
print("Enter a positive number: ", end="")
"""
try:
    guess = int(input())
    if guess < 0:
        raise ValueError("Invalid guess.")
except ValueError as error:
    print("Caught ValueError:", str(error))
except Exception as error:
    print("Caught unknown error:", str(error))
"""

