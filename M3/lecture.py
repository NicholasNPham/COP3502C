# Program to calculate and display the factorial number using a for loop

num = int(input("Enter a positive number: "))
factorial_num = num

res = 1

for i in range(1, num+1):
    res *= i

print(f'The factorial of {factorial_num} is {res}')
