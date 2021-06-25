n = 9
def solveSudoku(board):
    row = 0
    col = 0
    isEmpty = True
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                row = i
                col = j
                isEmpty = False
                break
        if not isEmpty:
            break
    if isEmpty:
        return True
    for num in range(1,n+1):
        if isSafe(board,row,col,num):
            board[row][col] = num
            if solveSudoku(board):
                return True
            else:
                board[row][col] = 0
    return False


def isSafe(board,row,col,num):
    for i in range(len(board)):
        if board[row][i] == num:
            return False

    for j in range(len(board)):
        if board[j][col] == num:
            return False
    for k in range(3):
        for m in range(3):
            if board[k+(row - row % 3)][m+(col-col%3)] == num:
                return False
    return True


def printBoard(board):
    for i in range(n):
        for j in range(n):
            print(board[i][j],end="  ")
        print()


board = [[0 for x in range(9)] for y in range(9)]
board = [[9,0,1,5,6,8,0,0,0],
            [0,0,8,3,0,2,9,0,5],
            [2,0,5,1,0,0,0,0,3],
            [4,0,0,0,0,5,1,0,2],
            [0,0,0,7,3,4,0,0,0],
            [5,8,0,0,0,0,7,6,0],
            [0,0,0,4,0,3,2,5,0],
            [7,0,2,0,5,1,3,4,9],
            [0,0,0,9,2,0,0,0,0]]

if solveSudoku(board):
    printBoard(board)
else:
    print("No Solution Exists")
