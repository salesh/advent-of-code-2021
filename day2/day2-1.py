
horizontal = 0
depth = 0

fp = open('input1.txt')
movingData = fp.read().splitlines()

for inx, move in enumerate(movingData):
    moveInstruction, moveValue = move.split(' ')
    moveValue = int(moveValue)
    if moveInstruction == 'forward':
        horizontal += moveValue
    elif moveInstruction == 'down':
        depth += moveValue
    elif moveInstruction == 'up':
        depth -= moveValue
    else:
        print('Invalid move')

print(horizontal * depth)
fp.close()
