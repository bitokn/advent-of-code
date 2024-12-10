import copy


def main():
    s = "2333133121414131402"
    s = list(s)
    blox = []
    space_total = 0
    for i in range(0, len(s), 2):
        size = int(s[i])
        for _ in range(size):
            blox.append(i // 2)
        if i != len(s) - 1:
            space = int(s[i + 1])
            space_total += space
            blox += "." * space
    print(space_total)
    print(s)
    print(blox)
    # assert blox == "00...111...2...333.44.5555.6666.777.888899"

    blox = list(blox)
    ogblox = copy.deepcopy(blox)
    oglen = len(blox)
    i = 0
    new_stru = []
    saved = []
    for i in range(oglen):
        # print(f"we are at {i} of {oglen}")
        if i < len(blox):
            if blox[i] != ".":
                new_stru.append(blox[i])
            if blox[i] == "." and blox[-1] != ".":
                new_stru.append(blox[-1])
                del blox[-1]
            elif blox[-1] == ".":
                del blox[-1]
            else:
                saved.append(blox[-1])
                del blox[-1]

        # elif blox[0] == ".":
        #     del blox[0]
        # elif blox[-1] == ".":
        #     del blox[-1]

        # for k in range(1, space_total + 1):
        #     if blox[i] == "." and blox[-k] != ".":
        #         temp = blox[-k]
        #         blox[-k] = blox[i]
        #         blox[i] = temp

    sum = 0

    print(new_stru + saved)

    new_new_stru = new_stru + saved
    #
    for j, blo in enumerate(new_new_stru):
        if blo != ".":
            sum += int(blo) * j

    print(sum)

    # tries:
    # 91033092217
    # 91033092217
    # 2580606367270858829096621157321860717177985
    # 6723756044288
    # 6723756044288
    # 6783612642985
    # 2969186814391
    # 6395800119709 correct !!


main()
