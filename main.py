
NUM_ROWS = 6
NUM_COLS = 5

board = ["0"]*NUM_COLS+[""]*(NUM_COLS*(NUM_ROWS-2))+["1"]*NUM_COLS


def print_board(b):
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            idx = row*NUM_COLS + col
            print(f"[{board[idx]}]", end="")
            if col != NUM_COLS-1:
                print(",", end="")
        print()


print_board(board)
