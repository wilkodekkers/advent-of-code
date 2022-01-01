#!/usr/bin/python3
"""
Fileinput module
"""
import fileinput

DATA = []
HORIZONTAL = 0
DEPTH = 0
AIM = 0

# initialize data
for line in fileinput.input():
    line = line.strip()
    DATA.append(line)

# part 1
for line in DATA:
    parts = line.split(" ")
    if parts[0] == "forward":
        HORIZONTAL += int(parts[1])
    if parts[0] == "down":
        DEPTH += int(parts[1])
    if parts[0] == "up":
        DEPTH -= int(parts[1])

print(f"part 1: {HORIZONTAL * DEPTH}")

# part 2
HORIZONTAL = 0
DEPTH = 0

for line in DATA:
    parts = line.split(" ")
    if parts[0] == "down":
        AIM += int(parts[1])
    if parts[0] == "up":
        AIM -= int(parts[1])
    if parts[0] == "forward":
        HORIZONTAL += int(parts[1])
        DEPTH += AIM * int(parts[1])

print(f"part 2: {HORIZONTAL * DEPTH}")
