from solutions import Solution


class Solution1(Solution):

    def __init__(self):
        super().__init__()
        self.elf_list = []

    def load(self, path_to_input_file: str) -> "Solution":
        super().load(path_to_input_file)
        self.fill_elf_list()
        return self

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
