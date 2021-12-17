def getData():
    f = open('input.txt')
    data = f.read().splitlines()

    f.close()
    return data


def calculate_new_velocity_y(y):
    return y - 1


def calculate_new_velocity_x(x):
    pom_x = x
    if x > 0:
        pom_x -= 1
    elif x < 0:
        pom_x += 1
    else:
        pom_x = 0
    return pom_x


if __name__ == '__main__':

    # target area: x=20..30, y=-10..-5
    # target area: x=241..275, y=-75..-49
    # x_min = 20
    # x_max = 30
    # y_min = -10
    # y_max = -5
    x_min = 241
    x_max = 275
    y_min = -75
    y_max = -49
    result_highest_y = []
    for index_x in range(x_max + 1):
        for index_y in range(abs(y_min + 1), y_min - 1, -1):
            probe_x = 0
            probe_y = 0
            x_velocity = index_x
            y_velocity = index_y
            highest_y = probe_y
            while True:
                probe_x += x_velocity
                probe_y += y_velocity

                if highest_y < probe_y:
                    highest_y = probe_y

                if x_velocity == 0:
                    if not x_max >= probe_x >= x_min:
                        break
                    elif probe_y < y_min:
                        break

                if x_max >= probe_x >= x_min and y_max >= probe_y >= y_min:
                    result_highest_y.append(highest_y)
                    break

                x_velocity = calculate_new_velocity_x(x_velocity)
                y_velocity = calculate_new_velocity_y(y_velocity)

    print(f'Part 1: {sorted(result_highest_y)[-1]}')
    print(f'Part 2: {len(result_highest_y)}')
