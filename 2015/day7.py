results = dict()

with open("day7.txt") as file:
    commands = dict()
    for line in file.readlines():
        p = line.strip().split(" -> ")
        commands[p[1]] = p[0]


def find(search):
    if search.isdigit():
        return int(search)

    name = commands[search]
    if name not in results:
        parts = name.split(" ")
        if "AND" in name:
            res = find(parts[0]) & find(parts[2])
        elif "OR" in name:
            res = find(parts[0]) | find(parts[2])
        elif "LSHIFT" in name:
            res = find(parts[0]) << find(parts[2])
        elif "RSHIFT" in name:
            res = find(parts[0]) >> find(parts[2])
        elif "NOT" in name:
            res = ~find(parts[1]) & 0xffff
        else:
            res = find(name)
        results[name] = res
    return results[name]


def main():
    print(find("a"))


if __name__ == "__main__":
    main()
