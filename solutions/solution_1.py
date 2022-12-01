from dataclasses import dataclass

from solutions.solution import Solution


@dataclass
class Solution1(Solution):
    elf_list = []

    def __init__(self, path_to_input: str):
        super().__init__(path_to_input)
        self.fill_elf_list()

    def part1(self) -> int:
        return max(self.elf_list)

    def part2(self) -> int:
        return sum(sorted(self.elf_list, reverse=True)[0:3])

    def fill_elf_list(self):
        elf = 0
        for calorie in self.lines:
            if calorie:
                elf += int(calorie)
            else:
                self.elf_list.append(elf)
                elf = 0
