
def getLines():
    file = open('input1.txt')

    data = file.read().splitlines()

    lines = []
    for pair in data:
        lines.append(pair.split('->'))

    file.close()

    return lines


# TODO Fixed 1000 x 1000 - bad thing to assume something like this
# wasted memory...
markPositions = [[0 for _ in range(1000)] for _ in range(1000)]
lines = getLines()
largestOverlap = 0
for index, line in enumerate(lines):
    point1 = line[0].strip().split(',')
    point2 = line[1].strip().split(',')

    x1 = int(point1[0])
    y1 = int(point1[1])
    x2 = int(point2[0])
    y2 = int(point2[1])

    if x1 == x2:
        # y1 and y2 are different
        maxY = max(y1, y2)
        minY = min(y1, y2)
        while maxY >= minY:
            markPositions[maxY][x1] += 1
            if markPositions[maxY][x1] > largestOverlap:
                largestOverlap = markPositions[maxY][x1]
            maxY -= 1
    elif y1 == y2:
        # x1 and x2 are different
        maxX = max(x1, x2)
        minX = min(x1, x2)
        while maxX >= minX:
            markPositions[y1][maxX] += 1
            if markPositions[y1][maxX] > largestOverlap:
                largestOverlap = markPositions[y1][maxX]
            maxX -= 1
    else:
        print('ignore diagonal ', x1, y1, x2, y2)

result = 0
for pos in markPositions:
    print(pos)

print('largestOverlap: ', largestOverlap)
# TODO probably there is smarter way than this
print('Bigger than one overlap : ',
      len(list(filter(lambda x: x > 1, [el for pos in markPositions for el in pos]))))
