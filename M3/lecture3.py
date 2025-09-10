# This is from learning a new skill

num = int(input("Enter the number: "))
original_num = num
reversed_num = 0

while num > 0:
    last_num_of_num = num % 10
    reversed_num = reversed_num * 10 + last_num_of_num
    num //= 10

if reversed_num == original_num:
    print(f"{original_num} is a palindrome.")
else:
    print(f"{original_num} is not a palindromic number.")

