def fibonacci(n):
    list = [0, 1]

    first = 0
    second = 1

    if n == 1 or n == 0:
        return list[0]
    else:
        for n in range(1, n-1):
            list.append(list[first] + list[second])
            first += 1
            second += 1

        return list[-1]

def is_prime(n):
    list = []
    count = 0

    for i in range(1, n+1):
        if n % i == 0:
            list.append(i)
            count += 1

    if count == 2:
        return True
    else:
        return False

def print_prime_factors(n):
    primeFactorList = []
    originalNum = n
    count = 2

    while n > 1:
        if n % count == 0:
            primeFactorList.append(count)
            n /= count
        else:
            count += 1

    strPrime = f"{originalNum} = "+" * ".join(str(prime) for prime in primeFactorList)

    print(strPrime)

