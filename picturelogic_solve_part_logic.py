# -*- coding: utf-8 -*-
import json


def picturelogic_solve():
    file = open('data.json', 'r')
    data = json.load(file)

    check = logic_data_valid_check(data)
    print(check)


def logic_data_valid_check(data):
    row_len = len(data['cols'])
    col_len = len(data['rows'])
    rows_check = len_check(data['rows'], row_len)
    cols_check = len_check(data['cols'], col_len)

    if rows_check == 0:
        return -1  # row number error
    elif cols_check == 0:
        return 0  # col number error
    else:
        return 1  # no error


def len_check(data, max_len):
    for row in data:
        line_sum = 0
        for i in range(len(row)):
            line_sum += row[i]

        if (line_sum + len(row) - 1) > max_len:
            return 0  # data number error

picturelogic_solve()