import numpy as np
import sys




class SodukuBoard:
    BOARD_SIZE = 9
    VALID = np.arrange(1,10)

    board_np = np.zeros([BOARD_SIZE, BOARD_SIZE])

    board = [[0] * BOARD_SIZE ] * BOARD_SIZE

    ref_board = []



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


    def check_rows(board_np):
        for i in xrange(BOARD_SIZE):
            if len(np.unique(board_np[i,:])) < BOARD_SIZE:
                return False
        return True

    def check_columns(board_np):
        for i in xrange(BOARD_SIZE):
            if len(np.unique(board_np[:,i])) < BOARD_SIZE:
                return False
        return True

    def check_sub_boards(board_np)
        #need to run through each subboard, there are nine ... and


    def validate_solution(board_np):
        if check_rows(board_np):
            if check_columns(board_np):
                if check_sub_boards(board_np):
                    return True



def main():
    my_board = SodukuBoard()
    my_board.read_boards_from_txt()
    print(my_board.ref_board)
    print(len(my_board.ref_board[0]))
    print(my_board.ref_board_np.shape)





if __name__ == '__main__':
    #call function that we need


    sys.exit(main())