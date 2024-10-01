#!/usr/bin/python3
"""
 0-main
"""


def pascal_triangle(n):
    """
    0-main
    """

    column = []
    if n == 0:
        return [[]]
    else:
        for i in range(n):

            row = []
            count = 0
            last_num = 0
            if i == 0:
                row.append(1)
                column.append(row)
                continue
            for x in column[i - 1]:
                num = x + last_num
                last_num = x
                row.append(num)

            row.append(last_num)
            column.append(row)
        return column
