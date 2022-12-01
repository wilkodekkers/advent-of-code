"""Abstract Solution Class"""

from abc import ABC, abstractmethod


class Solution(ABC):
    """Base class for defining Solution Classes"""

    def __init__(self):
        self.lines = []

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

    @staticmethod
    def get_file_input(path_to_input: str) -> list[str]:
        """Read file and return a list with contains each line as a string"""
        with open(path_to_input) as f:
            return [line.strip() for line in f.readlines()]

    def load(self, path_to_input_file: str) -> "Solution":
        """Load method that prepares things before the run method is called"""
        self.lines = self.get_file_input(path_to_input_file)
        return self

    def run(self) -> None:
        """Prints the result of part 1 and part 2 to the console"""
        print("Solution")
        print(f"Part 1: {self.part1()}")
        print(f"Part 2: {self.part2()}")
