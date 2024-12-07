from copy import deepcopy


def main():
    with open("input6.txt", "r") as file:
        lines = file.readlines()
        guard_pos = []
        guard_dir = "u"
        in_bounds = True
        for i, line in enumerate(lines):
            lines[i] = line.strip()
            if line.find("^") != -1:
                guard_x = line.find("^")
                # print(f"^ found at row {i} column {guard_x}")
                starting_pos = (guard_x, i)
        # print(lines, guard_pos)
        # starting_pos = guard_pos
        grid = []
        for line in lines:
            grid += [list(line)]
        # print(grid)
        # while in_bounds:
        #     if guard_dir == "u":
        #         if guard_pos[1] < len(grid) - 1 and guard_pos[0] < len(grid[0]) - 1:
        #             if grid[guard_pos[1] - 1][guard_pos[0]] == "#":
        #                 #print("thing above")
        #                 grid[guard_pos[1]][guard_pos[0]] = "+"
        #                 guard_dir = "r"
        #                 guard_pos = guard_pos[0] + 1
        #             else:
        #                 if grid[guard_pos[1]][guard_pos[0]] == "-":
        #                     grid[guard_pos[1]][guard_pos[0]] = "+"
        #                 else:
        #                     grid[guard_pos[1]][guard_pos[0]] = "|"
        #                 guard_pos[1] -= 1
        #         else:
        #             grid[guard_pos[1]][guard_pos[0]] = "^"
        #             in_bounds = False
        #     if guard_dir == "r":
        #         if guard_pos[1] < len(grid) - 1 and guard_pos[0] < len(grid[0]) - 1:
        #             if grid[guard_pos[1]][guard_pos[0] + 1] == "#":
        #                 #print("thing to the right")
        #                 grid[guard_pos[1]][guard_pos[0]] = "+"
        #                 guard_dir = "d"
        #                 guard_pos = guard_pos[1] + 1
        #             else:
        #                 if grid[guard_pos[1]][guard_pos[0]] == "|":
        #                     grid[guard_pos[1]][guard_pos[0]] = "+"
        #                 else:
        #                     grid[guard_pos[1]][guard_pos[0]] = "-"
        #                 guard_pos = guard_pos[0] + 1
        #         else:
        #             grid[guard_pos[1]][guard_pos[0]] = ">"
        #             in_bounds = False

        #     if guard_dir == "d":
        #         if guard_pos[1] < len(grid) - 1 and guard_pos[0] < len(grid[0]) - 1:
        #             if grid[guard_pos[1] + 1][guard_pos[0]] == "#":
        #                 #print("thing below")
        #                 grid[guard_pos[1]][guard_pos[0]] = "+"
        #                 guard_dir = "l"
        #                 guard_pos = guard_pos[0] - 1
        #             else:
        #                 if grid[guard_pos[1]][guard_pos[0]] == "-":
        #                     grid[guard_pos[1]][guard_pos[0]] = "+"
        #                 else:
        #                     grid[guard_pos[1]][guard_pos[0]] = "|"
        #                 guard_pos = guard_pos[1] + 1
        #         else:
        #             grid[guard_pos[1]][guard_pos[0]] = "v"
        #             in_bounds = False
        #     if guard_dir == "l":
        #         if guard_pos[1] < len(grid) - 1 and guard_pos[0] < len(grid[0]) - 1:
        #             if grid[guard_pos[1]][guard_pos[0] - 1] == "#":
        #                 #print("thing to the left")
        #                 grid[guard_pos[1]][guard_pos[0]] = "+"
        #                 guard_dir = "u"
        #                 guard_pos[1] -= 1
        #             else:
        #                 if grid[guard_pos[1]][guard_pos[0]] == "|":
        #                     grid[guard_pos[1]][guard_pos[0]] = "+"
        #                 else:
        #                     grid[guard_pos[1]][guard_pos[0]] = "-"
        #                 guard_pos = guard_pos[0] - 1
        #         else:
        #             grid[guard_pos[1]][guard_pos[0]] = "<"
        #             in_bounds = False

        # print(grid)
        p1 = 0
        for i in grid:
            p1 += i.count("X")

        coolbool = place_obstruction(1, 8, grid, starting_pos)

        p2 = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # print(f"obstruction at {i} {j}")
                # #print(grid)
                if (j, i) != starting_pos:
                    print(f"placing obstruct at {j} {i}")
                    coolbool = place_obstruction(i, j, grid, starting_pos)

                # #print(grid)
                if coolbool:
                    p2 += 1
                    print(f"infinite loop at obstruction loc {j} {i}")
        print(starting_pos)
        print(p1, p2)

        # #print(lines)
        # print(guard_pos)


def place_obstruction(i, j, grid, initial_pos):
    new_grid = deepcopy(grid)
    new_grid[i][j] = "#"
    guard_pos = initial_pos
    # print(new_grid)
    guard_dir = "u"
    # sum = 0
    in_bounds = True
    past_positions = set()

    while in_bounds:

        if guard_dir == "u":
            if (
                guard_pos[1] > 0
                and guard_pos[1] < len(new_grid) - 1
                and guard_pos[0] > 0
                and guard_pos[0] < len(new_grid[0]) - 1
            ):
                if new_grid[guard_pos[1] - 1][guard_pos[0]] == "#":
                    # print("thing above")
                    # new_grid[guard_pos[1]][guard_pos[0]] = "+"
                    past_positions.add(((guard_pos[0], guard_pos[1]), guard_dir))
                    guard_dir = "r"
                    # guard_pos = guard_pos[0] + 1
                else:
                    # if new_grid[guard_pos[1]][guard_pos[0]] == "-":
                    #     #new_grid[guard_pos[1]][guard_pos[0]] = "+"
                    #     pass
                    # else:
                    #     new_grid[guard_pos[1]][guard_pos[0]] = "|"
                    past_positions.add(((guard_pos[0], guard_pos[1]), guard_dir))
                    guard_pos = (guard_pos[0], guard_pos[1] - 1)
            else:
                # new_grid[guard_pos[1]][guard_pos[0]] = "^"
                in_bounds = False
        if guard_dir == "r":
            if (
                guard_pos[1] > 0
                and guard_pos[1] < len(new_grid) - 1
                and guard_pos[0] > 0
                and guard_pos[0] < len(new_grid[0]) - 1
            ):
                if new_grid[guard_pos[1]][guard_pos[0] + 1] == "#":
                    # print("thing to the right")
                    # new_grid[guard_pos[1]][guard_pos[0]] = "+"
                    past_positions.add(((guard_pos[0], guard_pos[1]), guard_dir))
                    guard_dir = "d"
                    # guard_pos = guard_pos[1] + 1
                else:
                    # if new_grid[guard_pos[1]][guard_pos[0]] == "|":
                    #     new_grid[guard_pos[1]][guard_pos[0]] = "+"
                    # else:
                    #     new_grid[guard_pos[1]][guard_pos[0]] = "-"
                    past_positions.add(((guard_pos[0], guard_pos[1]), guard_dir))
                    guard_pos = (guard_pos[0] + 1, guard_pos[1])
            else:
                # new_grid[guard_pos[1]][guard_pos[0]] = ">"
                in_bounds = False

        if guard_dir == "d":
            if (
                guard_pos[1] > 0
                and guard_pos[1] < len(new_grid) - 1
                and guard_pos[0] > 0
                and guard_pos[0] < len(new_grid[0]) - 1
            ):
                if new_grid[guard_pos[1] + 1][guard_pos[0]] == "#":
                    # print("thing below")
                    # new_grid[guard_pos[1]][guard_pos[0]] = "+"
                    past_positions.add(((guard_pos[0], guard_pos[1]), guard_dir))
                    guard_dir = "l"
                    # guard_pos = guard_pos[0] - 1
                else:
                    # if new_grid[guard_pos[1]][guard_pos[0]] == "-":
                    #     new_grid[guard_pos[1]][guard_pos[0]] = "+"
                    # else:
                    #     new_grid[guard_pos[1]][guard_pos[0]] = "|"
                    past_positions.add(((guard_pos[0], guard_pos[1]), guard_dir))
                    guard_pos = (guard_pos[0], guard_pos[1] + 1)
            else:
                # new_grid[guard_pos[1]][guard_pos[0]] = "v"
                in_bounds = False
        if guard_dir == "l":
            if (
                guard_pos[1] > 0
                and guard_pos[1] < len(new_grid) - 1
                and guard_pos[0] > 0
                and guard_pos[0] < len(new_grid[0]) - 1
            ):
                if new_grid[guard_pos[1]][guard_pos[0] - 1] == "#":
                    # print("thing to the left")
                    # new_grid[guard_pos[1]][guard_pos[0]] = "+"
                    past_positions.add(((guard_pos[0], guard_pos[1]), guard_dir))
                    guard_dir = "u"
                    # guard_pos[1] -= 1
                else:
                    # if new_grid[guard_pos[1]][guard_pos[0]] == "|":
                    #     new_grid[guard_pos[1]][guard_pos[0]] = "+"
                    # else:
                    #     new_grid[guard_pos[1]][guard_pos[0]] = "-"
                    past_positions.add(((guard_pos[0], guard_pos[1]), guard_dir))
                    guard_pos = (guard_pos[0] - 1, guard_pos[1])
            else:
                # new_grid[guard_pos[1]][guard_pos[0]] = "<"
                in_bounds = False
        # #print(sum)
        # print(past_positions)
        # print(guard_pos, guard_dir)
        if (guard_pos, guard_dir) in past_positions:
            return True

    # print(sum)
    return False


main()
