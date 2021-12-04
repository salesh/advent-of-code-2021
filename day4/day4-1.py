def findWinnerBoard(markingBoards):
    indexResultBoard = -1
    result = []
    for indexMarkedBoard, board in enumerate(markingBoards):
        for row in board:
            if 'X' not in row:
                result = row
                indexResultBoard = indexMarkedBoard
                break
        for column in zip(*board):
            if 'X' not in column:
                result = column
                indexResultBoard = indexMarkedBoard
                break
        if not indexResultBoard == -1:
            break
    return indexResultBoard, result


def calculateNotMarkedNumbers(indexMarkedBoard, markedBoard, allBoards):
    sumNotMarked = 0
    for indexRow, row in enumerate(markedBoard):
        for indexElement, element in enumerate(row):
            if element == 'X':
                sumNotMarked += int(allBoards[indexMarkedBoard]
                                    [indexRow][indexElement])
    return sumNotMarked


fp = open('input1.txt')
data = fp.read().splitlines()

bingoNumbers = []
allBoards = []
helperBoard = []
indexSize = 0
for indexLine, line in enumerate(data):
    if indexLine == 0:
        bingoNumbers = line.strip().split(',')
    else:
        if len(line.strip()) == 0:
            if indexSize > 4:
                allBoards.append(helperBoard)
                indexSize = 0
                helperBoard = []
        else:
            helperBoard.append(list(filter(None, line.split(' '))))
            indexSize += 1

            # Ah special case ** not proud hek **
            if indexLine + 1 == len(data):
                allBoards.append(helperBoard)
                helperBoard = []
                indexSize = 0

boardLength = len(allBoards)
markingBoards = [[['X' for _ in range(5)] for _ in range(5)]
                 for _ in range(boardLength)]

for bingoNumber in bingoNumbers:
    for indexBoard, board in enumerate(allBoards):
        for indexBoardRow, row in enumerate(board):
            if bingoNumber in row:
                markingBoards[indexBoard][indexBoardRow][row.index(
                    bingoNumber)] = bingoNumber

    winnerBoard = findWinnerBoard(markingBoards)
    if not winnerBoard[0] == -1:
        sumNonMarkedNumbers = calculateNotMarkedNumbers(winnerBoard[0],
                                                        markingBoards[winnerBoard[0]], allBoards)
        print(sumNonMarkedNumbers * int(bingoNumber))
        break

fp.close()


# def checkBoardWid():
