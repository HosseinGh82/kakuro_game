from itertools import combinations

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
# board = [[-2, -2, -2, -2, -2],
#           [-2, -1, [3, 2], 2, -2],
#           [-2, [-1, 4], 1, 3, -2],
#           [-2, -1, 2, -1, -2],
#           [-2, -2, -2, -2, -2]]

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


def checkGuid(guide):
    sum = 0
    for cell in guide.emptyCells:
        sum += cell[2]
    if sum != guide.guideNumber:
        return False
    return True


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


def generateStates(n):
    if n <= 0:
        return [[]]
    smaller_states = generateStates(n - 1)
    states = []
    for state in smaller_states:
        for num in range(1, 10):
            if num not in state:
                new_state = state + [num]
                states.append(new_state)
    return states


def generate_states_with_sum(count, sum_of_numbers):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = [comb for comb in combinations(numbers, count) if sum(comb) == sum_of_numbers]
    return result


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


def solveProblem2(listOfGuide, numberOfGuide):
    if len(listOfGuide) == numberOfGuide:
        # return board
        return True

    for i in generateStates(listOfGuide[numberOfGuide].countOfCells):
        for j in range(listOfGuide[numberOfGuide].countOfCells):
            board[listOfGuide[numberOfGuide].emptyCells[j][0]][listOfGuide[numberOfGuide].emptyCells[j][1]] = i[j]
            listOfGuide[numberOfGuide].emptyCells[j][2] = i[j]
        if checkGuid(listOfGuide[numberOfGuide]):
            solveProblem2(listOfGuide, numberOfGuide + 1)
            return True

    return False


def solveProblem3(listOfGuide, numberOfGuide):
    if len(listOfGuide) == numberOfGuide:
        # return board
        return True

    for i in generate_states_with_sum(listOfGuide[numberOfGuide].countOfCells, listOfGuide[numberOfGuide].guideNumber):
        for j in range(listOfGuide[numberOfGuide].countOfCells):
            board[listOfGuide[numberOfGuide].emptyCells[j][0]][listOfGuide[numberOfGuide].emptyCells[j][1]] = i[j]
            listOfGuide[numberOfGuide].emptyCells[j][2] = i[j]
        if checkGuid(listOfGuide[numberOfGuide]):
            solveProblem2(listOfGuide, numberOfGuide + 1)
            return True

    return False


printBoard(board, width, height)

guideList = findGuide(board, width, height)
solveProblem3(guideList, 0)
printBoard(board, width, height)


# for i in guideList:
#     i.printGuideInfo()

# print(result)
# printBoard(result, width, height)

# printBoard(board, width, height)


# solveProblem(1, 1)
# printBoard(board, width, height)


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
