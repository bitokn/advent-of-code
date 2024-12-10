def main():
    with open("./input9.txt", "r") as file:
        s = file.readline().strip()
        new_s = []
        total_space = 0
        for i in range(0, len(s)):
            space = 0
            size = 0
            if i % 2 == 0:
                size = int(s[i])
                for _ in range(size):
                    new_s.append(i // 2)

            else:
                space = int(s[i])
                for _ in range(space):
                    new_s.append(".")
                    total_space += 1
        printatble = []
        for item in new_s:
            printatble.append(str(item))

        print("".join(printatble))

        sorted_s = []
        k = len(new_s) - 1
        for i in range(len(new_s)):
            if new_s[i] != ".":
                sorted_s.append(new_s[i])
            else:  # if  new_s[i] == ".":
                while True:
                    if new_s[k] != ".":
                        sorted_s.append(new_s[k])
                        k -= 1
                        break
                    k -= 1

        for _ in range(total_space):
            sorted_s.pop()

        sum = 0
        for i, item in enumerate(sorted_s):
            sum += item * i
            sorted_s[i] = str(item)

        print("".join(sorted_s))
        print(sum)


main()
