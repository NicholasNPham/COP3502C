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
from math import remainder

# Question 2
"""
print("Welcome to the Currency Converter! The available currencies for conversion are USD, CAD, and YEN")

value = float(input("What is the current monetary value? "))
currentCurrency = input("What is the current currency? ")
desiredCurrency = input("What is the desired currency? ")

CAD_rate = 1.24
YEN_rate = 108.59

if currentCurrency == "CAD":
    USDValue = value / CAD_rate
elif currentCurrency == "YEN":
    USDValue = value / YEN_rate
else:
    USDValue = value

def currencyConversion(value):

    if desiredCurrency == "CAD":
        desired = USDValue * CAD_rate
    elif desiredCurrency == "YEN":
        desired = USDValue * YEN_rate
    else:
        desired = USDValue

    return desired

desiredValue = currencyConversion(USDValue)

print(f"You have: {desiredValue:.2f} {desiredCurrency}")
"""
# Practice Question 3:
"""
def numberDivisability():

    first = int(input("First number:"))
    second = int(input("Second number:"))

    remainder = first % second or second % first
    if remainder == 0:
        print("one is divisible by the other")
    else:
        print("They are not divisible")

numberDivisability()
"""
# Practice Question 4:
"""
def growth(first, second, third):
    pv = first
    r = second
    n = third

    futureValue = pv * (1 + r) ** n
    print(f"Estimated Future Value: {futureValue:.2f}")

pv = float(input("Initial savings amount: $ "))
r = int(input("Annual interest rate: ")) / 100
n = int(input("Number of years for saving: "))

growth(pv, r, n)
"""
# Practice Question 5:
"""
def bodyMassIndex(weight, height):
    bmi = weight / (height ** 2)
    return bmi

weightInKilo = float(input("Weight in Kilograms: "))
heightInMeters = float(input("Height in meters: "))

index = bodyMassIndex(weightInKilo, heightInMeters)

if index < 18.5:
    print(f"Your BMI is {index:.2f}.\nYou are underweight.")
elif 18.5 <= index < 24.9:
    print(f"Your BMI is {index:.2f}.\nYou are normal weight")
elif 24.9 <= index < 29.9:
    print(f"Your BMI is {index:.2f}.\nYou are overweight")
else:
    print(f"Your BMI is {index:.2f}.\nYou are obese")
"""
# Practice Question 6:
"""
def role(dice1, dice2):
    if dice1 < dice2:
        low = dice1
        high = dice2
    else:
        low = dice2
        high = dice1

    for i in range(1,low+1):
        for j in range(1,high+1):
            if i > j:
                print("", end="")
            else:
                print(f"({i},{j})", end=" ")
        print()

role(2,3)
"""