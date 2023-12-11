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


# height = 5
# width = 5
# board2 = [[-2, -2, -2, -2, -2],
#           [-2, -1, [3, 2], 2, -2],
#           [-2, [-1, 4], 1, 3, -2],
#           [-2, -1, 2, -1, -2],
#           [-2, -2, -2, -2, -2]]
#
# board = [[-2, -2, -2, -2, -2],
#          [-2, -1, [3, 2], 0, -2],
#          [-2, [-1, 4], 0, 0, -2],
#          [-2, -1, 0, -1, -2],
#          [-2, -2, -2, -2, -2]]


class Guide:
    def __init__(self, cells, guideNum, cCells):
        self.emptyCells = cells
        self.guideNumber = guideNum
        self.countOfCells = cCells

    def printGuideInfo(self):
        print("cells: ", end="")
        for i in self.emptyCells:
            print(f"({i[0]}, {i[1]}, {i[2]})", end=", ")
        print()
        print("count of cells =", self.countOfCells)
        print("Guide number", self.guideNumber)
        print()


def findGuide(b, w, h):
    guideList = []
    # For row guide:
    for i in range(w):
        for j in range(h):
            if type(b[i][j]) == list:
                if b[i][j][1] != -1:
                    num = b[i][j][1]
                    j2 = j + 1
                    cellList = []
                    while (j2 < w) and not (isEnd(i, j2)):
                        cellList.append([i, j2, board[i][j2]])
                        j2 += 1
                    guide = Guide(cellList, num, len(cellList))
                    guideList.append(guide)

    # For column guide:
    for i in range(h):
        for j in range(w):
            if type(b[i][j]) == list:
                if b[i][j][0] != -1:
                    num = b[i][j][0]
                    i2 = i + 1
                    cellList = []
                    while (j2 < h) and not (isEnd(i2, j)):
                        cellList.append([i2, j, board[i2][j]])
                        i2 += 1
                    guide = Guide(cellList, num, len(cellList))
                    guideList.append(guide)

    return guideList


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


def isEnd(x, y):
    if type(board[x][y]) == list:
        return True
    if board[x][y] < 0:
        return True
    return False


def validNumber(x, y, number):
    i = y
    while not isEnd(x, i):
        if board[x][i] == number:
            return False
        i -= 1

    i = y
    while not isEnd(x, i):
        if board[x][i] == number:
            return False
        i += 1

    i = x
    while not isEnd(i, y):
        if board[i][y] == number:
            return False
        i -= 1

    i = x
    while not isEnd(i, y):
        if board[i][y] == number:
            return False
        i += 1

    return True


# def checkGuid(guide):


def checkTable():
    for i in range(width):
        j = 0
        while j < height:
            guidNum = 0
            if type(board[i][j]) == list and board[i][j][1] != -1:
                guidNum = board[i][j][1]
                sum = 0
                j += 1
                while not isEnd(i, j):
                    sum += board[i][j]
                    j += 1
                if sum != guidNum:
                    return False
            j += 1

    for j in range(height):
        i = 0
        while i < width:
            guidNum = 0
            if type(board[i][j]) == list and board[i][j][0] != -1:
                guidNum = board[i][j][0]
                total = 0
                i += 1
                while not isEnd(i, j):
                    total += board[i][j]
                    i += 1
                if total != guidNum:
                    return False
            i += 1

    return True


def solveProblem(x, y):
    if y == height - 1:
        if x == width - 2:
            return True
        x += 1
        y = 1

    if type(board[x][y]) == list or board[x][y] != 0:
        return solveProblem(x, y + 1)

    for i in range(1, 10):
        if validNumber(x, y, i):
            board[x][y] = i
            if solveProblem(x, y + 1) and checkTable():
                return True
        board[x][y] = 0
    return False


printBoard(board, width, height)
print()
guideList = findGuide(board, width, height)

print(guideList)
solveProblem(1, 1)
printBoard(board, width, height)


# def convertToList(lg):
#     listOfAll = []
#
#     for i in lg:
#         for j in range(i.countOfCells):
#             listOfAll.append(i.emptyCells[j])
#         listOfAll.append(i.guideNumber)
#
#     return listOfAll

# def printListOfAll(l):
