data = []

with open("day2.txt") as file:
    data = [line.strip() for line in file.readlines()]


def part1(boxes):
    total = 0
    for box in boxes:
        l, w, h = [int(x) for x in box.split("x")]
        sides = [2 * l * w, 2 * w * h, 2 * h * l]
        total += int(sum(sides) + min(sides) / 2)
    return total


def part2(boxes):
    total = 0
    for box in boxes:
        sides = [int(x) for x in box.split("x")]
        a, b, c = sorted(sides)[:3]
        total += a * 2 + b * 2 + a * b * c
    return total


def main():
    print("part 1: {0}".format(part1(data)))
    print("part 2: {0}".format(part2(data)))


if __name__ == "__main__":
    main()
