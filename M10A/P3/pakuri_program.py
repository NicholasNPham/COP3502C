from pakuri import *
from pakudex import *

def menu():
    print("Pakudex Main Menu")
    print("-----------------")
    print("1. List Pakuri")
    print("2. Show Pakuri")
    print("3. Add Pakuri")
    print("4. Evolve Pakuri")
    print("5. Sort Pakuri")
    print("6. Exit")

def main():
    print("Welcome to Pakudex: Tracker Extraordinaire!")


    while True:
        max_cap = input("Enter max capacity of the Pakudex: ")

        try:
            max_cap = int(max_cap)
            if max_cap <= 0:
                print("Please enter a valid size.")
                break
            print(f"The Pakudex can hold {max_cap} species of Pakuri.\n")
            storage = Pakudex(max_cap)
            menu()
            choice = input("\nWhat would you like to do? ")

            if choice == "1":
                if len(storage.my_pakudex) == 0:
                    print("No Pakuri in Pakudex yet!")
                else:
                    print("Pakuri in Pakudex: ")
                    for i in range(len(storage.my_pakudex)):
                        print(f"{i}. {storage.my_pakudex[i].get_species()}")

            if choice == "2":



        except ValueError:
            print("Please enter a valid size.")

if __name__ == "__main__":
    main()
