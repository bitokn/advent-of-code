import itertools


def main():
    with open("input7.txt", "r") as file:
        lines = file.readlines()

        p1 = 0
        for line in lines:
            line = line.split(":")
            line[1] = line[1].strip().split()

            possible_ops = ["+", "*"]
            iterlist = [
                x
                for x in itertools.product(["*", "+", "||"], repeat=(len(line[1]) - 1))
            ]
            print(line)
            # print(len(iterlist))

            for j in iterlist:
                line_result = int(line[1][0])
                ## line_str = f"{line[1][0]}"
                line_str = line[1][0]
                for i in range(1, len(line[1])):
                    op_chosen = j[i % (len(line[1]) - 1)]
                    # if j[i % (len(line[1]) - 1)]:
                    #     op_chosen = possible_ops[0]
                    # else:
                    #     op_chosen = possible_ops[1]
                    if op_chosen == "+":
                        line_result = line_result + int(line[1][i])
                        line_str += f"+{line[1][i]}"

                    elif op_chosen == "*":
                        line_result = line_result * int(line[1][i])
                        line_str += f"*{line[1][i]}"
                    ## line_str += f"{line[1][i]}"
                    elif op_chosen == "||":
                        line_result = int(f"{line_result}{line[1][i]}")
                        line_str += f"||{line[1][i]}"

                if line_result == int(line[0]):
                    p1 += line_result
                    # break
                print(f"{line_str} = {line_result}")

        print("\n", p1)


main()
