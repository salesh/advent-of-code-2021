from collections import defaultdict
from queue import PriorityQueue
import sys


def getData():
    f = open('input1.txt')
    data = f.read().splitlines()
    f.close()

    return data


neighbours = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def dijkstra(matrix):
    height = len(matrix)
    width = len(matrix[0])

    # Big value for comparision
    weights = [[sys.maxsize for __ in range(width)] for _ in range(height)]

    # Init zero i didn't enter first cave
    weights[0][0] = 0

    # Already visited
    visited_mark = defaultdict(tuple)

    # All to visit
    node = (0, 0)
    visit_queue = PriorityQueue()
    visit_queue.put((0, node))

    while not visit_queue.empty():
        current_weight, node = visit_queue.get()
        visited_mark[node] = True

        x, y = node
        for ind_x, ind_y in neighbours:
            pos_x = x + ind_x
            pos_y = y + ind_y

            if len(matrix[0]) > pos_x >= 0 and len(matrix) > pos_y >= 0:
                if not visited_mark[(pos_x, pos_y)]:
                    if current_weight + matrix[pos_x][pos_y] < weights[pos_x][pos_y]:

                        weights[pos_x][pos_y] = current_weight + \
                            matrix[pos_x][pos_y]

                        visit_queue.put(
                            (weights[pos_x][pos_y], (pos_x, pos_y)))

    return weights[height-1][width-1]


if __name__ == '__main__':
    data = getData()

    matrix_part_1 = [[int(num) for num in row] for row in data]

    print(dijkstra(matrix_part_1))

    height = len(matrix_part_1)

    matrix_part_2 = [[0 for _ in range(height * 5)] for _ in range(height * 5)]

    for row_5 in range(5):
        for column_5 in range(5):
            for row in range(height):
                for column in range(height):
                    matrix_part_2[row_5 * height + row][column_5 * height + column] = (
                        matrix_part_1[row][column] + row_5 + column_5 - 1) % 9 + 1

    print(dijkstra(matrix_part_2))
