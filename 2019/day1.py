#!/usr/bin/python3
"""
Fileinput module
"""
import fileinput

DATA = []
FUEL = 0

# initialize data
for line in fileinput.input():
    line = line.strip()
    DATA.append(int(line))

# part 1
for x in DATA:
    FUEL += int(x / 3) - 2

print(f"part 1: {FUEL}")

# part 2
FUEL = 0

for x in DATA:
    RES = 0
    while (x > 0):
        x = int(x / 3) - 2
        if x > 0:
            RES += x
    FUEL += RES

print(f"part 2: {FUEL}")
