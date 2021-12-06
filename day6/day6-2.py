NUM_DAYS = 256
DAYS_NEW_FISH = 7


def getDataDict():
    file = open('input1.txt')
    data = [int(x) for x in file.read().split(',')]
    result = {x: 0 for x in range(0, DAYS_NEW_FISH + 2)}

    for value in data:
        result[value] += 1
    file.close()

    return result


def proceses(dictResult):
    numOfFish = sum(dictResult.values())
    print(f'Init count fish: {numOfFish}')
    day = 1
    while NUM_DAYS >= day:
        dictCopy = dictResult.copy()
        for k, v in dictResult.items():
            if not v == 0:
                if k == 0:
                    dictCopy[k] -= v
                    # 8 day add new fishes
                    dictCopy[DAYS_NEW_FISH + 1] += v
                    # 6 day place mothers
                    dictCopy[DAYS_NEW_FISH - 1] += v
                    numOfFish += v
                else:
                    dictCopy[k-1] += v
                    dictCopy[k] -= v
        dictResult = dictCopy
        print(f'After {day} days, count fish: {numOfFish}')
        day += 1


if __name__ == "__main__":
    dictResult = getDataDict()
    proceses(dictResult)
