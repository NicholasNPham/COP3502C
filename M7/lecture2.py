"""
Tuples:
- A tuple (immutable) is a sequence of comma-separated values. Typically, tuples are surrounded with parentheses ().

Tuples - Unpacking:
- A tuple (immutables) is a sequence of comma-separated values. Typically, tuples are surrounded with parentheses.

Sequence Operations:
- Sequence-type functions are built-in functions that operates on sequences like lists, tuples and strings.
    - + : combines two sequences
    - * : repeats a sequence multiple times
    - in : check in membership
    - [] : indexing and slicing
    - len(seq) : return the number of elements in seq
    - sum(seq) : return the sum of all elements in seq
    - min(seq), max(seq) : returns the min and max values in seq
    - seq.count(x) : return the number of occurrences of x
    - seq.index(x) : return the index of the 1st occurrence of x

Sequence Iterations:
- Iterating through a sequence(e.g. list, tuple, string, range) to access each element of the sequence using for loops. The built-in enumerate() function iterates over a sequence and provides an iteration counter.

Dictionary:
- Dictionary associates key with values. Keys must be of an immutable type
- Note: A dictionary key is unique - attempting to create a new entry that already exists in the dictionary replaces the existing entry

Dictionary Iteration:
- dict.items() returns (key, value) tuples.
- dict.keys() returns dictionary keys.
- dict.values() returns dictionary values.

Dictionary Methods:
- Dictionary methods can perform some useful operations, such as adding or removing element, obtaining all the keys ore values in the dictionary, merging dictionaries, etc.
    - get(key, default): Reads the value of the key, if the key does not exist in the dictionary, then returns default
    - dict1.update(dict2): Merges two dictionaries. Existing entries in dict1 are overwritten if the same key exists in dict2
    - pop(key, default): Removes and returns the key value. If key does not exist, Then return default.

Sets:
- Sets is an unordered collection of unique elements. A set can be written using curly braces {} with commas separating set elements
- Note: an empty set can only be created using set(). Then index operand

Modifying Sets:
- Sets are mutable. We could add, remove elements

Membership Operators:
- The in and not in operators which are also known as membership operators are used to determine whether a specific value can be found within a container, such as a list, a string, or a range.

Identity Operators:
- The is and is not operators which are also known as identity operators, are used to determine whether two variables are bound to the same object.

"""
# Tuples Example 1:
"""
a = [15, 67, 89, 45]
a[1] = 100
print(a)

# b = (15, 67, 89, 45)
# b[1] = 100
# print(b) # print Type Error: 'tuple' object does not support item assignment.

c = 12, 34, 56
d = (12, 34, 56)
print((type(c), type(d))) # print <class 'tuple'>, <class 'tuple'>

e = (12, 45, 56)
f = (24, 89)
g = e + f
print(g) # prints (12, 45, 56, 24, 89)
print(g[0]) # prints 12
print(list(g)) # prints [12, 45, 56, 24, 89]
"""
# Tuples Example 2:
"""
my_tup = (12, 45, 67, 98)
a, b, c, d = my_tup
print(a, b, c, d) # prints 12 45 67 98
# e, f = my_tup # prints ValueError: too many values to unpack (expected 2)
g, *h = my_tup
print(g, h) # prints 12 [45, 67, 98]
*i, j = my_tup
print(i, j) # prints [12, 45, 67] 98
k, *l, m = my_tup
print(k, l, m) # prints 12 [45, 67] 98
# *n, *o, p = my_tup
# print(n, o, p) #prints SyntaxError: multiple starred expressions in assignment
"""
# Tuples Example 3:
"""
print(len((2, 3, 4, 5, 6))) # prints 5
print(min((2, 3, 4, 5, 6))) # prints 2
print(max((2, 3, 4, 5, 6))) # prints 6
print((1, 2, 2, 3, 2).count(2)) # prints 3
print((34, 12, 45, 56, 87).index(12))
print((34, 45, 56, 78, 12, 12).index(12)) # will only print 12 because of the 4th index.
"""
# Sequence Iterations Example 1:
"""
my_list = [1, 2, 3, 4, 5]

for item in my_list:
    print(item, end=" ")
print()

for index, item in enumerate(my_list):
    print(f'Index: {index}, Item: {item}')
"""
# Dictionaries
"""
my_dict = {"name": "Nick", "age": 23, "address": "Florida"}
print(my_dict) # prints {'name': 'Nick', 'age': 23, 'address': 'Florida'}
print(my_dict["name"]) # prints Nick

my_dict["name"] = "John"
print(my_dict) # prints {'name': 'John', 'age': 23, 'address': 'Florida'}

my_dict["profession"] = "Student"
print(my_dict) # prints {'name': 'John', 'age': 23, 'address': 'Florida', 'profession': 'Student'}

del my_dict["age"]
print(my_dict) # prints {'name': 'John', 'address': 'Florida', 'profession': 'Student'}
"""
# Set Example

a = {}
print(type(a)) # prints <class 'dict'>
a = {1, 2, 3, 4, 4, 5}
print(a) # prints {1, 2, 3, 4, 5}
print(type(a)) # prints <class 'set'>

a = {1, 2, 3}
b = set([4, 5, 6])
c = a.union(b)
print(a, b, c) # prints {1, 2, 3} {4, 5, 6} {1, 2, 3, 4, 5, 6}

a = {2, 3, 4}
b = {3, 4, 5}
e = a.intersection(b)
print(a, b, e) # prints {2, 3, 4} {3, 4, 5} {3, 4}

h = a.difference(b)
print(a, b, h) # prints {2, 3, 4} {3, 4, 5} {2}
