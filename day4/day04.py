def main():
    with open("input4.txt", "r") as file:
        lines = file.readlines()
        # print(line)
        sum = 0
        width = len(lines[0]) - 1
        height = len(lines)
        print(height)
        print(width)
        for i in range(len(lines)):  # rows
            for j in range(len(lines[0])):  # cols
                if i <= width - 3 and j <= height - 3:
                    if (
                        lines[i][j] == "M"
                        and lines[i][j + 2] == "M"
                        and lines[i + 1][j + 1] == "A"
                        and lines[i + 2][j + 2] == "S"
                        and lines[i + 2][j] == "S"
                    ):
                        sum += 1
                        print(f"cross MAS found {i} {j}, sum: {sum}")

                    if (
                        lines[i][j] == "M"
                        and lines[i][j + 2] == "S"
                        and lines[i + 1][j + 1] == "A"
                        and lines[i + 2][j + 2] == "S"
                        and lines[i + 2][j] == "M"
                    ):
                        sum += 1
                        print(f"cross MAS found {i} {j}, sum: {sum}")

                    if (
                        lines[i][j] == "S"
                        and lines[i][j + 2] == "S"
                        and lines[i + 1][j + 1] == "A"
                        and lines[i + 2][j + 2] == "M"
                        and lines[i + 2][j] == "M"
                    ):
                        sum += 1
                        print(f"cross MAS found {i} {j}, sum: {sum}")

                    if (
                        lines[i][j] == "S"
                        and lines[i][j + 2] == "M"
                        and lines[i + 1][j + 1] == "A"
                        and lines[i + 2][j + 2] == "M"
                        and lines[i + 2][j] == "S"
                    ):
                        sum += 1
                        print(f"cross MAS found {i} {j}, sum: {sum}")

                # if lines[i][j : j + 4] == "XMAS" or lines[i][j : j + 4] == "SAMX":
                #     sum += 1
                #     print(f"found h at {i} {j}, sum {sum}")
                # if i <= width - 4:
                #     if (
                #         lines[i][j] == "S"
                #         and lines[i + 1][j] == "A"
                #         and lines[i + 2][j] == "M"
                #         and lines[i + 3][j] == "X"
                #     ):
                #         sum += 1
                #         print(f"found v samx at {i} {j}, sum {sum}")

                # if i <= width - 4:
                #     if (
                #         lines[i][j] == "X"
                #         and lines[i + 1][j] == "M"
                #         and lines[i + 2][j] == "A"
                #         and lines[i + 3][j] == "S"
                #     ):
                #         sum += 1
                #         print(f"found v xmas at {i} {j}, sum {sum}")

                # if i <= width - 4 and j <= height - 4:
                #     if (
                #         lines[i][j] == "S"
                #         and lines[i + 1][j + 1] == "A"
                #         and lines[i + 2][j + 2] == "M"
                #         and lines[i + 3][j + 3] == "X"
                #     ):
                #         sum += 1
                #         print(f"found diag r xmas at {i} {j}, sum {sum}")

                # if i <= width - 4 and j <= height - 4:
                #     if (
                #         lines[i][j] == "X"
                #         and lines[i + 1][j + 1] == "M"
                #         and lines[i + 2][j + 2] == "A"
                #         and lines[i + 3][j + 3] == "S"
                #     ):
                #         sum += 1
                #         print(f"found diag r samx at {i} {j}, sum {sum}")

                # if i <= width - 4:
                #     if (
                #         lines[i][j] == "S"
                #         and lines[i + 1][j - 1] == "A"
                #         and lines[i + 2][j - 2] == "M"
                #         and lines[i + 3][j - 3] == "X"
                #     ):
                #         sum += 1
                #         print(f"found diag l samx at {i} {j}, sum {sum}")

                # if i <= width - 4:
                #     if (
                #         lines[i][j] == "X"
                #         and lines[i + 1][j - 1] == "M"
                #         and lines[i + 2][j - 2] == "A"
                #         and lines[i + 3][j - 3] == "S"
                #     ):
                #         sum += 1
                #         print(f"found diag l xmas at {i} {j}, sum {sum}")


main()
