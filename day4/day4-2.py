def findLatestWinnerBoards(markingBoards, markedPositions):
    indexResultBoard = []
    result = []
    for indexMarkedBoard, board in enumerate(markingBoards):
        if not indexMarkedBoard in markedPositions:
            for row in board:
                if 'X' not in row:
                    result.append(row)
                    indexResultBoard.append(indexMarkedBoard)
            for column in zip(*board):
                if 'X' not in column:
                    result.append(column)
                    indexResultBoard.append(indexMarkedBoard)

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

markedPositions = {}
for indexBingoNumber, bingoNumber in enumerate(bingoNumbers):
    for indexBoard, board in enumerate(allBoards):
        if not indexBoard in markedPositions:
            for indexBoardRow, row in enumerate(board):
                if bingoNumber in row:
                    markingBoards[indexBoard][indexBoardRow][row.index(
                        bingoNumber)] = bingoNumber

    winnerBoard = findLatestWinnerBoards(markingBoards, markedPositions)
    if not winnerBoard[0] == -1:
        for item in winnerBoard[0]:
            sumNonMarkedNumbers = calculateNotMarkedNumbers(
                item, markingBoards[item], allBoards)
            markedPositions[item] = sumNonMarkedNumbers * int(bingoNumber)


print('First winner board {0} value {1}'.format(
    next(iter(markedPositions)), next(iter(markedPositions.values()))))
print('Last winner board {0} value {1}'.format(
    next(reversed(markedPositions.keys())), next(reversed(markedPositions.values()))))


fp.close()
