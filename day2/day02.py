def main():
    with open("input2.txt", "r") as file:
        lines = file.readlines()
        safe_count = 0
        for line in lines:
            print(line.split())
            str_arr = line.split()
            int_arr = []
            for i in range(len(str_arr)):
                int_arr.append(int(str_arr[i]))

            safe = False
            first_chance = issafe(int_arr)
            second_chance = False
            if first_chance:
                safe = True
            else:
                for i in range(len(int_arr)):
                    temp = int_arr.copy()
                    temp.pop(i)
                    sosdfalij = issafe(temp)
                    if sosdfalij:
                        second_chance = True

                    temp = int_arr.copy()

            if second_chance:
                safe = True

            if safe:
                safe_count += 1

        print(safe_count)


def issafe(int_arr):
    print(int_arr)
    safe = True

    if int_arr[0] - int_arr[1] < 0:
        is_descending = False
    else:
        is_descending = True

    for i in range(len(int_arr) - 1):
        diff = int_arr[i] - int_arr[i + 1]
        if is_descending and diff <= 3 and diff > 0:
            print("proceed")

        elif not is_descending and diff >= -3 and diff < 0:
            print("proceed")

        else:
            print("unsafe")
            safe = False
    if safe:
        return True
    else:
        return False


main()
