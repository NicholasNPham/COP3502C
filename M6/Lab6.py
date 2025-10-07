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
    for row in board:
        for space in row:
            print(space, end=" ")
        print()

def insert_chip(board,col,chip_type):
    pass

def check_if_winner(board,col,row,chip_type):
    pass

def main():

    height = int(input("What would you like the height of the board to be? "))
    length = int(input("What would you like the length of the board to be? "))

    print_board(initialize_board(height,length))

if __name__ == '__main__':
    main()


