fp = open('input.txt')

listDepths = fp.read().splitlines()

count = 0

for index, depth in enumerate(listDepths):
    if len(listDepths) > index + 1:
        # int was messing around with me at begin
        if int(listDepths[index + 1]) > int(listDepths[index]):
            count += 1
            print(f'{listDepths[index + 1]} increase')
        else:
            print(f'{listDepths[index + 1]} decrease')

fp.close()
