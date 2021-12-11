def getData():
    f = open('input.txt')
    data = f.read().split(',')
    f.close()

    return [int(i) for i in data]


if __name__ == '__main__':
    data = getData()
    sumData = sum(data)
    lengthData = len(data)

    result = []
    for index in range(int(sumData/lengthData) + 1):
        stepCalc = []
        for point in data:
            stepCalc.append(abs(point-index))
        result.append(sum(stepCalc))

    sortedResult = sorted(result)
    print(f'Index {result.index(sortedResult[0])} sum {sortedResult[0]}')
