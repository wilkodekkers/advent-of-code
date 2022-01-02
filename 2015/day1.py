#!/usr/bin/python3
data = []

with open("day1.txt") as file:
    data = [char for char in file.readline()]


def part1(commands):
    floor = 0
    for x in commands:
        if x == "(":
            floor += 1
        elif x == ")":
            floor -= 1
    return floor


def part2(commands):
    floor = 0
    index = 0
    for x in commands:
        index += 1
        if x == "(":
            floor += 1
        elif x == ")":
            floor -= 1
        if floor == -1:
            return index
    return -1


def main():
    print("part 1: {0}".format(part1(data)))
    print("part 2: {0}".format(part2(data)))


if __name__ == "__main__":
    main()
