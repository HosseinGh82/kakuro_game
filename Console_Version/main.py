import types

# height = 7
# width = 7

# board = [[-2, -2, -2, -2, -2, -2, -2],
#          [-2, -1, [3, 7], 0, 0, 0, -2],
#          [-2, [-1, 5], 0, 0, [6, 1], 0, -2],
#          [-2, -1, 0, -1, 0, -1, -2],
#          [-2, -1, -1, -1, 0, -1, -2],
#          [-2, -1, -1, -1, -1, -1, -2],
#          [-2, -2, -2, -2, -2, -2, -2]
#          ]


height = 5
width = 5
board2 = [[-2, -2, -2, -2, -2],
         [-2, -1, [3, 2], 2, -2],
         [-2, [-1, 4], 1, 3, -2],
         [-2, -1, 2, -1, -2],
         [-2, -2, -2, -2, -2]]


board = [[-2, -2, -2, -2, -2],
         [-2, -1, [3, 2], 0, -2],
         [-2, [-1, 4], 0, 0, -2],
         [-2, -1, 0, -1, -2],
         [-2, -2, -2, -2, -2]]

def isEnd(b, x, y):
    if type(b[x][y]) == list:
        return True
    if b[x][y] < 0:
        return True
    return False


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
                    while (j2 < w) and not (isEnd(b, i, j2)):
                        print(board[i][j2])
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
                    while (j2 < h) and not (isEnd(b, i2, j)):
                        cellList.append([i2, j, board[i2][j]])
                        i2 += 1
                    guide = Guide(cellList, num, len(cellList))
                    guideList.append(guide)

    return guideList


def convertToList(lg):
    listOfAll = []

    for i in lg:
        for j in range(i.countOfCells):
            listOfAll.append(i.emptyCells[j])
        listOfAll.append(i.guideNumber)

    return listOfAll


# def printListOfAll(l):

class Guide:
    # def __init__(self, guideLoc, lastLoc, guideNum):
    def __init__(self, cells, guideNum, cCells):
        # self.guideLocation = guideLoc
        # self.lastLocation = lastLoc
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
    # ii = y + 1
    # while isEnd(board, x, y):
    #     print(x, ii)
    #     if board[x][ii] == number:
    #         return False
    #     ii += 1
    tempGuide = 0
    for i in guideList:
        for j in range(i.countOfCells):
            if i.emptyCells[j][0] == x and i.emptyCells[j][1] == y:
                tempGuide = i
                for k in tempGuide.emptyCells:
                    tempx, tempy = k[0], k[1]
                    if board[tempx][tempy] == number:
                        return False

    return True

    # problem in column:
    # jj = x + 1
    # while isEnd(board, x, y):
    #     if board[jj][y] == number:
    #         return False
    #     jj += 1

    # problem in guide
    # sum = 0
    # for i in guideList:
    #     for j in i.emptyCells:
    #         if j[0] == x and j[1] == y:
    #                 for k in range(i.countOfCells):
    #                     xtemp, ytemp = i.emptyCells[k][0], i.emptyCells[k][1]
    #                     sum += board[xtemp][ytemp]
    #                 if sum == i.guideNumber:
    #                     return True


def allCellsFull(b, w, h):
    for i in range(w):
        for j in range(h):
            if type(b[i][j]) != list:
                if b[i][j] == 0:
                    return False
    return True


def checkTable(glist):
    sum = 0
    for i in glist:
        if type(i) == list:
            xtemp, ytemp = i[0], i[1]
            sum += board[xtemp][ytemp]
        else:
            if sum != i.guideNumber:
                return False
            sum = 0

    return True

result = 0

def solve_Problem(x, y):
    if y == height - 1:
        if x == width - 2:
            return True
        x += 1
        y = 1

    if type(board[x][y]) == list or board[x][y] != 0:
        return solve_Problem(x, y + 1)

    for i in range(1, 10):
        if validNumber(x, y, i):
            board[x][y] = i
            if solve_Problem(x, y + 1) and checkTable(guideList):
                return True
        board[x][y] = 0
    return False


# def solve_Problem(listOfAll, count):
# if len(listOfAll) == count:
#     return True

# print(listOfAll)
# if type(listOfAll[count]) == list:
#     print(listOfAll[count])
#     xtemp, ytemp = listOfAll[count][0], listOfAll[count][1]
#     value = board[xtemp][ytemp]
#
#     if value > 0:
#         solve_Problem(listOfAll, count + 1)
#
#     for i in range(1, 10):
#         if validNumber(xtemp, ytemp, i):
#             # if type(listOfAll[count + 1]) != list:
#             board[xtemp][ytemp] = i
#             if solve_Problem(listOfAll, count + 1) and checkTable(guideList):
#                 return True
#         board[xtemp][ytemp] = 0
# else:
#     solve_Problem(listOfAll, count + 1)
#
# return False

# if g == len(guideList):
#     return True
# guide = guideList[g]
# sum = 0
# for i in range(guide.countOfCells):
#     for j in range(1, 10):
#         xtemp, ytemp = guide.emptyCells[i][0], guide.emptyCells[i][1]
#         if validNumber(xtemp, ytemp, j):
#             sum += j
#             b[xtemp][ytemp] = j
#
# if sum == guide.guideNumber:
#     solve_Problem(b, g + 1)
#
#
# return False

# x, y = guide.guideLocation
# if allCellsFull(b, w, h):
#     return True
#
# if b[x][y] > 0:
#     sovle_Problem()
# for i in range(1, 10):


# def check_guide():
#     row = False
#     column = False

ll = findGuide(board2, width, height)
print(ll)
# alll = convertToList(ll)
# print(checkTable(alll))


# printBoard(board, width, height)
#
# guideList = findGuide(board, width, height)
# for i in guideList:
#     i.printGuideInfo()
#
# allCells = convertToList(findGuide(board, width, height))

# solve_Problem(allCells, 0)
# printBoard(solve_Problem(1, 1), width, height)
# boardsample = solve_Problem(1, 1)
# print(boardsample)
# solve_Problem(1, 1)
# print(result)
# printBoard(board, width, height)
