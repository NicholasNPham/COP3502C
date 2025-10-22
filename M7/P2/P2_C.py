from importlib.metadata import pass_none

import console_gfx as console_gfx

# console_gfx.display_image(console_gfx.test_rainbow)

def display_menu():
    print("\nRLE Menu\n"
          "--------")
    print("0. Exit")
    print("1. Load File")
    print("2. Load Test Image")
    print("3. Read RLE String")
    print("4. Read RLE Hex String")
    print("5. Read Data Hex String")
    print("6. Display Image")
    print("7. Display RLE String")
    print("8. Display Hex RLE Data")
    print("9. Display Hex Flat Data\n")


def to_hex_string(data):
    string = ""

    for num in data:
        if num == 10:
            string += "a"
        elif num == 11:
            string += "b"
        elif num == 12:
            string += "c"
        elif num == 13:
            string += "d"
        elif num == 14:
            string += "e"
        elif num == 15:
            string += "f"
        else:
            string += str(num)

    return string

def count_runs(flat_data):
    count = 1
    streak = 0

    for i in range(len(flat_data)-1):
        if flat_data[i] != flat_data[i+1]:
            streak = 0
            count += 1
        else:
            if flat_data[i] == flat_data[i+1]:
                streak += 1
                if streak % 15 == 0:
                    streak = 0
                    count += 1
    return count


def encode_rle(flat_data):
    list = []
    count = 1

    for i in range(len(flat_data) - 1):
        if flat_data[i] == flat_data[i + 1]:
            count += 1
            if count % 15 == 0:
                list.append(count)
                list.append(flat_data[i])
                count = 0
        else:
            list.append(count)
            list.append(flat_data[i])
            count = 1

    list.append(count)
    list.append(flat_data[-1])

    return list

def get_decoded_length(rle_data):
    sum = 0

    for i in range(len(rle_data)):
        if i % 2 == 0:
            sum += rle_data[i]

    return sum

def decode_rle(rle_data):
    decodedList = []

    for i in range(0, len(rle_data), 2):
        count = rle_data[i]
        value = rle_data[i + 1]
        for c in range(count):
            decodedList.append(value)

    return decodedList

def string_to_data(data_string):

    list = []

    for i in data_string:
        if i.isdigit():
            list.append(int(i))
        else:
            if i == "a":
                list.append(10)
            elif i == "b":
                list.append(11)
            elif i == "c":
                list.append(12)
            elif i == "d":
                list.append(13)
            elif i == "e":
                list.append(14)
            elif i == "f":
                list.append(15)

    return list

def to_rle_string(rle_data):
    if len(rle_data) == 0:
        return ""
    else:

        if rle_data[1] == 10:
            rle_data[1] = "a"
        elif rle_data[1] == 11:
            rle_data[1] = "b"
        elif rle_data[1] == 12:
            rle_data[1] = "c"
        elif rle_data[1] == 13:
            rle_data[1] = "d"
        elif rle_data[1] == 14:
            rle_data[1] = "e"
        elif rle_data[1] == 15:
            rle_data[1] = "f"

        if len(rle_data) == 2:
            return str(rle_data[0]) + str(rle_data[1])
        else:
            return str(rle_data[0]) + str(rle_data[1]) + ":" + to_rle_string(rle_data[2:])

def string_to_rle(string):
    stringRunValueList = []
    runValueList = []

    hexadecimalDict = {"a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}

    runValue = string.split(":")

    for section in runValue:
        if len(section) == 3:
            stringRunValueList.append(section[:2].lower())
            stringRunValueList.append(section[-1].lower())
        else:
            stringRunValueList.append(section[:1].lower())
            stringRunValueList.append(section[-1].lower())

    for num in stringRunValueList:
        if num in hexadecimalDict:
            runValueList.append(hexadecimalDict[num])
        else:
            runValueList.append(int(num))

    return runValueList

def main():
    print("Welcome to the RLE image encoder!")
    print("Displaying Spectrum Image:")
    console_gfx.display_image(console_gfx.test_rainbow)
    while True:
        display_menu()
        option = int(input("Select a Menu Option: "))
        if option == 0:
            break

        elif option == 1:
            filename = input("Enter name of file to load: ")
            image_data = console_gfx.load_file(filename)

        elif option == 2:
            image_data = console_gfx.test_image
            print("Test image data loaded.")

        elif option == 3:
            input_data = input("Enter an RLE string to be decoded: ")
            image_data = decode_rle(string_to_rle(input_data))

        elif option == 4:
            input_data = input("Enter the hex string holding RLE data: ")
            readableInputData = ""

            while len(input_data) > 0:
                readableInputData += input_data[0:2] + ":"
                input_data = input_data[2:]

            image_data = decode_rle(string_to_rle(readableInputData[:-1]))

        elif option == 5:
            input_data = input("Enter the hex string holding flat data: ")
            # 94111111111111111111111111111111111111

        elif option == 6:
                print("Displaying image...")
                console_gfx.display_image(image_data)

        elif option == 7:
            print(f"RLE representation: {to_rle_string(encode_rle(image_data))}")


        elif option == 8:
            res = to_hex_string(encode_rle(image_data))
            print(f"RLE hex values: {res}")

        elif option == 9:
            string = ""

            for num in image_data:
                string += str(num)

            print(f"Flat hex values: {string}")

        else:
            print("Error! Invalid input.")
if __name__ == "__main__":
    main()