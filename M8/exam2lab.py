def print_backwards(string):
    if len(string) == 1:
        return string
    else:
        return string[-1] + print_backwards(string[:-1])

print(print_backwards("Hello, world!"))