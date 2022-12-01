from abc import ABC, abstractmethod


class Solution(ABC):
    @abstractmethod
    def part1(self) -> any:
        """Returns the result of part 1"""

    @abstractmethod
    def part2(self) -> any:
        """Returns the result of part 2"""

    def run(self) -> None:
        """Prints the result of part 1 and part 2 to the console"""
        print("Solution")
        print(f"Part 1: {self.part1()}")
        print(f"Part 2: {self.part2()}")
