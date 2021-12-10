def getData():
    f = open('input1.txt')
    return f.read().splitlines()


openBrackets = ['(', '[', '{', '<']
dictPairs = {')': '(', ']': '[', '>': '<', '}': '{'}
dictPairScore = {')': 3, ']': 57, '>': 25137, '}': 1197}

if __name__ == '__main__':
    data = getData()

    result = 0
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
                    result += dictPairScore.get(bracket)
                    break
    print(result)
