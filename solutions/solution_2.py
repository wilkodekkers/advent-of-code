from solutions import Solution


class Solution2(Solution):

    def part1(self) -> int:
        score = 0
        for line in self.lines:
            op, me = line.split()
            score += {'X': 1, 'Y': 2, 'Z': 3}[me]
            score += {('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
                      ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
                      ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3}[(op, me)]
        return score

    def part2(self) -> int:
        score = 0
        for line in self.lines:
            op, me = line.split()
            score += {'X': 0, 'Y': 3, 'Z': 6}[me]
            score += {('A', 'X'): 3, ('A', 'Y'): 1, ('A', 'Z'): 2,
                      ('B', 'X'): 1, ('B', 'Y'): 2, ('B', 'Z'): 3,
                      ('C', 'X'): 2, ('C', 'Y'): 3, ('C', 'Z'): 1}[(op, me)]
        return score
