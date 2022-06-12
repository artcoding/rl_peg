# Utility functions
from math import sqrt


def calc_space(row: int, pos: int) -> int:
    """
    Calculate space index from row number and position in the row.
    """
    return (1 + row) * row // 2 + pos


def calc_row_pos(space: int) -> (int, int):
    """
    Calculate space row and position from its index
    :return:    tuple (row, pos)
    """

    row = int(sqrt(2 * space + 0.25) - 0.5)
    pos = space - calc_space(row, 0)

    # fix potential rounding errors
    if pos < 0:
        row -= 1
        pos = row
    if pos > row:
        row += 1
        pos = 0

    return row, pos
