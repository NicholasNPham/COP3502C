unitFrom = input('Enter the unit you are converting from: ')
unitTo = input('Enter the unit you are converting to: ')
degree = float(input(f'Enter the temperature in {unitFrom}: '))

if unitFrom == 'Fahrenheit' and unitTo == 'Kelvin':
    conversion = (degree - 32) * (5/9) + 273.15
    print(f'That is {conversion:.1f} degrees {unitTo}.')

elif unitFrom == 'Fahrenheit' and unitTo == 'Celsius':
    conversion = (degree - 32) * (5/9)
    print(f'That is {conversion:.1f} degrees {unitTo}.')

elif unitFrom == 'Kelvin' and unitTo == 'Fahrenheit':
    conversion = (degree - 273.15) * (9/5) + 32
    print(f'That is {conversion:.1f} degrees {unitTo}.')

elif unitFrom == 'Kelvin' and unitTo == 'Celsius':
    conversion = degree - 273.15
    print(f'That is {conversion:.1f} degrees {unitTo}.')

elif unitFrom == 'Celsius' and unitTo == 'Fahrenheit':
    conversion = (degree * (9/5)) + 32
    print(f'That is {conversion:.1f} degrees {unitTo}.')

elif unitFrom == 'Celsius' and unitTo == 'Kelvin':
    conversion = degree + 273.15
    print(f'That is {conversion:.1f} degrees {unitTo}.')
else:
    conversion = degree
    print(f'That is {conversion:.1f} degrees {unitTo}.')