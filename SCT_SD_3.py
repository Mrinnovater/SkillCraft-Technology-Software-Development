def print_board(board):
    for row in board:
        print(" ".join(str(num) if num!=0 else '.' for num in row))

def is_valid(board,row,col,num):
    # Check if 'num' is not in the current row, column and 3x3 subgrid
    for x in range(9):
        if board[row][x]==num or board[x][col]==num:
            return False
    start_row,start_col=3*(row//3),3*(col//3)
    for i in range(3):
        for j in range(3):
            if board[start_row+i][start_col+j]==num:
                return False
    return True

def solve_sudoku(board):
    empty_cell=find_empty(board)
    if not empty_cell:
        return True
    row,col=empty_cell
    for num in range(1,10):
        if is_valid(board,row,col,num):
            board[row][col]=num
            if solve_sudoku(board):
                return True
            board[row][col]=0
    return False

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                return(i,j)
    return None

# Example Sudoku puzzle (0 represents empty cells)
sudoku_board=[
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

if solve_sudoku(sudoku_board):
    print("Sudoku puzzle solved:")
    print_board(sudoku_board)
else:
    print("No solution exists.")