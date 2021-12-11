fp = open('input.txt')

listDepths = fp.read().splitlines()

count = 0
sumFirst = 0
sumSecond = 0

listLength = len(listDepths)
for index, depth in enumerate(listDepths):
    if listLength > index + 3:
        sumFirst = sum(int(x) for x in listDepths[index:index+3])
        sumSecond = sum(int(x) for x in listDepths[index+1:index+4])
        if sumSecond > sumFirst:
            count += 1
print(count)
fp.close()
