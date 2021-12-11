def getData():
    f = open('input1.txt')
    return f.read().splitlines()


def findFixed(outputWord, dictResult):
    if len(outputWord) == 2:
        dictResult[1] = outputWord
    elif len(outputWord) == 3:
        dictResult[7] = outputWord
    elif len(outputWord) == 4:
        dictResult[4] = outputWord
    elif len(outputWord) == 7:
        dictResult[8] = outputWord


def sortListFormat(input):
    return list(map(lambda w: ''.join(sorted(w)), input))


if __name__ == '__main__':
    data = getData()

    outputLines = list(
        map(sortListFormat, [line.split('|')[1].strip().split() for line in data]))
    inputLines = list(
        map(sortListFormat, [line.split('|')[0].strip().split() for line in data]))

    listDictInvert = []
    for lineWords in inputLines:
        dictResult = {}

        # default 2, 3, 4, 7
        for inputWord in lineWords:
            if len(inputWord) in [2, 3, 4, 7]:
                findFixed(inputWord, dictResult)

        # Find 6
        for word in lineWords:
            if len(word) == 6 and any(c not in word for c in dictResult[1]):
                dictResult[6] = word
                break

        # Find 0
        for word in lineWords:
            if len(word) == 6 and any(char not in word for char in dictResult[4]) and word not in dictResult.values():
                dictResult[0] = word
                break

        # Find 9
        for word in lineWords:
            if len(word) == 6 and not word in dictResult.values():
                dictResult[9] = word
                break

        # Find 5
        for word in lineWords:
            if len(word) == 5 and all(c in dictResult[6] for c in word) and word not in dictResult.values():
                dictResult[5] = word
                break

        # Find 3
        for word in lineWords:
            if len(word) == 5 and all(c in dictResult[9] for c in word) and word not in dictResult.values():
                dictResult[3] = word
                break

        # find 2
        for word in lineWords:
            if len(word) == 5 and word not in dictResult.values():
                dictResult[2] = word
                break

        listDictInvert.append({v: k for k, v in dictResult.items()})

    print(listDictInvert)

    result = 0
    for index, outputWords in enumerate(outputLines):
        result += int(''.join(map(str,
                      [listDictInvert[index][word] for word in outputWords])))

    print(f'Sum {result}')
