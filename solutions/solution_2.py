from solutions import Solution


class Solution2(Solution):
    LOSING_ACTION = {
        'A': 'Z',
        'B': 'X',
        'C': 'Y'
    }

    ACTION = {
        'A': 'Y',
        'B': 'Z',
        'C': 'X'
    }

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
            score += self.calculate_score(opponent, me)
        return score

    def part2(self) -> int:
        score = 0
        for line in self.lines:
            opponent, me = line.split(" ")
            score += self.calculate_action(opponent, me)
        return score

    def rock_strategy(self, me: str) -> int:
        match me:
            case 'X':  # tie
                return 1 + 3
            case 'Y':  # win
                return 2 + 6
            case 'Z':  # lose
                return 3 + 0

    def paper_strategy(self, me: str) -> int:
        match me:
            case 'X':  # lose
                return 1 + 0
            case 'Y':  # tie
                return 2 + 3
            case 'Z':  # win
                return 3 + 6

    def scissors_strategy(self, me: str) -> int:
        match me:
            case 'X':  # win
                return 1 + 6
            case 'Y':  # lose
                return 2 + 0
            case 'Z':  # tie
                return 3 + 3

    def calculate_score(self, opponent: str, me: str) -> int:
        match opponent:
            case 'A':
                return self.rock_strategy(me)
            case 'B':
                return self.paper_strategy(me)
            case 'C':
                return self.scissors_strategy(me)
            case _:
                return 0

    def calculate_action(self, opponent: str, me: str) -> int:
        if me == 'Y':
            return self.ACTION_SCORE[opponent] + 3
        elif me == 'X':
            return self.ACTION_SCORE[self.LOSING_ACTION[opponent]]
        else:
            return self.ACTION_SCORE[self.ACTION[opponent]] + 6
