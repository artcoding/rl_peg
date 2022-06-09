# Utility functions

def calc_space(row: int, pos: int) -> int:
    """
    Calculate space index from row number and position in the row.
    """
    return (1 + row) * row // 2 + pos


def space_moves(rows: int = 5) -> dict:
    """
    For each space of the board calculate possible moves of its pin.

    :param rows:    Number of rows on the board
    :return:        Dict mapping space number to list of tuples: (kill space, move_to space)
    """
    moves = {}

    space = 0
    for row in range(rows):
        for pos in range(row + 1):
            m_list = []
            if row > 1:
                new_pos = calc_space(row - 2, pos)
                new_pos_mid = calc_space(row - 1, pos)
                if pos <= row - 2:
                    m_list += [(new_pos_mid, new_pos), (space + 1, space + 2)]
                if pos > 1:
                    m_list += [(new_pos_mid - 1, new_pos - 2), (space - 1, space - 2)]

            if row < rows - 2:
                new_pos = calc_space(row + 2, pos)
                new_pos_mid = calc_space(row + 1, pos)
                m_list += [(new_pos_mid, new_pos), (new_pos_mid + 1, new_pos + 2)]

            moves[space] = m_list
            space += 1

    return moves
