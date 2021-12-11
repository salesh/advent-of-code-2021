# Generate two new binary numbers
# gama rate, epsilon rate
# power = game rate * epsilon rate

# Each bit in the gamma rate can be determined by
# finding the most common bit in the corresponding
# position of all numbers in the diagnostic report.

# The epsilon rate is the least common bit from
# each position is used.

fp = open('input1.txt')

data = fp.read().splitlines()
dictSum = {zero: 0 for zero in range(len(data[0]))}

for value in data:
    for i, val in enumerate(value):
        dictSum[i] += int(val)

gama_rate = ''
beta_rate = ''

lengthOfData = len(data)
for k, v in dictSum.items():
    if v > lengthOfData / 2:
        gama_rate += '1'
        beta_rate += '0'
    else:
        gama_rate += '0'
        beta_rate += '1'

print(int(gama_rate, 2) * int(beta_rate, 2))

fp.close()
