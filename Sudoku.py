def find_next_empty(puzzle):  # Afunction to find the next empty cell which needs to be filled
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c          # If the row and column are found then simply return the row and column

    return None,None                # else return None


# This Function Checks for every row and column in the Entire 9*9 grid and
# then checks the inner 3*3 Grid individually

def is_Valid(puzzle,guess,r,c):     

    # row_vals = puzzle[r]
    # if guess in row_vals:
    #     return False

    for i in range(9):
        if puzzle[r][i] == guess:   #Here the row is constant and every column is checked once
            return False
        
        if puzzle[i][c] == guess:   #Here the column is constant and every Row is checked once
            return False

        if puzzle[3 * (r//3) + i % 3][3 * (c//3) + i % 3] == guess:    #Here The inner grid is Checked with the guessing value
            #3 * (r//3) checks for which inner grid and i % 3 checks for which row or column
            return False
        
    return True
    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])


def solve_sudoku(puzzle):

    row,col = find_next_empty(puzzle)

    if row is None:
        return True #True is Returned if the Whole grid is checked and no
                    #Further empty cells are left
    
    for g in range(1,10):
        #Check if Valid
        if is_Valid(puzzle,g,row,col):
            puzzle[row][col] = g

            if solve_sudoku(puzzle): # Here the function Sudoku solver is recursively called
                                     # and checked for each values and if the function is returned true then we return True
                return True
            
            puzzle[row][col] = -1 #Here we BackTrack if the value is not valid so we again put -1 
        
    return False    #here false is returned to the solve_sudoku function if none of the g form 1 to 9 is satisfied,then we return false and it is checked and further backtracked

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)