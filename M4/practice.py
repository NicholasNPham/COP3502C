# Question 1
"""
choice = input("What format do you want to convert to? ")

def celsiusToFahrenheit(value):
    newDegree = (9/5) * value + 32
    return newDegree

def fahrenheitToCelsius(value):
    newDegree = (5/9) * (value - 32)
    return newDegree

if choice == "celsius":
    temperature = float(input("What is your temperature (F)?: "))
    degree = fahrenheitToCelsius(temperature)
    print(f'{temperature} fahrenheit is {degree:.1f} in celsius.')
elif choice == "fahrenheit":
    temperature = float(input("What is your temperature (C)?: "))
    degree = celsiusToFahrenheit(temperature)
    print(f'{temperature} celsius is {degree:.1f} in fahrenheit.')
else:
    print("Please enter a valid choice.")
"""
# Question 2
print("Welcome to the Currency Converter! The available currencies for conversion are USD, CAD, and YEN")

value = float(input("What is the current monetary value? "))
currentCurrency = input("What is the current currency? ")
desiredCurrency = input("What is the desired currency? ")



