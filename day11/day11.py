
def getData():
    f = open('input1.txt')
    return f.read().splitlines()


# Thing that I learned <- much smaller code with this one...
neighboars = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
              (0, 1), (1, -1), (1, 0), (1, 1)]


def step(matrix):
    blink = 0
    visitStack = []
    for inxRow in range(10):
        for inxCol in range(10):
            matrix[inxRow][inxCol] += 1
            if matrix[inxRow][inxCol] > 9:
                matrix[inxRow][inxCol] = 0
                blink += 1
                visitStack.append((inxRow, inxCol))
    while visitStack:
        inxRow, inxCol = visitStack.pop()
        for indX, inxY in neighboars:
            posX = inxRow + indX
            posY = inxCol + inxY
            #  matrix[posX][posY] > 0 only for position that didn't blink (i didn't visit)
            if posX >= 0 and posX < 10 and posY >= 0 and posY < 10 and matrix[posX][posY] > 0:
                matrix[posX][posY] += 1
                if matrix[posX][posY] > 9:
                    matrix[posX][posY] = 0
                    blink += 1
                    visitStack.append((posX, posY))
    return blink


def getPart1Result(matrix):
    return sum(step(matrix) for i in range(100))


def getPart2Result(matrix):
    steps = 0
    while sum(map(sum, matrix)) > 0:
        step(matrix)
        steps += 1
    return steps


if __name__ == '__main__':
    matrix = [[int(c) for c in row] for row in getData()]
    print('')
    print(f'Part 1: {getPart1Result([row[:] for row in matrix])}')
    print(f'Part 2: {getPart2Result([row[:] for row in matrix])}')
