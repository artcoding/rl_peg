from __future__ import annotations
from src.utils import calc_space, calc_row_pos
from src.state import State


class Action:

    rows = 5

    def __init__(self, move_from: int, kill: int, move_to: int):
        self.move_from = move_from
        self.move_to = move_to
        self.kill = kill

    def __eq__(self, other):
        return self.move_from == other.move_from and self.move_to == other.move_to

    def __hash__(self) -> int:
        return hash((self.move_from, self.move_to))

    def __repr__(self) -> str:
        return f"From space = {self.move_from} to space = {self.move_to}"

    def rotate(self) -> Action:
        """
        Return image of action rotated clockwise.
        """
        args = []
        for space in (self.move_from, self.kill, self.move_to):
            row, pos = calc_row_pos(space)
            new_pos = self.rows - 1 - row
            new_space = calc_space(row=new_pos + pos, pos=new_pos)
            args.append(new_space)
        return Action(*args)

    def mirror(self) -> Action:
        """
        Return image of action reflected in vertical mirror.
        """
        args = []
        for space in (self.move_from, self.kill, self.move_to):
            row, pos = calc_row_pos(space)
            new_space = calc_space(row=row, pos=row - pos)
            args.append(new_space)
        return Action(*args)

    def all_equivalent(self) -> [Action]:
        """
        Return the set of States into which self transforms under all operations.
        """
        mirror = self.mirror()
        rotated = self.rotate()
        rotated_mirror = mirror.rotate()

        res = [self, mirror, rotated, rotated_mirror, rotated.rotate(), rotated_mirror.rotate()]
        return res


def all_actions(rows: int = 5) -> dict:
    """
    For each space of the board calculate possible moves of its pin.

    :param rows:    Number of rows on the board
    :return:        Dict mapping space number to list of tuples: (kill space, move_to space)
    """
    moves = {}

    space = 0
    for row in range(rows):
        for pos in range(row + 1):
            actions = []
            if row > 1:
                new_pos = calc_space(row - 2, pos)
                new_pos_mid = calc_space(row - 1, pos)
                if pos <= row - 2:
                    actions += [Action(move_from=space, kill=new_pos_mid, move_to=new_pos),
                                Action(move_from=space, kill=space + 1, move_to=space + 2)]
                if pos > 1:
                    actions += [Action(move_from=space, kill=new_pos_mid - 1, move_to=new_pos - 2),
                                Action(move_from=space, kill=space - 1, move_to=space - 2)]

            if row < rows - 2:
                new_pos = calc_space(row + 2, pos)
                new_pos_mid = calc_space(row + 1, pos)
                actions += [Action(move_from=space, kill=new_pos_mid, move_to=new_pos),
                            Action(move_from=space, kill=new_pos_mid + 1, move_to=new_pos + 2)]

            moves[space] = actions
            space += 1

    return moves


def find_moves(state: State, space_moves: dict) -> {State}:
    new_states = set()

    for space in range(state.spaces()):
        if state.is_empty(space):
            continue

        for action in space_moves[space]:
            if not state.is_empty(action.kill) and state.is_empty(action.move_to):
                new_state = state.copy()
                new_state.clear_space(space)
                new_state.clear_space(action.kill)
                new_state.set_space(action.move_to)
                new_states.add((action, new_state))

    return new_states
