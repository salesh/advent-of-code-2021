def getData():
    f = open('input1.txt')
    data = f.read().splitlines()
    return data


if __name__ == '__main__':
    data = getData()
    occurrences = 0

    for line in data:
        signal, output = line.split('|')
        outputWords = output.strip().split(' ')
        lineWords = signal.strip().split(' ')
        for outputWord in outputWords:
            if len(outputWord) in [2, 3, 4, 7]:
                occurrences += 1

    print(occurrences)
