board = [['a', 0, 0, 0, 0, 0, 0, 'd', 0],
         ['d', 0, 0, 0, 0, 0, 0, 'd', 0],
         [0, 0, 0, 'c', 0, 0, 0, 'e', 0],
         [0, 'a', 0, 0, 0, 0, 'f', 0, 0],
         [0, 0, 0, 'g', 0, 0, 0, 0, 0],
         [0, 'e', 0, 0, 'h', 0, 0, 0, 'a'],
         [0, 'c', 0, 0, 0, 'b', 0, 0, 0],
         [0, 'g', 'a', 0, 0, 0, 0, 'b', 0],
         ['e', 'f', 0, 0, 'a', 0, 0, 0, 0]
         ]
board2 = [['a', 0, 0, 0, 0, 'g', 0, 0, 'i'],
         [0, 0, 'h', 0, 0, 'i', 'f', 0, 0],
         ['f', 0, 0, 'c', 0, 'a', 0, 'e', 0],
         ['c', 0, 0, 0, 'b', 'd', 0, 0, 0],
         ['d', 'a', 0, 0, 'c', 0, 'i', 0, 'h'],
         [0, 0, 'f', 0, 0, 0, 0, 0, 0],
         [0, 0, 'd', 0, 'f', 0, 'a', 'i', 'b'],
         [0, 0, 0, 'h', 'i', 0, 'd', 0, 0],
         [0, 0, 0, 'd', 0, 'c', 0, 'g', 0]
         ]

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
        for i in 'abcdefghi':
            if valid(board, i, (row, col)):
                board[row][col] = i

                if (solve(board)):
                    return True
                board[row][col] = 0
    return False


def valid(board, n, pos):
    # check line
    for i in range(len(board[0])):
        if board[pos[0]][i] == n and pos[1] != i:
            return False
    # check column
    for i in range(len(board[0])):
        if board[i][pos[1]] == n and pos[0] != i:
            return False
    # check 3x3 square
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_x * 3, box_x * 3 + 3):
        for j in range(box_y * 3, box_y * 3 + 3):
            if board[i][j] == n and (i, j) != pos:
                return False
    return True


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if (j == 8):
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row,col
    return None


print_board(board2)
solve(board2)
print("                                ")
print_board(board2)
