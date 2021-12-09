def getData():
    f = open('input1.txt')
    data = f.read().splitlines()
    f.close()

    return data


if __name__ == '__main__':

    data = getData()
    matrix = [[int(number) for number in row] for row in data]
    emptyMatrix = [[0 for __ in range(len(matrix[0]))]
                   for _ in range(len(matrix))]
    numberOfFounded = 0
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

    print(numberOfFounded)
