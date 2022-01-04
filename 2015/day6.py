grid = [[0 for y in range(1000)] for x in range(1000)]

with open("day6.txt") as file:
    commands = [line.strip() for line in file.readlines()]


def string_to_tuple(string):
    return tuple(map(int, string.split(",")))


def change_lights(start, end, value, toggle=False):
    for y in range(start[1], end[1] + 1):
        for x in range(start[0], end[0] + 1):
            if not toggle:
                grid[x][y] = value
            else:
                grid[x][y] = 1 if grid[x][y] == 0 else 0


def execute(command):
    parts = command.split(" ")
    if "turn on" in command:
        change_lights(start=string_to_tuple(parts[2]), end=string_to_tuple(parts[4]), value=1)
    elif "turn off" in command:
        change_lights(start=string_to_tuple(parts[2]), end=string_to_tuple(parts[4]), value=0)
    elif "toggle" in command:
        change_lights(start=string_to_tuple(parts[1]), end=string_to_tuple(parts[3]), value=0, toggle=True)


def new_change_lights(start, end, mode):
    for y in range(start[1], end[1] + 1):
        for x in range(start[0], end[0] + 1):
            if mode == "on":
                grid[x][y] += 1
            elif mode == "off":
                if grid[x][y] > 0:
                    grid[x][y] -= 1
            else:
                grid[x][y] += 2


def new_execute(command):
    parts = command.split(" ")
    if "turn on" in command:
        new_change_lights(start=string_to_tuple(parts[2]), end=string_to_tuple(parts[4]), mode="on")
    elif "turn off" in command:
        new_change_lights(start=string_to_tuple(parts[2]), end=string_to_tuple(parts[4]), mode="off")
    elif "toggle" in command:
        new_change_lights(start=string_to_tuple(parts[1]), end=string_to_tuple(parts[3]), mode="toggle")


def count_turned_on_lights(data):
    count = 0
    for y in range(1000):
        for x in range(1000):
            if data[x][y] == 1:
                count += 1
    return count


def total_brightness(data):
    total = 0
    for y in range(1000):
        for x in range(1000):
            total += data[x][y]
    return total


def reset_grid():
    for y in range(1000):
        for x in range(1000):
            grid[x][y] = 0


def main():
    for command in commands:
        execute(command)
    print("part 1: {0}".format(count_turned_on_lights(grid)))
    reset_grid()
    for command in commands:
        new_execute(command)
    print("part 2: {0}".format(total_brightness(grid)))


if __name__ == "__main__":
    main()
