#!/usr/bin/python3
"""
File input module
"""
import fileinput

data = []
count = 0

# initialize data
for line in fileinput.input():
    line = line.strip()
    data.append(int(line))

# part 1
for i in range(len(data) - 1):
    if data[i + 1] > data[i]:
        count += 1

print(f"Part 1: {count}")

# part 2
count = 0
for i in range(len(data) - 3):
    if data[i + 1] + data[i + 2] + data[i + 3] > data[i] + data[i + 1] + data[i + 2]:
        count += 1

print(f"Part 2: {count}")
