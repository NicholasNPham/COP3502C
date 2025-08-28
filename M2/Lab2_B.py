totalIncome = float(input("Enter your total income this year: "))

if 0 <= totalIncome <= 11600:
    owedTaxes = totalIncome * .1
    print(f"You owe ${owedTaxes:.2f} this year.")

elif 11601 <= totalIncome <= 47150:
    bracketOne = (11600 * .10)
    bracketTwo = (totalIncome - 11600) * .12
    owedTaxes = bracketOne + bracketTwo
    print(f"You owe ${owedTaxes:.2f} this year.")

elif 47150 <= totalIncome <= 100525:
    bracketOne = 11600 * .10
    bracketTwo = 35550 * .12
    bracketThree = (totalIncome - 47150) * .22
    owedTaxes = bracketOne + bracketTwo + bracketThree
    print(f"You owe ${owedTaxes:.2f} this year.")

elif 100521 <= totalIncome <= 191950:
    bracketOne = 11600 * .10
    bracketTwo = 35550 * .12
    bracketThree = 53375 * .22
    bracketFour = (totalIncome - 100521) * .24
    owedTaxes = bracketOne + bracketTwo + bracketThree + bracketFour
    print(f"You owe ${owedTaxes:.2f} this year.")

elif 191950 <= totalIncome <= 243725:
    bracketOne = 11600 * .10
    bracketTwo = 35550 * .12
    bracketThree = 53375 * .22
    bracketFour = 91425 * .24
    bracketFive = (totalIncome - 191950) * .32
    owedTaxes = bracketOne + bracketTwo + bracketThree + bracketFour + bracketFive
    print(f"You owe ${owedTaxes:.2f} this year.")

elif 243725 <= totalIncome <= 609350:
    bracketOne = 11600 * .10
    bracketTwo = 35550 * .12
    bracketThree = 53375 * .22
    bracketFour = 91425 * .24
    bracketFive = 51775 * .32
    bracketSix = (totalIncome - 243725) * .35
    owedTaxes = bracketOne + bracketTwo + bracketThree + bracketFour + bracketFive + bracketSix
    print(f"You owe ${owedTaxes:.2f} this year.")

else:
    bracketOne = 11600 * .10
    bracketTwo = 35550 * .12
    bracketThree = 53375 * .22
    bracketFour = 91425 * .24
    bracketFive = 51775 * .32
    bracketSix = 365625 *.35
    bracketSeven = (totalIncome - 609350) * .37
    owedTaxes = bracketOne + bracketTwo + bracketThree + bracketFour +bracketFive + bracketSix + bracketSeven
    print(f"You owe ${owedTaxes:.2f} this year.")