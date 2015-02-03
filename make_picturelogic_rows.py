# -*- coding: utf-8 -*-

from itertools import combinations

data = {
  "rows": [[2, 2], [0], [1, 1, 1], [3], [3]],
  "cols": [[1, 1], [2, 1], [3], [2, 1], [1, 1]]
}


def make_rows_combinations(rows, row_len):
    for row in rows:
        row_combination_pool = []
        row_sum = 0

        for num in row:
            row_sum += num

        if row_sum == 0:
            row_combination_pool.append(tuple(range(1)))
        else:
            for row_combinations in combinations(range(row_len-row_sum+1), len(row)):
                row_combination_pool.append(row_combinations)

        yield row_combination_pool


def make_rows_pool(rows, row_len):
    row_line_num = 0
    for row_combinations in make_rows_combinations(rows, row_len):
        row_sum = 0
        row_pool = []

        for num in rows[row_line_num]:
                row_sum += num

        for row_combination in row_combinations:
            row = []

            for append_zeros in range(row_len - row_sum):
                row.append(0)

            times_index = 0
            for location_index in reversed(row_combination):
                for insert_ones in range(list(reversed(rows[row_line_num]))[times_index]):
                    row.insert(location_index, 1)

                times_index += 1

            row_pool.append(row)

        yield row_pool
        row_line_num += 1


for i in make_rows_pool(data['rows'], len(data['cols'])):
    print(i)