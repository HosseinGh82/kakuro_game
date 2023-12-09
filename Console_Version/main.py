height = 7
width = 7

board = [[-2, -2, -2, -2, -2, -2, -2],
         [-2, -1, [3, 7], 0, 0, 0, -2],
         [-2, [-1, 5], 0, 0, [6, 1], 0, -2],
         [-2, -1, 0, -1, 0, -1, -2],
         [-2, -1, -1, -1, 0, -1, -2],
         [-2, -1, -1, -1, -1, -1, -2],
         [-2, -2, -2, -2, -2, -2, -2]
         ]


# Function for print cell
def printCell(cell):
    string1 = ""
    string2 = ""
    string3 = ""

    if type(cell) == list:
        string1 += "+ - - "
        if cell[1] == -1:
            string2 += "| \\ # "
        else:
            string2 += f"| \\ {cell[1]} "
        if cell[0] == -1:
            string3 += f"| # \\ "
        else:
            string3 += f"| {cell[0]} \\ "
    else:
        string1 += "+ - - "
        if cell == -1:
            string2 += "| # # "
            string3 += "| # # "
        elif cell == -2:
            string2 += "| @ @ "
            string3 += "| @ @ "
        else:
            string2 += f"|  {cell}  "
            string3 += f"|  {cell}  "

    return string1, string2, string3


# Function for print board
def printBoard(b, w, h):
    for i in range(w):
        string1 = ""
        string2 = ""
        string3 = ""
        for j in range(h):
            st1, st2, st3 = printCell(b[i][j])
            string1 += st1
            string2 += st2
            string3 += st3
        string1 += "+"
        string2 += "|"
        string3 += "|"

        print(string1)
        print(string2)
        print(string3)
    print("+ - - + - - + - - + - - + - - + - - + - - +")


# Function for validation number in row and column
def validNumber(x, y, number) -> bool:
    # problem in row:
    i = y + 1
    while type(board[x][i]) != list and board[x][i] != -1:
        if board[x][i] == number:
            return False
        i += 1

    # problem in column:
    j = x + 1
    while type(board[j][y]) != list and board[j][y] != -1:
        if board[j][y] == number:
            return False
        j += 1

    return True


def solve_Problem():
    return True


def check_guide():
    row = False
    column = False


printBoard(board, width, height)
