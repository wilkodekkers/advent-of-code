#!/usr/bin/python3
"""
File input module
"""
import fileinput

data = []
fuel = 0

# initialize data
for line in fileinput.input():
    line = line.strip()
    data.append(int(line))

# part 1
for x in data:
    fuel += int(x / 3) - 2

print(f"part 1: {fuel}")

# part 2
fuel = 0

for x in data:
    RES = 0
    while x > 0:
        x = int(x / 3) - 2
        if x > 0:
            RES += x
    fuel += RES

print(f"part 2: {fuel}")
