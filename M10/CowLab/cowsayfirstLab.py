import sys
from heifer_generator import get_cows

def list_cows(cows):
    print("Cows available:", end= " ")
    cow_names = []
    for cow in cows:
        cow_names.append(cow.get_name())
    print(" ".join(cow_names))


def find_cow(name, cows):
    for cow in cows:
        if cow.get_name() == name:
            return cow
    return None

def main():

    cows = get_cows()

    if len(sys.argv) == 2 and sys.argv[1] == "-l":
        list_cows(cows)
        return

    if len(sys.argv) >= 4 and sys.argv[1] == "-n":
        cow_name = sys.argv[2]
        message = " ".join(sys.argv[3:])

        chosen_cow = find_cow(cow_name, cows)

        if chosen_cow is None:
            print(f"Could not find {cow_name} cow!")
            return

        print(message)
        print(chosen_cow.get_image(), end="")
        return

    message = " ".join(sys.argv[1:])
    default_cow = cows[0]
    print(message)
    print(default_cow.get_image(), end="")

if __name__ == "__main__":
    main()