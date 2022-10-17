# Sudoku Solver, takes a 9x9 list of lists representing an unsolved Sudoku board
# Returns solved board, or False if no solution exists

def solveSudoku(board): 
    # Prints the board for testing
    def print_grid(board):
        for row in range(9):
            for col in range(9):
                print(board[row][col], end=" ")
            print('\n')


    # Searches for the first 0 in the board and returns its location as a tuple
    # Returns False if there are no empty squares
    def return_empty_location(board):
        for row in range(9):
            for col in range(9):
                if board[row][col]==0:
                    return (row, col)
        return False

    # Checks board to ensure it is a valid Sudoku puzzle (no doubles already present)
    def check_init_board(board):
        for row in range(9):
            for col in range(9):
                # Checks each number 1 by 1
                num = board[row][col]
                # If num == 0, skip to next cell
                if num == 0:
                    continue
                # Checks if the num matches any other in the current row
                for c in range(9):
                    if board[row][c]==num and c!=col:
                        return False
                # Checks if the num matches any other in the current column
                for r in range(9):
                    if board[r][col]==num and r!=row:
                        return False
                # Checking for the current 3x3 box:
                # This finds the top left hand corner of the current 3x3 box
                box_row_start = row - row % 3
                box_col_start = col - col % 3
                # Checks if the num matches any other in the 3x3 box
                for r in range(box_row_start ,box_row_start + 3):
                    for c in range(box_col_start, box_col_start + 3):
                        if board[r][c]==num and (r, c)!=(row, col):
                            return False
        # If we reach this point, the board is valid
        return True

    # Checks if the num we are testing can go in the current pos
    def check_valid(board, num, pos):
        row, col = pos

        # Checks if the num can go in the current row on the board
        for c in range(9):
            if board[row][c]==num and c!=col: # if the number is already in the row (ignore the num we are testing)
                return False

        # Checks if the num can go in the current column on the board
        for r in range(9):
            if board[r][col]==num and r!=row: # if the number is already in the col (ignore the num we are testing)
                return False

        # Checking for the current 3x3 box:
        # This finds the top left hand corner of the current 3x3 box
        box_row_start = row - row % 3
        box_col_start = col - col % 3
        # Checks if the num can go in the current column on the board
        for r in range(box_row_start ,box_row_start + 3):
            for c in range(box_col_start, box_col_start + 3):
                if board[r][c]==num and (r, c)!=pos: # if the number is already in the 3x3 box (ignore the num we are testing)
                    return False
        # If we reach this point, the number is valid (for now)
        return True


    def solve(board):
        # Find the next empty position to try numbers in
        empty_pos = return_empty_location(board)
        
        # If there are no empty positions, then the puzzle is solved!
        if not empty_pos:
            return True
        else:
            row, col = empty_pos

        # For each number 1-9 check if it is a possible fit for the current empty position
        for num in range(1, 10):
            if check_valid(board, num, empty_pos):
                board[row][col] = num
                # (Recursive call to solve()) - Now try solving the board with this num in position
                # If it ends up working out then insert this correct step to the start of steps and return True
                if solve(board):
                    # insert(0, ) is used instead of append() so that steps ends up in the right order
                    steps.insert(0, [row, col, num])
                    return True
                # If not set the position back to 0 and keep trying the next number
                board[row][col] = 0
        
        # If we reach here then no number can go in the spot, so return False (backtracking)
        return False
    
    # List to hold step-by-step solution
    # Elements of steps are of the form [row, col, num]
    steps = []

    # Check initial board
    if not check_init_board(board):
        return None
        
    # If solution exists return the board 9x9 list of lists
    if(solve(board)):
        print(board) # only required for testing
        # print(steps) # only required for testing
        return board, steps, True
    # Else return None to catch invalid Sudoku boards
    else:
        return None



# # Test boards
# grid =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
#        [5, 2, 0, 0, 0, 0, 0, 0, 0],
#        [0, 8, 7, 0, 0, 0, 0, 3, 1],
#        [0, 0, 3, 0, 1, 0, 0, 8, 0],
#        [9, 0, 0, 8, 6, 3, 0, 0, 5],
#        [0, 5, 0, 0, 9, 0, 6, 0, 0],
#        [1, 3, 0, 0, 0, 0, 2, 5, 0],
#        [0, 0, 0, 0, 0, 0, 0, 7, 4],
#        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

# grid =[[0, 0, 6, 3, 0, 2, 0, 8, 0],
#        [8, 0, 0, 0, 0, 0, 9, 0, 0],
#        [0, 0, 0, 0, 0, 7, 0, 2, 0],
#        [0, 7, 0, 9, 0, 0, 2, 4, 0],
#        [5, 4, 0, 0, 0, 0, 0, 7, 6],
#        [0, 1, 3, 0, 0, 0, 0, 0, 0],
#        [0, 3, 0, 7, 0, 0, 0, 0, 0],
#        [0, 0, 7, 0, 0, 0, 0, 0, 2],
#        [0, 8, 0, 5, 0, 7, 7, 0, 0]]

# # if success print the grid
# if(solveSudoku(grid)):
#     print("Success")
# else:
#     print("No solution exists")

# print(solveSudoku(grid))