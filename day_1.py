def main():
    with open("day_1.txt") as f:
        elf_list = []
        elf = 0
        for calorie in [line.rstrip() for line in f.readlines()]:
            if calorie:
                elf += int(calorie)
            else:
                elf_list.append(elf)
                elf = 0
        print(max(elf_list))
        print(sum(sorted(elf_list, reverse=True)[0:3]))


if __name__ == "__main__":
    main()
