#
from __future__ import annotations
from copy import copy


class State:
    def __init__(self, value: int, rows: int=5):
        self.value = value
        self.rows = rows

    def from_value(self, value: int) -> State:
        return State(value=value, rows=self.rows)

    def __eq__(self, other: State) -> bool:
        """Overrides the default implementation"""
        if isinstance(other, State):
            return self.value == other.value and self.rows == self.rows
        return False

    def __hash__(self) -> bool:
        return self.value

    def __repr__(self):
        return f"value = {self.value}; rows = {self.rows}"

    def swap_bits(self, p1: int, p2: int) -> None:
        """
        Swap bits at positions p1 and p2 in self.value
        """

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
        """
        Return image of state rotated clockwise\.
        """
        rotated = self.from_value(0)

        bit_pos = 0
        for row in range(self.rows):
            # position in rows after rotation
            new_row_pos = self.rows - 1 - row

            for new_row in range(self.rows - 1 - row, self.rows):
                # bit position in rotated value
                new_bit_pos = (1 + new_row) * new_row // 2 + new_row_pos

                # Read bit from bit_pos in self.value
                bit = self.value & (1 << bit_pos)
                # Insert bit to new_bit_pos in rotated.value
                if bit != 0:
                    rotated.value = rotated.value | (1 << new_bit_pos)
                bit_pos += 1

        return rotated

    def mirror(self) -> State:
        """
        Return image of state reflected in vertical mirror.
        """
        other = copy(self)
        for row in range(1, self.rows):
            start = (1 + row) * row // 2
            count = row // 2 + 1
            for c in range(count):
                # switch bits in positions pos and stop - pos
                other.swap_bits(start + c, start + count - c)

        return other

    def all_equivalent(self) -> {State}:
        """
        Return the set of States into which self transforms under all operations.
        """
        mirror = self.mirror()
        rotated = self.rotate()
        rotated_mirror = mirror.rotate()

        res = {self, mirror, rotated, rotated_mirror, rotated.rotate(), rotated_mirror.rotate()}
        return res
