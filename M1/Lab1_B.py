# Sales Tax Calculator

price = float(input("Enter the price of the item: "))
taxPercentage = float(input("Enter the sales tax percentage: ")) / 100
totalPrice = price + (taxPercentage * price)
print(f"Your total is ${totalPrice:.2f}")
