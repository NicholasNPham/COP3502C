def parse_student(string):
    studentDict = {}

    studentID = string[:8]
    studentBD = string[-4:]
    studentName = string[8:-4]

    studentDict.update({"id": int(studentID), "name": studentName, "birthdate": studentBD[:2] + "/" + studentBD[2:]})

    return studentDict

# print(parse_student("12345678Will Albright0116"))
# print(parse_student("87654321Leah Zabad0221"))
# print(parse_student("00000001Adrian Moreno0225"))
# print(parse_student("00000007Random Student0427"))

def count_items(mylist):
    dictionary = {}

    for item in mylist:
        dictionary[item] = dictionary.get(item, 0) + 1

    return dictionary

# print(count_items([1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3]))
# print(count_items(["a", "b", "c", "a", "aa", "c", "hello"]))
# print(count_items([0, 5, 4, 6, 5, 5, 9, 5, 4, 4, 8, 8, 9, 4, 9]))
# print(count_items("hello world"))