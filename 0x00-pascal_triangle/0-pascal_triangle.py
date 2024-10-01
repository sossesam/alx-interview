#!/usr/bin/python3

"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Class defined as Queen to solve nQueens problem
    using recursion
    """
    column = []
    if n <= 0:
        return [[]]
    else:
        for i in range(n):

            row = []
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
