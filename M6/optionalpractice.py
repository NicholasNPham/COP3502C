def bin(number):
    num = number
    binary = []
    res = ""

    if number == 0:
        return "0"
    else:
        while num > 0:
            binary.append(num % 2)
            num //= 2

        for b in range(len(binary) -1, -1, -1):
            res += str(binary[b])

        return res

# print(bin(10))      # Should output: 1010
# print(bin(42))      # Should output: 101010
# print(bin(0))       # Should output: 0
# print(bin(255))     # Should output: 11111111
# print(bin(12))      # Should output: 1100

# def capitalize(string):
#     original = string
#     formattedOriginal = ""
#
#     for char in original:
#         if ord(char) == 32:
#             formattedOriginal += chr(ord(char))
#         elif ord(char) <= 90:
#             formattedOriginal += chr(ord(char) + 32)
#         else:
#             formattedOriginal += chr(ord(char))
#
#     return formattedOriginal
#
#
# print(capitalize("heLLO OTHer uSer weLcomE"))

def capitalize(string):
    newList = []
    res = ""

    firstList = string.split(" ")
    for word in firstList:
        char = list(word)
        newList.append(char)

    for subList in newList:
        if ord(subList[0]) < 97:
            first = chr(ord(subList[0]) + 32)
        else:
            first = subList[0]


        if ord(first) in [111, 117, 115, 110, 100]:
            res += first
        else:
            res += chr(ord(first) - 32)

        for char in subList[1:]:
            if ord(char) < 97:
                res += chr(ord(char) + 32)
            else:
                res += char
        res += " "

    return res

# print(capitalize("heLLO OTHer uSer weLcomE")) #returns “Hello other user Welcome”
# print(capitalize("SIZE OF DESK")) #returns “size of desk”
# print(capitalize("NEW dRUMs foR SAlE")) #returns “new drums For sale”
# print(capitalize("this is a cool sentence")) #returns “This Is A Cool sentence”

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def partition(ls, amount):
    i = 0
    j = amount
    board = []

    for n in range(0, len(ls), amount):
        board.append(numbers[n: n + amount])

    return board

# print(partition(numbers, 3)) # Should output: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
# print(partition(numbers, 5)) # Should output: [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
# print(partition(numbers, 2)) # Should output: [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
