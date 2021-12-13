def getData():
    f = open('input1.txt')
    data = f.read().splitlines()
    f.close()
    return data


def countDotsInPartOfMatrix(matrix, x, y):
    count = 0
    for indexY in range(y):
        for indexX in range(x):
            if matrix[indexY][indexX] == '█':
                count += 1
    return count


def countDotsOfNStepsAndDrawMatrix(matrix, dots_list, fold_list, max_x, max_y, n):
    for point in dots_list:
        matrix[point[1]][point[0]] = '█'

    new_matrix_x = max_x + 1
    new_matrix_y = max_y + 1
    indexFold = 0
    sumCounts = 0
    for fold in fold_list:
        indexFold += 1
        route, fold_pos = fold
        if route == 'x':
            new_pos_x = fold_pos - 1
            for indexX in range(fold_pos + 1, new_matrix_x):
                for indexY in range(new_matrix_y):
                    if matrix[indexY][indexX] == '█':
                        matrix[indexY][new_pos_x] = '█'
                new_pos_x -= 1
            new_matrix_x = fold_pos

            countResult = countDotsInPartOfMatrix(
                matrix, fold_pos, new_matrix_y)
            sumCounts += countResult
            if n == indexFold:
                return countResult

        elif route == 'y':
            new_pos_y = fold_pos - 1
            for indexY in range(fold_pos + 1, new_matrix_y):
                for indexX in range(new_matrix_x):
                    if matrix[indexY][indexX] == '█':
                        matrix[new_pos_y][indexX] = '█'
                new_pos_y -= 1
            new_matrix_y = fold_pos

            countResult = countDotsInPartOfMatrix(
                matrix, new_matrix_x, fold_pos)
            if n == indexFold:
                return countResult
            sumCounts += countResult
        else:
            print('Nay!')

    helpMatrix = [['.' for __ in range(new_matrix_x + 1)]
                  for _ in range(new_matrix_y + 1)]
    for indexY in range(new_matrix_y + 1):
        for indexX in range(new_matrix_x + 1):
            helpMatrix[indexY][indexX] = matrix[indexY][indexX]
    for line in helpMatrix:
        print(line)
    return sumCounts


if __name__ == '__main__':
    data = getData()

    max_x = 0
    max_y = 0
    dots_list = []
    fold_list = []
    for line in data:
        if line == '':
            continue
        elif line.startswith('fold along'):
            pos, num = line.split(' ')[2].split('=')
            fold_list.append([pos, int(num)])
        else:
            x, y = line.split(',')
            dots_list.append([int(x), int(y)])

            if int(x) > max_x:
                max_x = int(x)
            if int(y) > max_y:
                max_y = int(y)

    matrix = [['.' for __ in range(max_x + 1)] for _ in range(max_y + 1)]

    print(
        f'Only first: {countDotsOfNStepsAndDrawMatrix([row[:] for row in matrix], dots_list, fold_list, max_x, max_y, 1)}')

    print(
        f'All counts: {countDotsOfNStepsAndDrawMatrix([row[:] for row in matrix], dots_list, fold_list, max_x, max_y, -1)}')
