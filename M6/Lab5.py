def hex_char_decode(digit):
    if digit.upper() == "A":
        value = 10
    elif digit.upper() == "B":
        value = 11
    elif digit.upper() == "C":
        value = 12
    elif digit.upper() == "D":
        value = 13
    elif digit.upper() == "E":
        value = 14
    elif digit.upper() == "F":
        value = 15
    else:
        value = int(digit)

    return value

def hex_string_decode(hex): #0xB5AD34
    if hex[1] == 'x' or hex[1] == 'X':
        hex = hex[2:]
    else:
        hex = hex

    sum = 0
    i = len(hex) - 1
    while i > 0:
        for num in hex:
            sum += hex_char_decode(num) * (16 ** i)
            i -= 1
    return sum

def binary_string_decode(binary):
    if binary[1] == 'b' or binary[1] == 'B':
        binary = binary[2:]
    else:
        binary = binary

    sum = 0
    i = len(binary) - 1
    while i > 0:
        for num in binary:
            sum += int(num) * (2 ** i)
            i -= 1
    return sum

def binary_to_hex(binary):
    if binary[1] == 'b' or binary[1] == 'B':
        binary = binary[2:]
    else:
        binary = binary

    groupBinary = []

    hex = ""
    length = len(binary)
    for num in range(length, 0, -4):
        res = binary[max(0, num-4):num]
        if len(res) == 3:
            res = "0" + res
        elif len(res) == 2:
            res = "00" + res
        elif len(res) == 1:
            res = "000" + res

        groupBinary.append(res)

    for i in range(len(groupBinary) - 1, -1, -1):
        convertedNum = binary_string_decode(groupBinary[i])
        if convertedNum >= 10:
            hex += chr(65 + (convertedNum - 10))
        else:
            hex += str(convertedNum)



    return hex



def main():
    while True:
        print("\nDecoding Menu\n-------------\n1. Decode hexadecimal\n2. Decode binary\n3. Convert binary to hexadecimal\n4. Quit")
        option = input("Please enter an option: ")
        if option == "1":
            start = input("Please enter the numeric string to convert: ")
            res = hex_string_decode(start)
            print(f'Result: {res}')
            continue
        elif option == "2":
            start = input("Please enter the numeric string to convert: ")
            res = binary_string_decode(start)
            print(f'Result: {res}')
            continue
        elif option == "3":
            start = input("Please enter the numeric string to convert: ")
            res = binary_to_hex(start)
            print(f'Result: {res}')
            continue
        elif option == "4":
            print("Goodbye!")
            break
        else:
            print("enter valid option")





if __name__ == "__main__":
    main()