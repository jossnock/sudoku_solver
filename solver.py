# -1 to go back

def fill_board():
    """Enter the board; if you make a mistake, enter -1 to go back.\n
    Each input must be an integer between 1 and 9 inclusive.\n
    Start by listing the digits to the left of the top row, then from left to right.
    Repeat for the rest of the rows, in descending order.\n
    For empty cells, put 0"""
    print("Enter the board; if you make a mistake, enter -1 to go back.\n Each input must be an integer between 1 and 9 inclusive.\n Start by listing the digits to the left of the top row, then from left to right. Repeat for the rest of the rows, in descending order.\n For empty cells, put 0")
    board = [[[] for i in range(9)] for i in range(9)]
    i = 0
    while i < 9:
        j = 0
        while j < 9:
            digit = input("Row: {} Column: {}\n".format(i+1, j+1))
            try:
                int(digit)
            except ValueError:
                print("the number must be an integer, try again")
            else: 
                digit = int(digit)
                if digit == -1:
                    j -= 1
                else:
                    if ((digit >= 0) and (digit <=9)):
                        if digit == 0:
                            board[i][j] = (1,2,3,4,5,6,7,8,9)
                        else:
                            board[i][j] = digit
                        j += 1
                    else:
                        print("the number must be between 1 and 9 inclusive, try again")
        i += 1
    return board

def sudoku_print(board):
    for i in range(9):
        print(board[i])

#sudoku_print(fill_board())
#sudoku_print([[1]*9]*9)



"""
Steps:
 - Assign each cell a list of possible values.
 - Iterate through each cell, checking its row, column, and box
     - Check last free cell in column/row/box
     - Check for naked/hidden singles, naked/hidden doubles, triples, etc.
     - Pointing pairs/triples/etc. (i.e. all 3 notes in a box are alligned on 1 row, so other 3s can be eliminated from the row)
     - execute the techniques
     - Check for x-wing (sudoku.com/sudoku-rules/h-wing/)
     - Check for y-wing (sudoku.com/sudoku-rules/y-wing/)
     - Check for swordfish (sudoku.com/sudoku-rules/swordfish/)

Variable Names:
 - notes <tuple>
 - cell_solved <bool>
 - 
 
 Extras:
 - Add killer sudoku support
"""
