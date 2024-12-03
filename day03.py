def main():
    with open("input3.txt", "r") as file:
        line = file.read()
        print(line)
        sum = 0
        str_nums = ["0","1","2","3","4","5","6","7","8","9"]
        switch_on = True

        for i in range(len(line)):
            if line[i : i + 4] == "mul(":
                print("we proceed")
                j = 0
                string = "0"
                not_comma = 1
                cancel = False
                while not_comma:
                    if line[i + j + 4] == ",":
                        not_comma = False
                    elif line[i + j + 4] not in str_nums:
                        string = "0"
                        string2 = "0"
                        cancel = True
                        not_comma = 0
                    else:
                        string = string + line[i + j + 4]
                    j += 1

                print("string1", int(string))
                k = 0
                string2 = "0"
                not_endparen = 1
                while not_endparen:
                    if line[i + j + k + 4] == ")":
                        not_endparen = 0
                    elif line[i + k + j + 4] not in str_nums:
                        string = "0"
                        string2 = "0"
                        cancel = True
                        not_endparen = 0
                    else:
                        string2 = string2 + line[i + j + k + 4]
                    k += 1

                if not cancel and switch_on:
                    print("string2", int(string2))
                    product = int(string) * int(string2)
                    print(f"{string}*{string2} = {product}")
                    sum += product

            elif line[i : i + 4] == "do()":
                switch_on = True
            elif line[i : i + 7] == "don't()":
                switch_on = False
        print(sum)


main()
