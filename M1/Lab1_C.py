# Calculate how many days are in between two dates

yearOne = 1999 # int(input("Enter the year for date 1: "))
monthOne = 12 # int(input("Enter the month for date 1: "))
dayOne = 30 # int(input("Enter the day for date 1: "))
yearTwo = 2000 # int(input("Enter the year for date 2: "))
monthTwo = 1 # int(input("Enter the month for date 2: "))
dayTwo = 1  # int(input("Enter the day for date 2: "))

if yearOne > yearTwo:
    yearInt = yearOne - yearTwo
else:
    yearInt = yearTwo - yearOne

if monthOne > monthTwo:
    monthInt = monthOne - monthTwo
else:
    monthInt = monthTwo - monthOne

if dayOne > dayTwo:
    dayInt = dayOne - dayTwo
else:
    dayInt = dayTwo - dayOne

print(yearInt, monthInt, dayInt)

daysInYear = (yearInt * 12) * 30
daysInMonth = monthInt * 30

totalDays = daysInYear + daysInMonth + dayInt

output = f"The difference between {monthOne}/{dayOne}/{yearOne} and {monthTwo}/{dayTwo}/{yearTwo} is {totalDays} days!"
print(output)

