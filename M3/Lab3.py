# Do Not Commit EVER.
import math

calculator = True
choice = True

current_result = 0.0
sum_of_calculations = 0.0
number_of_calculations = 0

# menu = (f"Current Result: {current_result}\n"
#           "\nCalculator Menu\n"
#           "---------------\n"
#           "0. Exit Program\n"
#           "1. Addition\n"
#           "2. Subtraction\n"
#           "3. Multiplication\n"
#           "4. Division\n"
#           "5. Exponentiation\n"
#           "6. Logarithm\n"
#           "7. Display Average\n")

while calculator:
    # This prints Menu First Time after program Starts
    print(f"Current Result: {current_result}\n")
    menu = ("\nCalculator Menu\n"
            "---------------\n"
            "0. Exit Program\n"
            "1. Addition\n"
            "2. Subtraction\n"
            "3. Multiplication\n"
            "4. Division\n"
            "5. Exponentiation\n"
            "6. Logarithm\n"
            "7. Display Average\n")
    print(menu)

    # Second While Loop
    while choice:
        # First Choice
        choice = input("Enter Menu Selection: ")
        if choice == "0":
            print("Thanks for using this calculator. Goodbye!")
            calculator = False
            break
        elif choice == "7":
            if number_of_calculations == 0:
                print("Error: No calculations yet to average!\n")
                continue
            else:
                print(f'Sum of calculations: {sum_of_calculations}')
                print(f'Number of calculations: {number_of_calculations}')
                print(f"Average of calculations: {(sum_of_calculations / number_of_calculations):.2f}")
                continue

        elif choice in ["1", "2", "3", "4", "5", "6"]:
            a = input("Enter first operand: ")
            if a == "RESULT":
                a = current_result
            else:
                a = float(a)
            b = input("Enter second operand: ")
            if b == "RESULT":
                b = current_result
            else:
                b = float(b)

                if choice == "1":
                    current_result = a + b
                if choice == "2":
                    current_result = a - b
                if choice == "3":
                    current_result = a * b
                if choice == "4":
                    current_result = a / b
                if choice == "5":
                    current_result = a ** b
                if choice == "6":
                    current_result = math.log(b, a)

                sum_of_calculations += current_result
                number_of_calculations += 1
                print(f"Current Result: {current_result}\n")
                print(menu)

        else:
            print("Error: Invalid selection!")


