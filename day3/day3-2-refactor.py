# oxygen generator rating, determine the most common value (0 or 1)
# if equal keep the ones with 1

# CO2 scrubber rating, determine least common value (0 or 1)
# if equal keep the ones with 0

# whenever eliminate on position you need to calculate again sum dict
# of binary numbers that are left in list for next position


def calculateRating(ratingList, dataLength, ratingType, currentPos=0):
    while 1:
        ratingListLength = len(ratingList)
        if ratingListLength == 1:
            break

        dictPositionSums = buildPositionSums(ratingList, dataLength)
        sumPos = dictPositionSums.get(currentPos)

        newRatingList = []
        for value in ratingList:
            if sumPos >= ratingListLength / 2:
                if ratingType == 'oxygen' and not value[currentPos] == '0':
                    newRatingList.append(value)
                if ratingType == 'co2scrub' and not value[currentPos] == '1':
                    newRatingList.append(value)
            else:
                if ratingType == 'oxygen' and not value[currentPos] == '1':
                    newRatingList.append(value)
                if ratingType == 'co2scrub' and not value[currentPos] == '0':
                    newRatingList.append(value)
        ratingList = newRatingList
        currentPos += 1
    return ratingList


def buildPositionSums(ratingList, numberLength):
    dictPositionSums = {i: 0 for i in range(numberLength)}
    for rating in ratingList:
        for index, rate in enumerate(rating):
            dictPositionSums[index] += int(rate)
    return dictPositionSums


fp = open('input1.txt')

data = fp.read().splitlines()
dataLength = len(data[0])

ratingList = calculateRating(data, dataLength, 'oxygen', 0)
scrubList = calculateRating(data, dataLength, 'co2scrub', 0)

print(int(ratingList[0], 2) * int(scrubList[0], 2))

fp.close()
