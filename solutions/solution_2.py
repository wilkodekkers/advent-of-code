from solutions import Solution


class Solution2(Solution):
    ACTION_SCORE = {
        'A': 1,
        'B': 2,
        'C': 3,
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    def part1(self) -> int:
        score = 0
        for line in self.lines:
            opponent, me = line.split(" ")
            base = self.ACTION_SCORE[me]
            result = (self.ACTION_SCORE[opponent], self.ACTION_SCORE[me])
            bonus_points = 0
            match result:
                case (1, 2) | (2, 3) | (3, 1):
                    bonus_points = 6
                case (a, b):
                    bonus_points = 3 if (a == b) else 0
            score += base + bonus_points
        return score

    def part2(self) -> int:
        score = 0
        for line in self.lines:
            opponent, me = line.split(" ")
            opponent = self.ACTION_SCORE[opponent]
            me = self.ACTION_SCORE[me]
            match me:
                case 1:
                    me = 3 if (opponent - 1 < 1) else opponent - 1
                case 2:
                    me = opponent
                case 3:
                    me = 1 if (opponent + 1 > 3) else opponent + 1
                case _:
                    me = 0
            result = (opponent, me)
            bonus_points = 0
            match result:
                case (1, 2) | (2, 3) | (3, 1):
                    bonus_points = 6
                case (a, b):
                    bonus_points = 3 if (a == b) else 0
            score += me + bonus_points
        return score
