#
from __future__ import annotations
from copy import copy


class State:
    def __init__(self, value: int, rows: int):
        self.value = value
        self.rows = rows

        self.mirror_map = {}
        # for row in range(1, rows):
        #     for pos in

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, State):
            return self.value == other.value and self.rows == self.rows
        return False

    # This function swaps bit at positions p1 and p2 in an integer n
    def swap_bits(self, p1: int, p2: int):

        # Move p1'th to rightmost side
        bit1 = (self.value >> p1) & 1

        # Move p2'th to rightmost side
        bit2 = (self.value >> p2) & 1

        if bit1 == bit2:
            return

        # XOR the two bits
        x = (bit1 ^ bit2)

        # Put the xor bit back to their original positions
        x = (x << p1) | (x << p2)

        # XOR 'x' with the original number so that the
        # two sets are swapped
        self.value = self.value ^ x

    def rotate(self) -> State:
        return self

    def mirror(self) -> State:
        other = copy(self)
        for row in range(1, self.rows):
            start = (1 + row) * row // 2
            count = row // 2 + 1
            for c in range(count):
                # switch bits in positions pos and stop - pos
                other.swap_bits(start + c, start + count - c)

        return other
