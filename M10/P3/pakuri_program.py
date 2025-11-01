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
                continue
            print(f"The Pakudex can hold {max_cap} species of Pakuri.")
            storage = Pakudex(max_cap)
            break
        except ValueError:
            print("Please enter a valid size.")

    while True:
            print()
            menu()
            choice = input("\nWhat would you like to do? ")

            if choice == "1":
                if storage.get_size() == 0:
                    print("No Pakuri in Pakudex yet!")
                else:
                    names = storage.get_species_array()
                    print("Pakuri In Pakudex: ")
                    for i in range(len(names)):
                        print(f"{i+1}. {names[i]}")

            elif choice == "2":
                species_name = input("Enter the name of the species to display: ")
                stats = storage.get_stats(species_name)
                if stats == None:
                    print("Error: No such Pakuri!")
                else:
                    print(f"Species: {species_name}")
                    print(f"Attack: {stats[0]}")
                    print(f"Defense: {stats[1]}")
                    print(f"Speed: {stats[2]}")

            elif choice == "3":

                if storage.get_size() == storage.get_capacity():
                    print("Error: Pakudex is full!")
                else:
                    species_name = input("Enter the name of the species to add: ")
                    add_checker = storage.add_pakuri(species_name)
                    if add_checker == False:
                        print("Error: Pakudex already contains this species!")
                    else:
                        print(f"Pakuri species {species_name} successfully added!")

            elif choice == "4":
                species_name = input("Enter the name of the species to evolve: ")
                evolve_checker = storage.evolve_species(species_name)
                if evolve_checker == False:
                    print("Error: No such Pakuri!")
                else:
                    print(f"{species_name} has evolved!")

            elif choice == "5":
                storage.sort_pakuri()
                print("Pakuri have been sorted!")

            elif choice == "6":
                print("Thanks for using Pakudex! Bye!")
                break

            else:
                print("Unrecognized menu selection!")

if __name__ == "__main__":
    main()
