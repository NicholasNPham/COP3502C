import math

scientificCalculator = True

resultTotal = 0.0
numberOfCalc = 0
resultCurrent = 0.0

while scientificCalculator:

    print(f"Current Result: {resultCurrent}\n")
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

    choice = input('\nEnter Menu Selection: ')

    if choice == "0":
        print("Thanks for using this calculator. Goodbye!")
        break

    if choice == "1":
        numberOfCalc += 1
        a = float(input('Enter first operand: '))
        b = float(input('Enter second operand: '))

        if a == "RESULT":
            result = resultCurrent + b
        elif b == "RESULT":
            result = a + resultCurrent
        else:
            result = resultCurrent + resultCurrent

        result = a + b
        resultTotal += result
        resultCurrent = result

    elif choice == "2":
        numberOfCalc += 1
        a = float(input('Enter first operand: '))
        b = float(input('Enter second operand: '))
        result = a - b
        resultTotal += result
        resultCurrent = result

    elif choice == "3":
        numberOfCalc += 1
        a = float(input('Enter first operand: '))
        b = float(input('Enter second operand: '))
        result = a * b
        resultTotal += result
        resultCurrent = result

    elif choice == "4":
        numberOfCalc += 1
        a = float(input('Enter first operand: '))
        b = float(input('Enter second operand: '))
        result = a / b
        resultTotal += result
        resultCurrent = result

    elif choice == "5": #result Total = -2 resultcurrent = -2
        numberOfCalc += 1
        a = float(input('Enter first operand: '))
        b = float(input('Enter second operand: '))
        result = a ** b
        resultTotal += result
        resultCurrent = result

    elif choice == "6":
        pass
        numberOfCalc += 1
        a = float(input('Enter first operand: '))
        b = float(input('Enter second operand: '))
        result = math.log(b, a)
        resultTotal += result
        resultCurrent = result

    elif choice == "7":
        if numberOfCalc != 0:
            print(f"Sum of calculations: {resultTotal}")
            print(f"Number of calculations: {numberOfCalc}")
            print(f"Average of calculations: {(resultTotal / numberOfCalc):.2f}")
        else:
            print(f"Error: No calculations yet to average!")

    else:
        print("Error: Invalid Selection.")

