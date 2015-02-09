# -*- coding: utf-8 -*-

from make_picturelogic_rows import make_rows_pool


data = {
    "rows": [[2, 2], [0], [1, 1, 1], [3], [3]],
    "cols": [[1, 1], [2, 1], [3], [2, 1], [1, 1]]
}


def picturelogic_find_answer(data):
    rows_pool = make_rows_pool(data['rows'], len(data['cols']))
    cycle_max = []
    cycles = [0, 0, 0, 0, 0]

    for row_pool in rows_pool:
        cycle_max.append(len(row_pool))

    while True:
        break_flag = 0

        for col_line in range(len(data['cols'])):
            test_col = [0]

            for i in reversed(range(len(data['rows']))):
                if rows_pool[i][cycles[i]][col_line] == 0:
                    if i == len(data['rows']) - 1:
                        pass
                    elif rows_pool[i+1][cycles[i+1]][col_line] == 1:
                        test_col.append(0)
                    elif rows_pool[i][cycles[i]][col_line] == 0:
                        pass
                    else:
                        print("make test col error")
                elif rows_pool[i][cycles[i]][col_line] == 1:
                    test_col[-1] += 1
                else:
                    print("make test col error")
            else:
                if test_col[-1] == 0 and len(test_col) != 0:
                    test_col.pop(-1)

            if test_col == data['cols'][col_line]:
                pass
            else:
                break
        else:
            return cycles

        # if break_flag == 1:
        #     break
        # else:
        cycles = cycle_count(cycles, cycle_max)
        if cycles == -1:
            return -1


def cycle_count(cycles, cycle_max):
    cycles[0] += 1

    for i in range(len(cycles)):
        if cycles[-1] == cycle_max[-1]:
            return -1

        if cycles[i] == cycle_max[i]:
            cycles[i] = 0
            cycles[i+1] += 1

    return cycles
