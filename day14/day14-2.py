from collections import Counter


def getData():
    f = open('input1.txt')
    data = f.read().splitlines()
    f.close()
    return data


if __name__ == '__main__':

    data = getData()
    template = data[0]
    count_letters = Counter(template)

    paths = {}
    for pair in data[2:]:
        key, value = pair.split(' -> ')
        paths[key] = value

    all_mappings = Counter(template[index: index + 2]
                           for index in range(len(template) - 1))

    for index_steps in range(40):
        dict_help = Counter()
        for pair_of_letters, num in all_mappings.items():
            if pair_of_letters in paths:
                first_letter, second_letter = pair_of_letters
                path_rule = paths[pair_of_letters]

                dict_help[first_letter + path_rule] += num
                dict_help[path_rule + second_letter] += num

                count_letters[path_rule] += num
            else:
                dict_help[pair_of_letters] = num
        all_mappings = dict_help
    print(all_mappings)
    print(
        f'Max occurrence - min occurrence {max(count_letters.values()) - min(count_letters.values())}')
