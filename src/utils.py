# Utility functions

def calc_space(row: int, pos: int) -> int:
    """
    Calculate space index from row number and position in the row.
    """
    return (1 + row) * row // 2 + pos
