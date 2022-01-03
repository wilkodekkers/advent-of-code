import hashlib


def find_hash(pub, lookup):
    index = 0
    while True:
        string = pub + str(index)
        res = hashlib.md5(string.encode()).hexdigest()
        if res[:len(lookup)] == lookup:
            return index
        index += 1


def main():
    print("part 1: {0}".format(find_hash("yzbqklnj", "00000")))
    print("part 2: {0}".format(find_hash("yzbqklnj", "000000")))


if __name__ == "__main__":
    main()
