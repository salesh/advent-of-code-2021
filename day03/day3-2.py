# oxygen generator rating, determine the most common value (0 or 1)
# if equal keep the ones with 1

# CO2 scrubber rating, determine least common value (0 or 1)
# if equal keep the ones with 0

# whenever eliminate on position you need to calculate again sum dict
# of binary numbers that are left in list for next position

fp = open('input.txt')

data = fp.read().splitlines()

oxygenList = data.copy()
currentPos = 0
while 1:
    lengthOxygenList = len(oxygenList)
    if lengthOxygenList == 1:
        break

    dictSum = {zero: 0 for zero in range(len(data[0]))}
    for value in oxygenList:
        for i, val in enumerate(value):
            dictSum[i] += int(val)

    sumPos = dictSum.get(currentPos)

    newList = []
    for pos, value in enumerate(oxygenList):
        if sumPos >= lengthOxygenList / 2:
            if not value[currentPos] == '0':
                newList.append(value)
        else:
            if not value[currentPos] == '1':
                newList.append(value)

    oxygenList = newList
    currentPos += 1

scrubList = data.copy()
currentPos = 0
while 1:
    lengthScrubList = len(scrubList)
    if lengthScrubList == 1:
        break

    dictSum = {i: 0 for i in range(len(data[0]))}
    for value in scrubList:
        for i, val in enumerate(value):
            dictSum[i] += int(val)

    sumPos = dictSum.get(currentPos)

    newList = []
    for pos, value in enumerate(scrubList):
        if sumPos >= lengthScrubList / 2:
            if not value[currentPos] == '1':
                newList.append(value)
        else:
            if not value[currentPos] == '0':
                newList.append(value)

    scrubList = newList
    currentPos += 1

print(int(oxygenList[0], 2) * int(scrubList[0], 2))

fp.close()
