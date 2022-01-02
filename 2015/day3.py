data = []

with open("day3.txt") as file:
    data = [line.strip() for line in file.readline()]


def part1(commands):
    locations = [(0, 0)]
    pos = [0, 0]
    for command in commands:
        if command == 'v':
            pos[1] += 1
        elif command == '>':
            pos[0] += 1
        elif command == '^':
            pos[1] -= 1
        elif command == '<':
            pos[0] -= 1
        locations.append(tuple(pos))
    return len(set(locations))


def part2(commands):
    locations = [(0, 0)]
    santa = [0, 0]
    robot = [0, 0]
    santa_turn = True
    for command in commands:
        if command == 'v':
            if santa_turn:
                santa[1] += 1
            else:
                robot[1] += 1
        elif command == '>':
            if santa_turn:
                santa[0] += 1
            else:
                robot[0] += 1
        elif command == '^':
            if santa_turn:
                santa[1] -= 1
            else:
                robot[1] -= 1
        elif command == '<':
            if santa_turn:
                santa[0] -= 1
            else:
                robot[0] -= 1
        locations.append(tuple(santa if santa_turn else robot))
        santa_turn = False if santa_turn else True
    return len(set(locations))


def main():
    print("part 1: {0}".format(part1(data)))
    print("part 2: {0}".format(part2(data)))


if __name__ == "__main__":
    main()
