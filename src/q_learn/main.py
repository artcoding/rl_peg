# Entry point for the Q-learning algorithm

from src import State, find_moves
from src import space_moves


def learn(rows: int = 5):
    states = {}

    print(space_moves(rows))

    n_holes = (1 + rows) * rows // 2
    current_state = State(value=(1 << n_holes) - 2 - (1 << 3), rows=rows)

    print(f"current state = {current_state.value}")
    print(f"moves = {find_moves(current_state)}")
    print(f"new states = {[bin(s.value) for s in find_moves(current_state)]}")

    equivs = current_state.all_equivalent()
    print(equivs)


if __name__ == '__main__':
    learn(rows=5)
