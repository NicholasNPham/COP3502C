def bin(number):
    num = number
    binary = []
    res = ""

    if number == 0:
        return "0"
    else:
        while num > 0:
            binary.append(num % 2)
            num //= 2

        for b in range(len(binary) -1, -1, -1):
            res += str(binary[b])

        return res

print(bin(10))      # Should output: 1010
print(bin(42))      # Should output: 101010
print(bin(0))       # Should output: 0
print(bin(255))     # Should output: 11111111
print(bin(12))      # Should output: 1100




