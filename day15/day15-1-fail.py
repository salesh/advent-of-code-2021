from collections import deque


class Node:
    def __init__(self, x, y, weight, parent=None):
        self.x = x
        self.y = y
        self.weight = weight
        self.parent = parent

    # String representation
    def __repr__(self) -> str:
        return str((self.x, self.y, self.weight))


def getData():
    f = open('input.txt')
    data = f.read().splitlines()
    f.close()

    return data


def sumWeightsOfPath(current_node):
    sum_weights = current_node.weight
    print(current_node)
    parent = current_node.parent
    while parent:
        print(parent)
        sum_weights += parent.weight
        parent = parent.parent
    return sum_weights


neighbours = [(-1, 0), (0, -1), (0, 1), (1, 0)]
if __name__ == '__main__':
    data = getData()

    matrix = [[int(num) for num in row] for row in data]

    start_node = Node(0, 0, 0)
    end_node = Node(len(matrix[0]) - 1, len(matrix) - 1,
                    matrix[len(matrix) - 1][len(matrix[0]) - 1])

    visit_queue = deque()
    visit_queue.append(start_node)

    visited_mark = set()
    visited_mark.add((start_node.x, start_node.y))

    print(visit_queue)
    while visit_queue:
        current_node = visit_queue.popleft()
        x = current_node.x
        y = current_node.y

        if x == end_node.x and y == end_node.y:
            print(sumWeightsOfPath(current_node))

        for ind_x, ind_y in neighbours:
            pos_x = x + ind_x
            pos_y = y + ind_y

            if len(matrix[0]) > pos_x >= 0 and len(matrix) > pos_y >= 0:
                next_node = Node(
                    pos_x, pos_y, matrix[pos_y][pos_x], current_node)

                coordinates = (next_node.x, next_node.y)

                if coordinates not in visited_mark:
                    visit_queue.append(next_node)
                    visited_mark.add(coordinates)

        print(visit_queue)
# fail
