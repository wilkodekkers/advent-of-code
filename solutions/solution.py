from abc import ABC


class Solution(ABC):
    def part1(self):
        raise NotImplementedError()

    def part2(self):
        raise NotImplementedError()

    def run(self):
        print("Solution")
        print(f"Part 1: {self.part1()}")
        print(f"Part 2: {self.part2()}")
