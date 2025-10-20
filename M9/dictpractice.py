# Question 1
items = {"never": "gonna", "give": "you", "up": "."}
# print(items[0]) # prints key error because it is a dictionary, dictionaries use keys to access values not numeric indices

# Question 2
dict = {}
numbers = [1, 4, 7, 9]

for i in range(len(numbers)):
    dict[i] = numbers[i] * 2

    """
    The key is dict[i] and the key is numbers[i] * 2 resulting in [dict[i]: numbers[i] * 2] -> {0: 1, 1: 8 ...}
    dict[i] can update the dict to create a new key and assign a value. 
    """

# print(dict[1])

# Question 3
set1 = {1, 2, 3, 4, 5, 6} # assign a set
set2 = {1, 3, 5, 7} # assign a set
set3 = set1.union(set2) # this is merging the list because of the union is creates a new list that is all unique chars or ints
# print(set3) # print {1,2,3,4,5,6,7}

# Question 4
# Select all of the following valid ways to insert the element 123 to the end of a tuple
# tuples are immutable they cannot be changed or updated.

# Question 5
months = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4} # assign a dict
months["May"] = 5 # add a new key:value
# print(months)

# Question 6:
s = {1, 2, 3, 4} # a set can be updated
s.add(5) # [set name].add("#) to update the set

# Coding/Programming Questions

# Question 1

def is_anagram(word_1, word_2):
    word_1_map = {}
    word_2_map = {}

    for char in word_1: # for each character in the word
        word_1_map[char] = 1 + word_1_map.get(char, 0)
        """
         word_1_map[char] = key
         1 + word_1_map.get(char, 0) = value
         word_1_map.get(char, 0) = additional value if present if not 0 as default 
        """

    for char in word_2:
        word_2_map[char] = 1 + word_2_map.get(char, 0)

    return word_1_map == word_2_map

# print(is_anagram("listen", "silent"))
#
# print(is_anagram("pizza", "zzaip"))
#
# print(is_anagram("dj", "khaled"))

# Question 2
def dupe_letter(word):

    letters = set() # creates a set that can be looked into
    list_word = list(word) # creates a list of the string

    for i in range(len(list_word)): # starts a range function from 0 to length of list_word
        if list_word[i] in letters: # if the index spot of list word is in the set
            list_word[i] = "" # change the index spot in the list to empty string
        else: # otherwise
            letters.add(list_word[i]) # add it to the set

    word = ''.join(list_word) # at the end of the for loop join the characters to create a new list with no dupes and join them.

    return word

# print(dupe_letter("hello"))
# print(dupe_letter("aabbccef"))
# print(dupe_letter("thissentencehasdupes"))

# Question 3

def member_attendance(event_attendance):

    event_attendance_map = {}

    for event in event_attendance:
        name = event.split(":")[0].strip()

        event_attendance_map[name] = 1 + event_attendance_map.get(name, 0)

    return event_attendance_map


event_attendance = ["Jack : GBM 1", "John : GBM 1", "Jill : GBM 1", "Jack : GBM 2", "John : GBM 2", "Julie : GBM 2"]
print(member_attendance(event_attendance))

event_attendance = ["Jack : GBM 1", "John : GBM 1", "Jill : GBM 1", "Jack : GBM 2", "John : GBM 2", "Julie : GBM 2", "Jack : GBM 3", "Julie : GBM 3", "Julian : GBM 3"]
print(member_attendance(event_attendance))

event_attendance = ["Jack : GBM 1", "John : GBM 1", "Jill : GBM 1", "Jack : GBM 2", "John : GBM 2", "Julie : GBM 2", "Jack : GBM 3", "Julie : GBM 3", "Julian : GBM 3", "Jack : Pool Party", "John : Pool Party", "Julie : Pool Party"]
print(member_attendance(event_attendance))

