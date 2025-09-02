import math

scientificCalculator = True
resultTotal = 0.0
numberOfCalc = 0
resultCurrent = 0.0

while scientificCalculator:
    choice = input("Enter Menu Selection: ")

    if choice == "0":
        print("Thanks for using this calculator. Goodbye!")
        break

    elif choice == "7":
        if numberOfCalc != 0:
            print(f"Sum of calculations: {resultTotal}")
            print(f"Number of calculations: {numberOfCalc}")
            print(f"Average of calculations: {resultTotal / numberOfCalc:.2f}")
        else:
            print("Error: No calculations yet to average!")
        continue  # skip menu printing, go straight to next input

    elif choice in ["1","2","3","4","5","6"]:
        # Only print Current Result and Menu for actual calculations
        print(f"\nCurrent Result: {resultCurrent}\n")
        print("Calculator Menu")
        print("---------------")
        print("0. Exit Program")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Logarithm")
        print("7. Display Average")

        numberOfCalc += 1
        a_input = input("Enter first operand: ")
        b_input = input("Enter second operand: ")

        a = resultCurrent if a_input.upper() == "RESULT" else float(a_input)
        b = resultCurrent if b_input.upper() == "RESULT" else float(b_input)

        if choice == "1":
            result = a + b
        elif choice == "2":
            result = a - b
        elif choice == "3":
            result = a * b
        elif choice == "4":
            result = a / b
        elif choice == "5":
            result = a ** b
        elif choice == "6":
            result = math.log(b, a)

        resultTotal += result
        resultCurrent = result

    else:
        # Only print error, no menu or current result
        print("Error: Invalid Selection!")
        continue