import math

scientificCalculator = True
resultTotal = 0.0
numberOfCalc = 0
resultCurrent = 0.0

while scientificCalculator:

    menu = (f"Current Result: {resultCurrent}\n"
            "\nCalculator Menu\n"
            "---------------\n"
            "0. Exit Program\n"
            "1. Addition\n"
            "2. Subtraction\n"
            "3. Multiplication\n"
            "4. Division\n"
            "5. Exponentiation\n"
            "6. Logarithm\n"
            "7. Display Average")
    print(menu)
    choice = input('\nEnter Menu Selection: ')

    if choice not in ('0', '1', '2', '3', '4', '5', '6', '7'):
        print("Error: Invalid selection!")
        choice = input('\nEnter Menu Selection: ')

    if choice == "7":
        if numberOfCalc != 0:
            print(f"Sum of calculations: {resultTotal}")
            print(f"Number of calculations: {numberOfCalc}")
            print(f"Average of calculations: {(resultTotal / numberOfCalc):.2f}")

        else:
            print(f"Error: No calculations yet to average!")

        choice = input('\nEnter Menu Selection: ')
        if choice == "0":
            print("Thanks for using this calculator. Goodbye!")
            scientificCalculator = False
        continue

    elif  choice == "0":
        print("Thanks for using this calculator. Goodbye!")
        break

    elif choice in ["1", "2", "3", "4", "5", "6"]:
        # Adds step to count of number of calculations
        numberOfCalc += 1
        # This is to get Input
        a = input('Enter first operand: ')
        b = input('Enter second operand: ')
        # Noticed Test Case "RESULT" meaning result equals to last result current

        if a == "RESULT":
            a = resultCurrent
        else:
            a = float(a)

        if b == "RESULT":
            b = resultCurrent
        else:
            b = float(b)

        if choice == "1":
            resultCurrent = a + b
        elif choice == "2":
            resultCurrent = a - b
        elif choice == "3":
            resultCurrent = a * b
        elif choice == "4":
            resultCurrent = a / b
        elif choice == "5":
            resultCurrent = a ** b
        elif choice == "6":
            resultCurrent = math.log(b, a)

        resultTotal += resultCurrent


# resultTotal += result
