# -*- coding: utf-8 -*-

from picturelogic_find_answer import picturelogic_find_answer

data = {
    "rows": [[2, 2], [0], [1, 1, 1], [3], [3]],
    "cols": [[1, 1], [2, 1], [3], [2, 1], [1, 1]]
}

answer_cycle = [0, 1, 0, 0, 1]

rows_pool = [
    [[1, 1, 0, 1, 1], [0, 1, 0, 1, 0]],
    [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0]],
    [[1, 0, 1, 0, 1], ],
    [[0, 1, 1, 1, 0]],
    [[0, 1, 1, 1, 1], [0, 1, 1, 1, 0]]
]


def picturelogic_show_answer(data):
    # answer_cycle = picturelogic_find_answer(data)
    # if answer_cycle == -1:
    #     print('no answer')
    # else:
    #     answer_cycle

    for line in range(len(answer_cycle)):
        for dot in rows_pool[line][answer_cycle[line]]:
            # print(dot, end='')
            if dot == 1:
                print('◼︎︎ ', end='')
            else:
                print('◻ ', end='')
        else:
            print('')


picturelogic_show_answer(data)