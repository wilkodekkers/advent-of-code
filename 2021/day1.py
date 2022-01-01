"""
Fileinput module
"""
import fileinput

DATA = []
COUNT = 0

# initialize data
for line in fileinput.input():
    line = line.strip()
    DATA.append(int(line))

# part 1
for i in range(len(DATA)-1):
    if DATA[i+1] > DATA[i]:
        COUNT += 1

print(f"Part 1: {COUNT}")

# part 2
COUNT = 0
for i in range(len(DATA)-3):
    if DATA[i+1] + DATA[i+2] + DATA[i+3] > DATA[i] + DATA[i+1] + DATA[i+2]:
        COUNT += 1

print(f"Part 2: {COUNT}")
