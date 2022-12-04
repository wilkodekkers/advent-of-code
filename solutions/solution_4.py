from solutions import Solution


class Solution4(Solution):

    def __init__(self):
        super().__init__()
        self.data = []

    def load(self, path_to_input_file: str) -> "Solution":
        super().load(path_to_input_file)
        self.data = [[int(n) for elf in line.split(',') for n in elf.split('-')] for line in self.lines]
        return self

    def part1(self) -> int:
        return sum((a >= c and b <= d) or (c >= a and d <= b) for a, b, c, d in self.data)

    def part2(self) -> int:
        return sum(b >= c and d >= a for a, b, c, d in self.data)
