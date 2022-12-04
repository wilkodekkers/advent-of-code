from solutions import Solution


class Solution4(Solution):

    def __init__(self):
        super().__init__()
        self.elf_pairs = []

    def load(self, path_to_input_file: str) -> "Solution":
        super().load(path_to_input_file)
        self.elf_pairs = list(map(self.parse_elves, self.lines))
        return self

    @staticmethod
    def parse_elves(line: str) -> list:
        return [list(map(lambda val: int(val), x.split('-'))) for x in line.split(',')]

    @staticmethod
    def calc_dif(line) -> list[bool, bool, bool, bool]:
        return [
            line[1][0] - line[0][0] >= 0,
            line[1][0] - line[0][1] > 0,
            line[1][1] - line[0][0] >= 0,
            line[1][1] - line[0][1] > 0
        ]

    @staticmethod
    def sub_in_pair(pair) -> bool:
        if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]:
            return True
        elif pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:
            return True
        return False

    def part1(self) -> int:
        return sum(map(self.sub_in_pair, self.elf_pairs))

    def part2(self) -> int:
        dif_list = map(self.calc_dif, self.elf_pairs)
        solution = [
            [True, False, True, True],
            [True, False, True, False],
            [False, False, True, True],
            [False, False, True, False],
        ]
        return sum(x in solution for x in dif_list)
