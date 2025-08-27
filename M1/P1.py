import p1_random as p1
rng = p1.P1Random()

gameNumber = 0
playerWin = 0
dealerWin = 0
gameTied = 0
gameProgress = True

while gameProgress:
    # New Game Loop
    gameNumber += 1
    print(f'Start Game #{gameNumber}')
    card = rng.next_int(13) + 1 #[0-12]
    # Resetting Hand Count
    hand = card

    if card == 1:
        hand = 1
        card = "ACE"
    elif 2 <= card <= 10:
        hand = card
    elif card == 11:
        hand = 10
        card = "JACK"
        hand = 10
    elif card == 12:
        card = "QUEEN"
    else:
        hand = 10
        card = "KING"
    print(f'\nYour card is {card}!')
    print(f'Your hand is: {hand}')
    while True:
        choice = int(input("\n1. Get Another Card \n2. Hold Hand \n3. Print statistics \n4. Exit \n\nChoose your choice: "))
        if choice == 1:
            card = rng.next_int(13) + 1
            if card == 1:
                hand += card
                print('Your card is ACE!')
                print(f'Your hand is {hand}')
            elif 2 <= card <= 10:
                hand += card
                print(f'Your card is {card}!')
                print(f'Your hand is {hand}')
            elif card == 11:
                hand += 10
                print(f'Your card is JACK!')
                print(f'Your hand is {hand}')
            elif card == 12:
                hand += 10
                print(f'Your card is QUEEN!')
                print(f'Your hand is {hand}')
            elif card == 13:
                hand += 10
                print(f'Your card is KING!')
                print(f'Your hand is {hand}')

            if hand == 21:
                playerWin += 1
                print("\nBLACKJACK! You win!\n")
                break
            elif hand > 21:
                dealerWin += 1
                print("\nYou exceeded 21! You lose.\n")
                break

        elif choice == 2:
            # Dealer's Draw
            dealerHand = rng.next_int(11) + 16
            print(f"\nDealer's hand: {dealerHand}")
            print(f"Your hand is {hand}")
            if dealerHand == 21:
                dealerWin += 1
                print("\nDealer Wins!\n")
                break
            elif dealerHand > 21:
                playerWin += 1
                print("\nYou Win!\n")
                break
            elif hand == dealerHand:
                print("\nIt's a tie! No one wins!\n")
                gameProgress += 1
                break
            elif hand > dealerHand:
                playerWin += 1
                print("\nYou Win!\n")
                break
            elif dealerHand < hand:
                dealerWin += 1
                print("\nDealer Wins!\n")
                break

        elif choice == 3:
            print(f'Number of Player wins: {playerWin}')
            print(f'Number of Dealer wins: {dealerWin}')
            print(f'Number of tie games: {gameTied}')
            print(f'total # of games is: {gameNumber - 1}')
            print(f'Percentage of Player wins: {playerWin/(gameNumber - 1):.2f}%')

        elif choice == 4:
            gameProgress = False
            break
        else:
            print("Invalid input!\n\nPlease enter an integer value between 1 and 4.")
