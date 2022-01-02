#!/usr/bin/python3
"""
File input module
"""
import fileinput


def get_data():
    data = []
    for file_line in fileinput.input():
        file_line = file_line.strip()
        for string in file_line.split(","):
            data.append(int(string))
    return data


def execute(data, noun, verb):
    index = 0
    data[1] = noun
    data[2] = verb
    while index < len(data):
        if data[index] == 1:
            data[data[index + 3]] = data[data[index + 1]] + data[data[index + 2]]
        elif data[index] == 2:
            data[data[index + 3]] = data[data[index + 1]] * data[data[index + 2]]
        elif data[index] == 99:
            break
        index += 4
    return data


# part 1
print("day 1: {0}".format(execute(get_data(), 12, 2)[0]))

# part 2
print("day 2: {0}".format(next(
    100 * noun + verb for noun in range(100) for verb in range(100) if execute(get_data(), noun, verb)[0] == 19690720)))
