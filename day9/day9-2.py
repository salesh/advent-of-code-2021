import math


def getData():
    f = open('input1.txt')
    data = f.read().splitlines()
    f.close()

    return data


def populateSpread(matrix, emptyMatrix, indexRow, indexColumn, point):
    emptyMatrix[indexRow][indexColumn] = 1

    if indexColumn - 1 > -1:
        leftNum = matrix[indexRow][indexColumn - 1]
        if leftNum < 9 and not emptyMatrix[indexRow][indexColumn - 1] == 1:
            populateSpread(matrix, emptyMatrix,
                           indexRow, indexColumn - 1, leftNum)

    if indexRow - 1 > -1:
        upNum = matrix[indexRow - 1][indexColumn]
        if upNum < 9 and not emptyMatrix[indexRow - 1][indexColumn] == 1:
            populateSpread(matrix, emptyMatrix,
                           indexRow - 1, indexColumn, upNum)

    if indexRow + 1 < len(matrix):
        downNum = matrix[indexRow + 1][indexColumn]
        if downNum < 9 and not emptyMatrix[indexRow + 1][indexColumn] == 1:
            populateSpread(matrix, emptyMatrix,
                           indexRow + 1, indexColumn, downNum)

    if indexColumn + 1 < len(row):
        rightNum = matrix[indexRow][indexColumn + 1]
        if rightNum < 9 and not emptyMatrix[indexRow][indexColumn + 1] == 1:
            populateSpread(matrix, emptyMatrix,
                           indexRow, indexColumn + 1, rightNum)
    return emptyMatrix


if __name__ == '__main__':

    data = getData()
    matrix = [[int(number) for number in row] for row in data]
    emptyMatrix = [[0 for __ in range(len(matrix[0]))]
                   for _ in range(len(matrix))]
    numberOfFounded = 0
    listBasin = []
    for indexRow, row in enumerate(matrix):
        for indexColumn, number in enumerate(row):
            down = indexRow + 1
            right = indexColumn + 1
            left = indexColumn - 1
            up = indexRow - 1
            lowPoint = number

            # up and left no need to check for value already checked
            if left > -1:
                leftNum = matrix[indexRow][left]
                if emptyMatrix[indexRow][left] == 1 or leftNum <= lowPoint:
                    continue
            if up > -1:
                upNum = matrix[up][indexColumn]
                if emptyMatrix[up][indexColumn] == 1 or upNum <= lowPoint:
                    continue

            if down < len(matrix):
                downNum = matrix[down][indexColumn]
                if downNum <= lowPoint:
                    continue

            if right < len(row):
                rightNum = matrix[indexRow][right]
                if rightNum <= lowPoint:
                    continue

            emptyMatrix[indexRow][indexColumn] = 1
            numberOfFounded += 1 + lowPoint

            spreadMatrix = [[0 for __ in range(len(matrix[0]))]
                            for _ in range(len(matrix))]
            populateSpread(matrix, spreadMatrix,
                           indexRow, indexColumn, lowPoint)
            listBasin.append(sum(map(sum, spreadMatrix)))

    listBasin.sort()
    print(math.prod(listBasin[-3:]))
