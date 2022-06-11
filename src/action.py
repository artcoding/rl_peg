from __future__ import annotations
from src.utils import space_moves
from src.state import State


class Action:

    def __init__(self, state: State, kill: int, move_to: int):
        self.state = state
        self.kill = kill
        self.move_to = move_to

    @classmethod
    def from_int(cls, value: int) -> Action:
        return Action(State(value), -1, -1)

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self) -> int:
        return self.state.value

    def __repr__(self) -> str:
        return f"State.value = {self.state.value}; Kill = {self.kill}; Move_to = {self.move_to}"


def find_moves(state: State) -> {State}:
    space_moves_ = space_moves(state.rows)
    new_states = set()

    for space in range(state.spaces()):
        if state.is_empty(space):
            continue

        for space_move in space_moves_[space]:
            kill, move_to = space_move
            if not state.is_empty(kill) and state.is_empty(move_to):
                new_state = state.copy()
                new_state.clear_space(space)
                new_state.clear_space(kill)
                new_state.set_space(move_to)
                new_states.add(Action(new_state, kill, move_to))

    return new_states
