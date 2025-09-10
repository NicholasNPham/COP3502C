num = int(input("enter number: "))

reversedNum = 0

while num > 0:
    digit = num % 10
    reversedNum = reversedNum * 10 + digit
    num //= 10

print(reversedNum)
