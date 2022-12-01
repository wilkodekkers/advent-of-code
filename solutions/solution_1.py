from solutions.solution import Solution


class Solution1(Solution):
    def __init__(self):
        self.elf_list = []
        with open("solutions/inputs/day_1.txt") as f:
            lines = [line.strip() for line in f.readlines()]
        self.fill_elf_list(lines)

    def part1(self) -> int:
        return max(self.elf_list)

    def part2(self) -> int:
        return sum(sorted(self.elf_list, reverse=True)[0:3])

    def fill_elf_list(self, lines: list[str]):
        elf = 0
        for calorie in [line.rstrip() for line in lines]:
            if calorie:
                elf += int(calorie)
            else:
                self.elf_list.append(elf)
                elf = 0
