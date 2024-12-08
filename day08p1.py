from copy import deepcopy


def main():
    with open("input8.txt", "r") as file:
        p1 = 0
        lines = file.readlines()
        # antenna_pos = []
        for i, line in enumerate(lines):
            line = list(line.strip())
            lines[i] = line

        copyl = deepcopy(lines)

        for i in range(len(lines)):
            for j in range(len(line)):
                for l in range(1, len(lines) - i):
                    for k in range(1, len(line) - j):
                        if lines[i][j] != "." and lines[i][j] == lines[i + l][j + k]:
                            print(
                                f"{i + 2 * l} {j + 2 * k} and {i - 1 * l} {j - 1 * k}"
                            )
                            if (
                                (i + 2 * l) < len(lines)
                                and (j + 2 * k) < len(line)
                                and copyl[i + 2 * l][j + 2 * k] != "#"
                            ):
                                p1 += 1
                                copyl[i + 2 * l][j + 2 * k] = "#"
                            if (
                                (i - 1 * l) >= 0
                                and (j - 1 * k) >= 0
                                and copyl[i - 1 * l][j - 1 * k] != "#"
                            ):
                                p1 += 1
                                copyl[i - 1 * l][j - 1 * k] = "#"
                    for k in range(j, -1, -1):
                        if lines[i][j] != "." and lines[i][j] == lines[i + l][j - k]:
                            print(
                                f"{i + 2 * l} {j - 2 * k} and {i - 1 * l} {j + 1 * k}"
                            )
                            if (
                                (i + 2 * l) < len(lines)
                                and (j - 2 * k) >= 0
                                and copyl[i + 2 * l][j - 2 * k] != "#"
                            ):
                                p1 += 1
                                copyl[i + 2 * l][j - 2 * k] = "#"
                            if (
                                (i - 1 * l) >= 0
                                and (j + 1 * k) < len(line)
                                and copyl[i - 1 * l][j + 1 * k] != "#"
                            ):
                                p1 += 1
                                copyl[i - 1 * l][j + 1 * k] = "#"
        for line in lines:
            print(line)
        print("---")
        for line in copyl:
            print(line)
        print(p1)


main()
