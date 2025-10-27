lower = int(input("Lower Limit: "))
upper = int(input("Upper Limit: "))
for a in range(lower, upper + 1):
    for b in range(a, upper + 1):
        for c in range(b, upper + 1):
            if a ** 2 + b ** 2 == c ** 2:
                print(a, b, c)
