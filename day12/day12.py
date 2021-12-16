def getData():
    f = open('input0.txt')
    data = f.read().splitlines()
    f.close()
    return data


def count_distinct_paths(graph, can_duplicate):
    # Keeping path + can duplicate further
    paths_list = [(('start',), not can_duplicate)]

    distinct = 0
    while paths_list:
        # get last one and check if we are at end
        path, duplicate = paths_list.pop()
        if path[-1] == 'end':
            distinct += 1
        else:
            # check all neighbors
            for neighbor in graph[path[-1]]:
                # neighbor is big letter or he is small letter and he is not in path
                if neighbor.isupper() or neighbor not in path:
                    paths_list.append((path + (neighbor,), duplicate))
                # part 2 , we can't go from start again
                elif not duplicate and neighbor != 'start':
                    paths_list.append((path + (neighbor,), True))
    return distinct


if __name__ == '__main__':
    data = getData()

    input_list = [line.split('-') for line in data]
    graph = {}
    for input in input_list:
        k, v = input[:2]

        # This was my mistake - I had only k directions...
        graph.setdefault(k, []).append(v)
        graph.setdefault(v, []).append(k)

    print(f'Part 1 {count_distinct_paths(graph, False)}')
    print(f'Part 2 {count_distinct_paths(graph, True)}')
