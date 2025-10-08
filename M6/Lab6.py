def initialize_board(num_rows, num_cols):

    board = []

    for rows in range(num_rows):
        r = []
        for cols in range(num_cols):
            r.append("_")
        board.append(r)

    return board

def print_board(board):

    board = board
    for row in board[::-1]:
        for space in row:
            print(space, end=" ")
        print()

def insert_chip(board,col,chip_type):
    row = 0
    col = col
    chip_type = chip_type
    board = board

    if board[row][col] == "x" or board[row][col] == "o":
        row += 1
        board[row][col] = chip_type
    else:
        board[row][col] = chip_type

def check_if_winner(board,col,row,chip_type):
    pass

def main():

    height = int(input("What would you like the height of the board to be? "))
    length = int(input("What would you like the length of the board to be? "))

    print_board(initialize_board(height,length))
    board = initialize_board(height,length)
    # print(board) # This is the print the list

    print("\nPlayer 1: x")
    print("Player 2: 0\n")

    player1 = 0

    while True:

            if player1 % 2 == 0:
                chip_type = "x"
                col = int(input("Player 1: Which column would you like to choose? "))
                if col <= len(board):
                    insert_chip(board, col, chip_type)
                    player1 += 1
                    print_board(board)
                else:
                    print("Enter Valid Column")
                    continue
            else:
                chip_type = "o"
                col = int(input("Player 2: Which column would you like to choose? "))
                if col <= len(board):
                    insert_chip(board, col, chip_type)
                    player1 += 1
                    print_board(board)
                else:
                    print("Enter Valid Column")
                    continue

if __name__ == '__main__':
    main()


