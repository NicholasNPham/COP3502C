# Introduction to Algorithms
"""
Algorithms
- An algorithm is a step-by-step procedure for solving a problem
- Input -> Output -> Definite & Unambiguous

Overview
- Searching:
    - Linear Search
    - Binary Search
- Sorting:
    - Insertion Sort
    - Selection Sort
    - Bubble Sort
- Simulation/Timing
- Big-O Notation
"""
from codecs import make_identity_dict

# Linear Search

"""
Search Problem
- Deals with locating an item in a large collection of Data

Search Algorithm
- Method of locating a specific item in a larger collection of data

The Sequential Search Algorithms
- The sequential or linear search algorithm uses a loop to:
    - Sequentially step through a container
    - Compare each element with the search value
    - Stop when:
        - The value is found
        - The end of the array is encountered
"""
# Example 1
def linearSearch(books, target):
    for i in range(0, len(books)):
        if books[i] == target:
            return i
    return -1

mybooks = ["The Supper Club", '1984', 'Responsive Web Design', 'The Great Gatsby']
# print(linearSearch(mybooks, 'Responsive Web Design'))
# print(linearSearch(mybooks, 'Harry Potter and the Prisoner of Azkaban'))

# Binary Search

"""
Binary Search
- Requires a sorted container
- Starts with the element in the middle of the container
- If the element is the desired value, search is over
- Otherwise, the value in the middle element is either grater or less than the desired value
    - If the value in the middle is greater than the desired value, search in the first half of the container.
    - Otherwise search the second half
- Repeat as needed while adjusting start and end points of the search until you find the value you are looking for or start and end are equal
"""

def binarySearch(buses, target):

    start, end = 0, len(buses) - 1
    mid = (start + end) // 2
    while start <= end:
        if buses[mid] == target:
            return mid
        elif buses[mid] > target:
            end = mid - 1
            mid = (start + end) // 2
            continue
        else:
            start = mid + 1
            mid = (start + end) // 2
            continue
    return -1

buses = [1, 11, 22, 37, 38]
# print(binarySearch(buses, 37))
# print(binarySearch(buses, 17))

def lectureBinSearch(buses, target):
    start, end = 0, len(buses) - 1
    while start <= end:
        mid = (start + end) // 2
        if buses[mid] == target:
            return mid
        elif buses[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

# print(lectureBinSearch(buses, 37))
# print(lectureBinSearch(buses, 17))

# Selection Sort

"""
Selection Sort
- The central idea is to move the smallest element to its correct position, then follow that with the second smallest to its correct postion and so on.

- The smallest value in the container is located and moved to element 0.
- Then the next smallest value is located and moved to element 1.
- This process continues until all the elements have been placed in their proper order

"""

def selectionSort(list):

    for i in range((len(list))):
        min_index = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min_index]:
                min_index = j

        list[i], list[min_index] = list[min_index], list[i]

    return list

# print(selectionSort([5, 2, 88, 23, 6]))

# Bubble Sort

"""
Bubble Sorting
- Compares adjacent Items and exchanges them if they are out of order

Pass
- Denotes one full iteration iteration to reach the end of the container
"""


def bubble_sort(arr):
    """
    Sorts an array using bubble sort and shows each step.

    Args:
        arr: List of comparable elements

    Returns:
        The sorted list
    """
    n = len(arr)
    print(f"Starting array: {arr}\n")

    # Traverse through all array elements
    for i in range(n):
        print(f"Pass {i + 1}:")
        swapped = False

        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(f"  Swapped {arr[j + 1]} and {arr[j]}: {arr}")

        if not swapped:
            print(f"  No swaps needed")
            break
        print()

    return arr

# print(bubble_sort([29, 10, 14, 37, 13]))

# Insertion Sort

"""
Insertion Sort
 - Takes each item from unsorted region and insert into its correct order in sorted region
 
"""


def insertion_sort(arr):
    """
    Sorts an array using insertion sort and shows each step.

    Args:
        arr: List of comparable elements

    Returns:
        The sorted list
    """
    print(f"Starting array: {arr}\n")

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        print(f"Step {i}: Inserting {key}")

        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        print(f"  Result: {arr}\n")

    return arr


# Sort the specific array
numbers = [29, 10, 14, 37, 13]
# result = insertion_sort(numbers)
# print(f"Final sorted array: {result}")

# Algorithmic Analysis

"""
Measuring Efficiency of Algorithms
- How are the algorithms coded?
- What computer you use to run an algorithm?
- What data you feed into the algorithms

Big-O Notation
- Used in Computer Science to describe the performance or time/space complexity of an algorithm. Big-O specifically describes an upper boud on runtime performance or the space used (e.g., in memory or on disk) by an algorithm and represents this performance in terms of the size of input to the algorithm.

Analysis and Big-O Notation
- If Algorithm A requires time proportional to f(n), where n is the size of input to the program,. Algorithm A is said to be of order f(n), which is denoted as O(f(n)).
- The function f(n) is called the algorithm's growth-rate function
- The notation uses the capital letter O to denote order and hence it is called the Big-O Notation.

Common Growth Rate Functions
- Most Common Order of Growth used within Big-O Notation
    - O(1) - Constant Growth - Assign a number to a variable
    - O(log n) - Logarithmic growth - Find an item in a sorted list using binary search
    - O(n) - Linear Growth - Find an item in a list using sequential search
    - O(n log n) - Log-Linear Growth - Some faster sorting algorithm (e.g., merge sort)
    - O(n^2) - Quadratic Growth - Simple sorting algorithm (e.g., bubble sort)
    - O(n^3) - Cubic growth - Deeper nested integration
    - O(a^n) for some a > 1 - Exponential growth - Find the solution to the travelling salesman using dynamic programming
    
"""

# Measuring Efficiency of Algorithms

import time

# start_time = time.perf_counter()
# for i in range(0, 1000000):
#     print("", end="")
# stop_time = time.perf_counter()
# print(f"Total time: {stop_time - start_time:.4f} seconds")

# Examples of Algorithmic Analysis

"""
Growth-Rate Functions
- Properties
    - Ignore low-order terms
    - Ignore a multiplicative constant in the higher-order term
    - You can combine growth-rate functions: O(f(n)) + O(g(n)) = O(f(n) + g(n))
    - These properties imply that you need only an estimate of the time requirement to obtain an algoritm's growth rate.
    

"""

# Compute Big O with Consecutive Operations

def reduce(vals):
    min = vals[0] # O(1)

    for i in range(len(vals)): # O(n)
        if vals[i] < min: # O(1)
            min = vals[i] # O(1)

        for i in range(len(vals)): #O(n)
            vals[i] -= min # O(1)

    return vals # O(1)

    # Total = O(n) not O(2n) because both O(n) are independent of each other

# print(reduce([9, 8, 6, 1, 11]))

# Example 2:

def max_diff(vals): # O(n^2)
    max = 0 # O(1)

    for i in range(0, len(vals)):  # O(n) * lower for loop = O(n)
        for j in range(0, len(vals)): # O(n)
            if abs(vals[i] - vals[j]) > max: # O(1)
                max = abs(vals[i] - vals[j]) # O(1)

    return max

# Analyze Selection Sort

def selection_sort(vals): # O(n^2)

    for i in range(o, len(vals)): # O(n)

        index_min = i # O(1)

        for j in range(i + 1, len(vals)): # O(n)
            if vals[j] < vals[index_min]: index_min = j # O(1)

        vals[index_min], vals[i] = vals[i], vals[index_min] # O(1)

# Analyze Binary Search

"""
PSUDOCODE PSUDOCODE
"""
"""
def bs(b, t):
    s, e = 0, l(b) - 1
    w s <= e:
        m = (s + e) // 2
        if b[m] == t:
            return m
        ef b[m] < t:
            s = m + 1
        es:
            e = m - 1            

Time Complexity is : O(logn)
n/2^K -> n - n/2 -> (n/2)/2 -> ((n/2)/2)/2 

"""

