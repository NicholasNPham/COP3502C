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
    print(f'Start Game {gameNumber}')
    card = rng.next_int(13) + 1 #[0-12]
    if card <= 10:
        hand = card
    else:
        hand = 10
    print(f'Your card is {card}')
    print(f'Your hand is {hand}')
    while True:
        choice = input("1. Get Another Card \n2. Hold Hand \n3. Print statistics \n4. Exit \nChoose your choice: ")