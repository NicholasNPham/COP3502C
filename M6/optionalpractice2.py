def parse_student(string):
    studentDict = {}

    studentID = string[:8]
    studentBD = string[-4:]
    studentName = string[8:-4]

    studentDict.update({"id": int(studentID), "name": studentName, "birthdate": studentBD[:2] + "/" + studentBD[2:]})

    return studentDict

print(parse_student("12345678Will Albright0116"))
print(parse_student("87654321Leah Zabad0221"))
print(parse_student("00000001Adrian Moreno0225"))
print(parse_student("00000007Random Student0427"))