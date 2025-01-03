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
                            for kk in range(max(len(lines), len(line))):
                                print(
                                    f"{i + kk * l} {j + kk * k} and {i - kk * l} {j - kk * k}"
                                )
                                if (
                                    (i + kk * l) < len(lines)
                                    and (j + kk * k) < len(line)
                                    and copyl[i + kk * l][j + kk * k] != "#"
                                ):
                                    p1 += 1
                                    copyl[i + kk * l][j + kk * k] = "#"
                                if (
                                    (i - kk * l) >= 0
                                    and (j - kk * k) >= 0
                                    and copyl[i - kk * l][j - kk * k] != "#"
                                ):
                                    p1 += 1
                                    copyl[i - kk * l][j - kk * k] = "#"
                    for k in range(j, -1, -1):
                        if lines[i][j] != "." and lines[i][j] == lines[i + l][j - k]:
                            for kk in range(max(len(lines), len(line))):
                                print(
                                    f"{i + kk * l} {j - kk * k} and {i - kk * l} {j + kk * k}"
                                )
                                if (
                                    (i + kk * l) < len(lines)
                                    and (j - kk * k) >= 0
                                    and copyl[i + kk * l][j - kk * k] != "#"
                                ):
                                    p1 += 1
                                    copyl[i + kk * l][j - kk * k] = "#"
                                if (
                                    (i - kk * l) >= 0
                                    and (j + kk * k) < len(line)
                                    and copyl[i - kk * l][j + kk * k] != "#"
                                ):
                                    p1 += 1
                                    copyl[i - kk * l][j + kk * k] = "#"
        for line in lines:
            print(line)
        print("---")
        for line in copyl:
            print(line)
        print(p1)


main()
