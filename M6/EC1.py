
def cost(adultPrice, kidPrice):
    adultTickets = int(input("Adult tickets:  "))
    kidTickets = int(input("Kid tickets:  "))

    if adultTickets + kidTickets <= 30:
        cost = adultPrice * adultTickets + kidPrice * kidTickets
        return f"Total cost: ${cost:.2f}  "
    else:
        return "Invalid option; please restart app..."



def main():
    print("Available movies today:")
    print("A)12 Strong:	1)2:30	2)4:40	3)7:50	4)10:50")
    print("B)Coco:	        1)12:40	2)3:45")
    print("C)The Post:	1)12:45	2)3:35	3)7:05	4)9:55")

    movieChoice = input("Movie choice:  ")

    adultPriceBefore2 = 11.17
    adultPriceAfter2 = 12.45
    kidPriceBefore2 = 8.00
    kidPriceAfter2 = 9.68

    if movieChoice == "A":
        showTime = int(input("Showtime:  "))
        if showTime in [1, 2, 3, 4]:
            print(cost(adultPriceAfter2, kidPriceAfter2))
        else:
            print("Invalid option; please restart app...")
    elif movieChoice == "B":
        showTime = int(input("Showtime:  "))
        if showTime == 1:
            print(cost(adultPriceBefore2, kidPriceBefore2))
        elif showTime == 2:
            print(cost(adultPriceAfter2, kidPriceAfter2))
        else:
            print("Invalid option; please restart app...")
    elif movieChoice == "C":
        showTime = int(input("Showtime:  "))
        if showTime == 1:
            print(cost(adultPriceBefore2, kidPriceBefore2))
        elif showTime in [2, 3, 4]:
            print(cost(adultPriceAfter2, kidPriceAfter2))
        else:
            print("Invalid option; please restart app...")
    else:
        print("Invalid option; please restart app...")


if __name__ == '__main__':
    main()
