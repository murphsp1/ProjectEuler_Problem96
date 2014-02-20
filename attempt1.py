import numpy as np
import sys




class SodukuBoard:
    BOARD_SIZE = 9

    board_np = np.zeros([BOARD_SIZE, BOARD_SIZE])
    board = [[0] * BOARD_SIZE ] * BOARD_SIZE


    def read_boards_from_txt(self):

        #The idiomatic way to handle file reading
        with open('sudoku.txt', 'r') as file_handle:
            for line in file_handle:
                print line


def main():
    my_board = SodukuBoard()
    my_board.read_boards_from_txt()


if __name__ == '__main__':
    #call function that we need


    sys.exit(main())