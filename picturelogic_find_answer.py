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
        print(cycles)
        cycles = cycle_count(cycles, cycle_max)
        if cycles == -1:
            print("End cycles, no answer.")
            break


def cycle_count(cycles, cycle_max):
    cycles[0] += 1

    for i in range(len(cycles)):
        if cycles[-1] == cycle_max[-1]:
            return -1

        if cycles[i] == cycle_max[i]:
            cycles[i] = 0
            cycles[i+1] += 1
            # print(cycles)

    return cycles




picturelogic_find_answer(data)
