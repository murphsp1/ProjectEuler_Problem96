import numpy as np
import sys


BOARD_SIZE = 9
VALID = np.arange(1,10)

class SodukuBoard:

    def __init__(self):
        self.board_np = np.zeros([BOARD_SIZE, BOARD_SIZE])
        self.board = [[0] * BOARD_SIZE ] * BOARD_SIZE
        self.ref_board = []
        self.ref_board = self.read_boards_from_txt()


    def __str__(self):
        return self.board_np

    def __repl__(self):
        return self.board_np

    def check_rows(self):
        for i in xrange(BOARD_SIZE):
            if len(np.unique(self.board_np[i,:])) < BOARD_SIZE:
                return False
        return True


    def read_boards_from_txt(self):

        #The idiomatic way to handle file reading
        with open('sudoku.txt', 'r') as file_handle:
            ref_board = []
            for line in file_handle:
                if line[0]=='G':
                    #New board
                    board_number = int(line.split(' ')[1]) - 1
                    ref_board.append(board_number)
                    ref_board[board_number] = []
                    print board_number
                else:
                    print(line)
                    new_board_row = [int(c) for c in line if c in '1234567890']
                    ref_board[board_number].append(new_board_row)

            self.ref_board = ref_board
            self.ref_board_np = np.array(ref_board)
        return True



    def check_columns(self):
        for i in xrange(BOARD_SIZE):
            if len(np.unique(self.board_np[:,i])) < BOARD_SIZE:
                return False
        return True

    def check_sub_boards(self):

        for r in range(3): #rows
            for c in range(3): #columns
                col = c*3
                row = r*3
                sub_board = self.board_np[row:row+3, col:col+3]
                print(sub_board)
                if len(np.unique(sub_board)) < BOARD_SIZE:
                    return False
        return True


    def validate_solution(self):
        if self.check_rows(self.board_np):
            if self.check_columns(board_np):
                if self.check_sub_boards(board_np):
                    return True
        return False



def main():
    my_board = SodukuBoard()
    my_board.read_boards_from_txt()
    print(my_board.ref_board)
    print(len(my_board.ref_board[0]))
    print(my_board.ref_board_np.shape)





if __name__ == '__main__':
    #call function that we need


    sys.exit(main())