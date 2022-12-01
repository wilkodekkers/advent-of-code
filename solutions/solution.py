"""Abstract Solution Class"""

from abc import ABC, abstractmethod


class Solution(ABC):
    """Base class for defining Solution Classes"""

    @abstractmethod
    def part1(self) -> int:
        """Returns the result of part 1

        Returns the result of this part
        """

    @abstractmethod
    def part2(self) -> int:
        """Returns the result of part 2

        Returns the result of this part
        """

    def run(self) -> None:
        """Prints the result of part 1 and part 2 to the console"""
        print("Solution")
        print(f"Part 1: {self.part1()}")
        print(f"Part 2: {self.part2()}")
