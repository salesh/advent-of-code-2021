import math

should_update = False


class Node:
    def __init__(self, left, right, value) -> None:
        self.parent = None
        self.left = left
        self.right = right
        self.value = value


def getData():
    f = open('input.txt')
    data = f.read().splitlines()
    f.close()
    return data


def create_binary_tree(value):
    if type(value) == int:
        return Node(None, None, value)

    left = value[0]
    right = value[1]

    left_node = create_binary_tree(left)
    right_node = create_binary_tree(right)

    parent = Node(left_node, right_node, None)

    left_node.parent = parent
    right_node.parent = parent

    return parent


def add_pair(left_node, right_node):
    node = Node(left_node, right_node, None)
    left_node.parent = node
    right_node.parent = node

    return node


def add_left_sibling(target, value):
    original = target
    while target.left is None or target.left is original:
        original = target
        target = target.parent

        if target is None:
            return

    target = target.left

    while target.right is not None:
        target = target.right

    target.value += value


def add_right_sibling(target, value):
    original = target

    while target.right is None or target.right is original:
        original = target
        target = target.parent

        if target is None:
            return
    target = target.right

    while target.left is not None:
        target = target.left

    target.value += value


def reduce_explode(root, depth=0):
    global should_update

    if root is None or should_update:
        return root

    if depth == 4 and root.value is None:
        left = root.left
        right = root.right

        if left.value is not None and right.value is not None:
            add_left_sibling(left, left.value)
            add_right_sibling(right, right.value)

            should_update = True
            return Node(None, None, 0)

    left = reduce_explode(root.left, depth + 1)
    right = reduce_explode(root.right, depth + 1)

    if left is not None:
        left.parent = root

    if right is not None:
        right.parent = root

    root.left = left
    root.right = right

    return root


def reduce_split(root, depth=0):
    global should_update

    if root is None or should_update:
        return root

    if root.value is not None:

        if root.value >= 10:

            left_value = math.floor(root.value / 2)
            right_value = math.ceil(root.value / 2)

            left_node = Node(None, None, left_value)
            right_node = Node(None, None, right_value)

            parent = Node(left_node, right_node, None)

            left_node.parent = parent
            right_node.parent = parent

            should_update = True

            return parent

    left = reduce_split(root.left, depth + 1)
    right = reduce_split(root.right, depth + 1)

    if left is not None:
        left.parent = root

    if right is not None:
        right.parent = root

    root.left = left
    root.right = right

    return root


def create_pair_list(root):
    if root.value is None:
        return [create_pair_list(root.left), create_pair_list(root.right)]
    else:
        return root.value


def calculate_magnitude(pairs):

    if type(pairs) == int:
        return pairs

    return 3 * calculate_magnitude(pairs[0]) + 2 * calculate_magnitude(pairs[1])


def part_1(lines):
    global should_update

    current_node = None

    for line in lines:
        pairs = eval(line)

        if current_node is None:
            current_node = create_binary_tree(pairs)
            continue

        binary_tree = create_binary_tree(pairs)
        current_node = add_pair(current_node, binary_tree)

        while True:
            current_node = reduce_explode(current_node)

            if should_update:
                should_update = False
                continue

            current_node = reduce_split(current_node)

            if should_update:
                should_update = False
                continue

            break

    print(f'Part 1 {calculate_magnitude(create_pair_list(current_node))}')


def part_2(lines):
    global should_update

    max_magnitude = float("-inf")

    for first in lines:
        for second in lines:
            p_1, p_2 = eval(first), eval(second)

            current_node = add_pair(
                create_binary_tree(p_1), create_binary_tree(p_2))

            while True:

                current_node = reduce_explode(current_node)

                if should_update:
                    should_update = False
                    continue

                current_node = reduce_split(current_node)

                if should_update:
                    should_update = False
                    continue

                break

            max_magnitude = max(max_magnitude, calculate_magnitude(
                create_pair_list(current_node)))

    print(f'Part 2 {max_magnitude}')


if __name__ == '__main__':
    data = getData()
    part_1(data)
    part_2(data)
