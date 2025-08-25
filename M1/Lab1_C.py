# Calculate how many days are in between two dates

yearOne = int(input("Enter the year for date 1: "))
monthOne = int(input("Enter the month for date 1: "))
dayOne = int(input("Enter the day for date 1: "))
yearTwo = int(input("Enter the year for date 2: "))
monthTwo = int(input("Enter the month for date 2: "))
dayTwo = int(input("Enter the day for date 2: "))

daysInFirstDate = (yearOne * 12) * 30 + monthOne * 30 + dayOne
daysInSecondDate = (yearTwo * 12) * 30 + monthTwo * 30 + dayTwo

if daysInFirstDate > daysInSecondDate:
    totalDays = daysInFirstDate - daysInSecondDate
else:
    totalDays = daysInSecondDate - daysInFirstDate

output = f"The difference between {monthOne}/{dayOne}/{yearOne} and {monthTwo}/{dayTwo}/{yearTwo} is {totalDays} days!"
print(output)

