def getData():
    f = open('input1.txt')
    return f.read().splitlines()


openBrackets = ['(', '[', '{', '<']
dictPairs = {')': '(', ']': '[', '>': '<', '}': '{'}
dictPairBadScore = {')': 3, ']': 57, '>': 25137, '}': 1197}
dictPairCorrectScore = {')': 1, ']': 2, '>': 4, '}': 3}

goodScores = []
if __name__ == '__main__':
    data = getData()

    resultBad = 0
    resultGood = 0
    for line in data:
        stack = []
        for bracket in line:
            if bracket in openBrackets:
                stack.append(bracket)
            else:
                myPair = dictPairs.get(bracket)
                if stack[-1] == myPair:
                    stack.pop()
                else:
                    resultBad += dictPairBadScore.get(bracket)
                    stack = []
                    break

        dictPairsInverted = {v: k for k, v in dictPairs.items()}
        if len(stack) > 0:
            for bracket in reversed(stack):
                myPair = dictPairsInverted.get(bracket)
                resultGood = 5 * resultGood + dictPairCorrectScore.get(myPair)
            goodScores.append(resultGood)
            resultGood = 0
    print(f'Bad format score {resultBad}')
    print(
        f'Good format closing score {sorted(goodScores)[int(len(goodScores) / 2)]}')
