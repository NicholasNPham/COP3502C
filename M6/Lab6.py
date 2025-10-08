def initialize_board(num_rows, num_cols):

    board = []

    for rows in range(num_rows):
        r = []
        for cols in range(num_cols):
            r.append("-")
        board.append(r)

    return board

def print_board(board):

    board = board
    for row in board[::-1]:
        for space in row:
            print(space, end=" ")
        print()

def insert_chip(board,col,chip_type):
    col = col
    chip_type = chip_type
    board = board

    for row in range(len(board)):
        if board[row][col] == "-":
            board[row][col] = chip_type
            return row
    return None

def check_if_winner(board,col,row,chip_type):

    # Vertical Check
    count = 1

    # up
    r = row - 1
    while r >= 0 and board[r][col] == chip_type:
        count += 1
        r -= 1
    # down
    r = row + 1
    while r < len(board) and board[r][col] == chip_type:
        count += 1
        r += 1

    if count >= 4:
        return True

    # Horizontal check
    count = 1

    # look left
    c = col - 1
    while c >= 0 and board[row][c] == chip_type:
        count += 1
        c -= 1

    # look right
    c = col + 1
    while c < len(board[0]) and board[row][c] == chip_type:
        count += 1
        c += 1

    if count >= 4:
        return True

    return False

def check_draw(board):
    for row in board:
        for space in row:
            if space == "-":
                return False
    return True

def main():

    height = int(input("What would you like the height of the board to be? "))
    length = int(input("What would you like the length of the board to be? "))

    print_board(initialize_board(height,length))
    board = initialize_board(height,length)

    print("\nPlayer 1: x")
    print("Player 2: o\n")

    player1 = 0

    while True:

        # Player 1
        if player1 % 2 == 0:
            chip_type = "x"
            col = int(input("Player 1: Which column would you like to choose? "))

            if col < 0 or col >= len(board[0]):
                print("Enter Valid Column")
                continue
            else:
                row = insert_chip(board,col,chip_type[0])
                if row is None:
                    print("Column is full, Choose Another")
                    continue
                else:
                    player1 += 1
                    print_board(board)

                if check_if_winner(board,col,row,"x"):
                    print("Player 1 won the game!")
                    break

                if check_draw(board):
                    print("Draw. Nobody wins.")
                    break


        # Player 2
        else:
            chip_type = "o"
            col = int(input("Player 2: Which column would you like to choose? "))

            if col < 0 or col >= len(board[0]):
                print("Enter Valid Column")
                continue
            else:
                row = insert_chip(board, col, "o")
                if row is None:
                    print("Column is full, Choose Another")
                    continue
                else:
                    player1 += 1
                    print_board(board)

                if check_if_winner(board, col, row, chip_type[0]):
                    print("Player 2 won the game!")
                    break

                if check_draw(board):
                    print("Draw. Nobody wins.")
                    break

        # print(board) # This is the print the list

if __name__ == '__main__':
    main()