import math
from itertools import combinations


def main():
    with open("./2023day12input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line)
            alt_code = []
            main_code = []
            for i, thing in enumerate(line):
                if thing in ["#", ".", "?"]:
                    main_code.append(thing)
                    # print(f"{i} {thing}")
                elif thing not in ["\n", ",", " "]:
                    # is_spring = False
                    alt_code.append(int(thing))
            print(main_code)
            print(alt_code)

            print(does_match(main_code, alt_code))
            print(main_code.count("?"))

            true_count = 0

            # create new arrays to test
            hashes_left = main_code.count("?") - (sum(alt_code) - main_code.count("#"))

            # print(create_new_try(main_code, hashes_left))

            # initialize a list
            my_list = [1, 2, 3, 1, 5, 4]
            item = "?"

            indices = [i for i in range(len(main_code)) if main_code[i] == item]

            print(indices)

            # for i, qpos in enum(indicies);

            for i, qpos in enumerate(indices):
                print(create_new_try(main_code.copy(), qpos))
            print("---")


def does_match(main_code, alt_code):
    consecutive = False
    con_count = 0
    con_arr = []
    for i in range(len(main_code)):
        if main_code[i] == "#":
            consecutive = True
            con_count += 1
        else:
            consecutive = False
            if con_count:
                print(con_count)
                con_arr.append(con_count)
            con_count = 0
    if con_count:
        con_arr.append(con_count)
        print(con_count)
    print(con_arr)
    return con_arr == alt_code


def create_new_try(array_to_be_swapped, n):

    for i in range(len(array_to_be_swapped)):
        if array_to_be_swapped[i] == "?" and i != n:
            array_to_be_swapped[i] = "#"

        elif array_to_be_swapped[i] == "?" and i == n:
            array_to_be_swapped[i] = "."

    return array_to_be_swapped

    # replaces n ? with n # starting at i


main()
