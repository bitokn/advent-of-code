def main():
    s = "2333133121414131402"

    constructed_s = []
    i = 0
    k = len(s) - 1
    while i < len(s):

        if i % 2 != 0:  # even elements
            for dd in range(len(s) - 1, -1, -1):
                if int(s[i]) <= int(s[dd]):
                    last_id = (len(s) - 1) // 2
                    for _ in range(int(s[dd])):
                        constructed_s.append(last_id)
                    for _ in range(int(s[i]) - int(s[dd])):
                        constructed_s.append(".")

                    s = s[:dd] + "0" + s[dd + 1 :]
                    break

            else:
                for _ in range(int(s[i])):
                    constructed_s.append(".")
        else:
            for _ in range(int(s[i])):
                constructed_s.append(i // 2)
        i += 1

    print(constructed_s)


main()
