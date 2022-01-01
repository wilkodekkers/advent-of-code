#!/usr/bin/python3
"""
File input module
"""
import fileinput

data = []
horizontal = 0
depth = 0
aim = 0

# initialize data
for line in fileinput.input():
    line = line.strip()
    data.append(line)

# part 1
for line in data:
    parts = line.split(" ")
    if parts[0] == "forward":
        horizontal += int(parts[1])
    if parts[0] == "down":
        depth += int(parts[1])
    if parts[0] == "up":
        depth -= int(parts[1])

print(f"part 1: {horizontal * depth}")

# part 2
horizontal = 0
depth = 0

for line in data:
    parts = line.split(" ")
    if parts[0] == "down":
        aim += int(parts[1])
    if parts[0] == "up":
        aim -= int(parts[1])
    if parts[0] == "forward":
        horizontal += int(parts[1])
        depth += aim * int(parts[1])

print(f"part 2: {horizontal * depth}")
