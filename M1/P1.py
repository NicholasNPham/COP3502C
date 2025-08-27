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
    print(f'START GAME #{gameNumber}')
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
    print(f'\nYour card is a {card}!')
    print(f'Your hand is: {hand}')
    while True:
        choice = int(input("\n1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit\n\nChoose an option: "))
        if choice == 1:
            card = rng.next_int(13) + 1
            if card == 1:
                hand += card
                print('Your card is a ACE!')
                print(f'Your hand is: {hand}')
            elif 2 <= card <= 10:
                hand += card
                print(f'Your card is a {card}!')
                print(f'Your hand is: {hand}')
            elif card == 11:
                hand += 10
                print(f'Your card is a JACK!')
                print(f'Your hand is: {hand}')
            elif card == 12:
                hand += 10
                print(f'Your card is a QUEEN!')
                print(f'Your hand is: {hand}')
            elif card == 13:
                hand += 10
                print(f'Your card is a KING!')
                print(f'Your hand is: {hand}')

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
            print(f"Your hand is: {hand}")
            if dealerHand == 21:
                dealerWin += 1
                print("\nDealer wins!\n")
                break
            elif dealerHand > 21:
                playerWin += 1
                print("\nYou win!\n")
                break
            elif hand == dealerHand:
                print("\nIt's a tie! No one wins!\n")
                gameTied += 1
                break
            elif hand > dealerHand:
                playerWin += 1
                print("\nYou win!\n")
                break
            else:
                dealerWin += 1
                print("\nDealer wins!\n")
                break

        elif choice == 3:
            print(f'Number of Player wins: {playerWin}')
            print(f'Number of Dealer wins: {dealerWin}')
            print(f'Number of tie games: {gameTied}')
            print(f'Total # of games played is: {gameNumber - 1}')
            print(f'Percentage of Player wins: {(playerWin/(gameNumber - 1))* 100:.1f}%')

        elif choice == 4:
            gameProgress = False
            break
        else:
            print("Invalid input!\n\nPlease enter an integer value between 1 and 4.")
