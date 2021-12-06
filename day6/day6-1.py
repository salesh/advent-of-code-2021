NUM_DAYS = 256
DAYS_NEW_FISH = 7


def getDataList():
    file = open('input1.txt')
    data = [int(x) for x in file.read().split(',')]
    file.close()
    return data


def procesesList(daysUntilNewFishData):
    print('Initial state: ', daysUntilNewFishData)

    day = 1
    result = daysUntilNewFishData.copy()

    while NUM_DAYS >= day:
        newBorns = []
        for index, value in enumerate(result):
            if value == 0:
                result[index] = DAYS_NEW_FISH - 1
                newBorns.append(DAYS_NEW_FISH + 1)
            else:
                result[index] -= 1
        result.extend(newBorns)
        #print(f'After {day} days: {result}, count fish: {len(result)}')
        print(f'After {day} days, count fish: {len(result)}')

        day += 1


if __name__ == "__main__":

    daysUntilNewFishData = getDataList()
    procesesList(daysUntilNewFishData)
