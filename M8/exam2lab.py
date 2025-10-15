def print_backwards(string):
    if len(string) == 0:
        return
    else:
        print(string[-1], end="")
        print_backwards(string[:-1])

def format_names(l):
    if len(l) == 0:
        return []
    else:
        if "," in l[0]:
            return [l[0]] + format_names(l[1:])
        else:
            name = l[0].split()
            first = name[0]
            last = name[1]
            formatted = last + ', ' + first
            return [formatted] + format_names(l[1:])


def sum_a(l):
    if len(l) == 0:
        return 0
    else:
        if "a" in l[0]:
            return l[0]["a"] + sum_a(l[1:])
        else:
            return sum_a(l[1:])

def process_list(list):
    if len(list) == 0:
        return []

    even = [str(list[0])]

    if len(list) > 1:
        odd = [list[1] * 10]
        rest = process_list(list[2:])

        rest_even = []
        for i in rest:
            if isinstance(i, str):
                rest_even.append(i)

        rest_odd = []
        for i in rest:
            if isinstance(i, int):
                rest_odd.append(i)

        return even + rest_even + odd + rest_odd
    else:
        return even
