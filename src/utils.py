# Utility functions

def calc_bit_pos(row: int, pos: int):
    return (1 + row) * row // 2 + pos


def bit_moves(rows: int = 5) -> dict:
    moves = {}

    bit_pos = 0
    for row in range(rows):
        for pos in range(row + 1):
            m_list = []
            if row > 1:
                new_pos = calc_bit_pos(row - 2, pos)
                new_pos_mid = calc_bit_pos(row - 1, pos)
                if pos <= row - 2:
                    m_list.append((new_pos_mid, new_pos))
                if pos > 1:
                    m_list.append((new_pos_mid - 1, new_pos - 2))

            if row < rows - 2:
                new_pos = calc_bit_pos(row + 2, pos)
                new_pos_mid = calc_bit_pos(row + 1, pos)
                m_list.append((new_pos_mid, new_pos))
                m_list.append((new_pos_mid + 1, new_pos + 2))

            moves[bit_pos] = m_list
            bit_pos += 1

    return moves
