import operator


def getData():
    f = open('input1.txt')
    data = f.read().splitlines()
    f.close()
    return data


def calculateOccurrenceDifference(new_template):
    dict_occurrences = {}
    for character in new_template:
        if character in dict_occurrences:
            dict_occurrences[character] += 1
        else:
            dict_occurrences[character] = 1

    min = list(dict_occurrences.values())[0]
    max = min
    for k, v in dict_occurrences.items():
        if v > max:
            max = v
        if v < min:
            min = v
    return max - min


if __name__ == '__main__':

    data = getData()

    template = data[0]
    paths = {}
    for pair in data[2:]:
        key, value = pair.split('->')
        paths[key.strip()] = value.strip()

    pairs = list(map(operator.concat, template[:-1], template[1:]))

    new_pairs = pairs.copy()
    new_template = ''
    for x in range(10):
        help_list = []
        for index, pair in enumerate(pairs):
            if pair in paths:
                new_pair = new_pairs[index][:1] + paths[pair]
                # for end pair keep ending char
                if index + 1 == len(pairs):
                    new_pairs[index] = new_pair + new_pairs[index][1:]
                else:
                    new_pairs[index] = new_pair
                new_template = ''.join(map(str, new_pairs))

                help_list = list(
                    map(operator.concat, new_template[:-1], new_template[1:]))

        pairs = help_list
        new_pairs = pairs
        print(f'After step {x + 1}: {new_template}')

    print(
        f'Max occurrence - min occurrence {calculateOccurrenceDifference(new_template)}')
