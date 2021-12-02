
horizontal = 0
depth = 0
aim = 0

fp = open('input1.txt')
movingData = fp.read().splitlines()

for inx, move in enumerate(movingData):
    moveInstruction, moveValue = move.split(' ')
    moveValue = int(moveValue)
    if moveInstruction == 'forward':
        horizontal += moveValue
        depth += aim * moveValue
    elif moveInstruction == 'down':
        aim += moveValue
    elif moveInstruction == 'up':
        aim -= moveValue
    else:
        print('Invalid move')

print(horizontal * depth)
fp.close()
