from string import ascii_lowercase

with open("day5.txt") as file:
    data = [line.strip() for line in file.readlines()]


def check_vowel_count(string):
    vowel_count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in string:
        if char in vowels:
            vowel_count += 1
    return vowel_count


def contains_excluded_combinations(string):
    exclude = ['ab', 'cd', 'pq', 'xy']
    for pair in exclude:
        if pair in string:
            return True
    return False


def contains_double_character(string):
    for character in ascii_lowercase:
        if character + character in string:
            return True
    return False


def is_nice(string):
    return check_vowel_count(string) >= 3 and \
           not contains_excluded_combinations(string) and \
           contains_double_character(string)


def contains_pair_of_two_letters(string):
    for i in range(len(string) - 2):
        if string[i + 2:].find(string[i] + string[i + 1]) != -1:
            return True
    return False


def letter_repeats_one_letter_between(string):
    for index in range(len(string) - 2):
        if string[index] is string[index + 2]:
            return True
    return False


def new_is_nice(string):
    return contains_pair_of_two_letters(string) and \
           letter_repeats_one_letter_between(string)


def main():
    print("part 1: {0}".format(len([string for string in data if is_nice(string)])))
    print("part 2: {0}".format(len([string for string in data if new_is_nice(string)])))


if __name__ == "__main__":
    main()
