# Program to calculate and display the factorial number using a for loop

num = int(input("Enter a positive number: "))
factorial_num = num

res = num
while num > 1:
    res *= num - 1
    num -= 1

print(f'The factorial of {factorial_num} is {res}')
