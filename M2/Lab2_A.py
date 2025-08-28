lengthOne = float(input("Side length 1: "))
lengthTwo = float(input("Side length 2: "))
lengthThree = float(input("Side length 3: "))

if lengthOne == lengthTwo == lengthThree:
    print('This is an equilateral triangle!')
elif lengthOne == lengthTwo or lengthOne == lengthThree or lengthTwo == lengthThree:
    print("This is an isosceles triangle!")
else:
    print('This is a scalene triangle!')

