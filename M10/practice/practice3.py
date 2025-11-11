# MCQ 1
"""
For the following list, how will the list elements look after the 3rd pass of bubble sort?
[12, 1, 98, 37, 29, 7, 10]
"""
# Notes on Bubble Sort
"""
Bubble Sort starts off with the two first indices:
Swap if the right is greater than the left or if left is less than the right
then the next two including the left than repeat
each pass is one full iteration of the whole list
"""
# Answer:
"""
[12, 1, 98, 37, 29, 7, 10]

After 3 Pass
[1, 12, 7, 10, 29, 31, 98]
"""

# MCQ 2
"""
What will the following list look like after 2 passes of selection sort?
[5, 19, 1, 55, 30, 23, 28]
"""
# Notes on Selection Sort
"""
Selection sort is iteration through the list and then swapping in the left or 0th most index
then on the next index find the second lowest and swap in the next 0th most index
"""
# Answer:
"""
[1, 5 19, 55, 30, 23, 28]
"""
# MCQ 3
"""
How many passes of binary search are required for the list [1, 4, 10, 15, 29, 55, 56] and key = 4?
"""
# Notes on Binary Search:
"""
Binary Search is splitting the list in have and to see if its in either the left or right split.
continue splitting until the left, middle, right is the key to look for.
"""
# Answer:
"""
A. 2 passes
"""
# MCQ 4
"""
What is the time complexity of the following code snippet?
for i in range(0, 100):
   print(i * i)
"""
# Answer:
"""
Because the range is set between two variables, it will constantly run the same amount of time.
resulting in n(1) because its a constant run time every single time. 
"""
# MCQ 4
"""
What is the time complexity of the following code snippet?
for i in range(0, n):
   for j in range(0, n // 2):
       print(i + j)
"""
# Answer
"""
for i in range(0, n):            O(n)
   for j in range(0, n // 2):    O(n // 2)
       print(i + j)              O(n * n // 2) -> O(n^2)
"""
# MCQ 5
"""
The time complexity of this code snippet is O(log n) because we are multiplying by 2 each iteration,
therefore we are doing fewer and fewer steps as n gets bigger, so it’s efficient because the time grows slowly
"""

#FRQ 1

def linear_search(items, key):
    for num in items:
        if num == key:
            return True
    return False

# print(linear_search([1, 2, 5, 3, 10], 3))

def selection_sort(items):
    for i in range(0, len(items)):

        index_min = i

        for j in range(i + 1, len(items)):
            if items[j] < items[index_min]:
                index_min = j

        items[index_min], items[i] = items[i], items[index_min]

    return items

# print(selection_sort([4, 1, 7, 10, 5, 2]))

def bubble_sort(items):
    for i in range(len(items)):
        print(f"bubble sort pass {i + 1}")
        for j in range(0, len(items) - i - 1):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
                print(items)

    return items

print(bubble_sort([10, 5, 15, 20, 1, 9]))