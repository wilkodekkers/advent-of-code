from string import ascii_letters

from solutions import Solution


class Solution3(Solution):

    def part1(self) -> int:
        score = 0
        for line in self.lines:
            rucksack1 = set(list(line[:len(line) // 2]))
            rucksack2 = set(list(line[len(line) // 2:]))
            common_character = rucksack1 & rucksack2
            char = ''.join(common_character)
            score += ascii_letters.index(char) + 1
        return score

    def part2(self) -> int:
        score = 0
        n = 3
        for i in range(0, len(self.lines) - n + 1, n):
            rucksacks = self.lines[i:i + n]
            rucksack1 = set(list(rucksacks[0]))
            rucksack2 = set(list(rucksacks[1]))
            rucksack3 = set(list(rucksacks[2]))
            common_character = rucksack1 & rucksack2 & rucksack3
            char = ''.join(common_character)
            score += ascii_letters.index(char) + 1
        return score
