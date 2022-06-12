from .context import src


def test_calc_space():
    assert src.calc_space(0, 0) == 0
    assert src.calc_space(4, 3) == 13
    assert src.calc_space(3, 3) == 9
    assert src.calc_space(4, 0) == 10


def test_calc_row_pos():
    assert src.calc_row_pos(0) == (0, 0)
    assert src.calc_row_pos(13) == (4, 3)
    assert src.calc_row_pos(9) == (3, 3)
    assert src.calc_row_pos(10) == (4, 0)

    row, pos = 23, 18
    assert src.calc_row_pos(src.calc_space(row, pos)) == (row, pos)
