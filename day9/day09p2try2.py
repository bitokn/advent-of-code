import copy


def main():
    with open("./input9.txt", "r") as file:
        s = file.readline().strip()
        new_s = []
        total_space = 0
        spaces = []
        sizes = []
        for i in range(0, len(s)):
            space = 0
            size = 0
            if i % 2 == 0:
                size = int(s[i])
                for _ in range(size):
                    new_s.append(i // 2)
                sizes.append((i // 2, s[i]))

            else:
                space = int(s[i])
                for _ in range(space):
                    new_s.append(".")
                    total_space += 1
                    spaces.append(int(s[i]))
        print(s)
        print(sizes, spaces)

        print(new_s)
        og_s = copy.deepcopy(new_s)
        sum = 0
        # k = int(sizes[-1][0])
        lens = len(s)
        k = lens // 2
        i = 0
        flag = 0

        newslen = len(new_s)
        progress = 0
        while i < newslen:
            if flag:
                progress += 1
                print(f"progress {progress} of ~{lens*5}")
                i = 0
                flag = 0
            printable, i, start_end = check_for_space(new_s, i)
            if printable != "":
                # print(printable, start_end)

                while True:
                    # new_var = int(s[k*2])
                    new_var = int(s[k * 2])

                    if new_var <= start_end[1] - start_end[0] + 1 and start_end[
                        0
                    ] < og_s.index(k):
                        if int(s[k * 2]) > 1 and k in new_s:
                            for _ in range(int(s[k * 2]) - 2):
                                del new_s[start_end[0]]
                            new_s[new_s.index(k) : new_s.index(k) + int(s[k * 2])] = [
                                "."
                            ] * int(s[k * 2])
                            new_s[start_end[0] : start_end[1]] = [k] * (int(s[k * 2]))
                        elif k in new_s:
                            new_s[new_s.index(k)] = "."
                            new_s[start_end[0]] = k

                        k -= 1
                        limit = 0
                        # i = 0
                        break
                    if k != 0:
                        k -= 1
                    else:
                        # k = int(sizes[-1][0])
                        k = lens // 2
                        flag = 1
                        break

            else:
                i += 1

    print(new_s)
    sum = 0
    for j, blo in enumerate(new_s):
        if blo != ".":
            sum += int(blo) * j
    print(sum, progress)


def check_for_space(adfsjkl: list, i: int) -> str:
    og_i = i
    spaces_str = ""
    start_end = ()
    if adfsjkl[i] != ".":
        i += 1

    elif adfsjkl[i] == ".":
        for j in range(i + 1, len(adfsjkl)):
            if adfsjkl[i] == adfsjkl[j]:
                continue
            else:
                spaces_str = (
                    f"space from {i} is until {j-1}{adfsjkl[j - 1]} (size {j - i})"
                )
                start_end += (i, j - 1)
                i += j - i
                break
    i += 1
    if spaces_str != "":
        return spaces_str, i - 1, start_end
    else:
        return spaces_str, og_i, start_end


main()
