def getData():
    f = open('input1.txt')
    data = f.read().split(',')
    f.close()

    return [int(i) for i in data]


def calculateStep(n):
    step = 0
    for index in range(n):
        step += 1 + index
        index += 1
    return step


if __name__ == '__main__':
    data = getData()
    sumData = sum(data)
    lengthData = len(data)

    result = []
    for index in range(int(round(sumData/lengthData)) + 1):
        stepCalc = []
        for point in data:
            stepCalc.append(calculateStep(abs(point-index)))
        result.append(sum(stepCalc))

    sortedResult = sorted(result)

    print(f'Index {result.index(sortedResult[0])} sum {sortedResult[0]}')
