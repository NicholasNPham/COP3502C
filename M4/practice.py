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

def currencyToUSD(currencyAmount):
    if currentCurrency == desiredCurrency:
        currencyConversion = currencyAmount
    elif currentCurrency == "CAD":
        currencyAmount /= 1.24 # Turns into USD
        if desiredCurrency == "YEN":
            currencyConversion = currencyAmount * 108.59
        elif desiredCurrency == "CAD":
            currencyConversion = currencyAmount * 1.24
        else:
            currencyConversion = currencyAmount
    elif currentCurrency == "YEN":
        currencyAmount /= 108.59 # Turns into USD
        if desiredCurrency == "YEN":
            currencyConversion = currencyAmount * 108.59
        elif desiredCurrency == "CAD":
            currencyConversion = currencyAmount * 1.24
        else:
            currencyConversion = currencyAmount
    else:
        if desiredCurrency == "YEN":
            currencyConversion = currencyAmount * 108.59
        elif desiredCurrency == "CAD":
            currencyConversion = currencyAmount * 1.24
        else:
            currencyConversion = currencyAmount

    return currencyConversion

currencyConversion = currencyToUSD(value)

print(f"You have: {currencyConversion:.2f} {desiredCurrency}")

