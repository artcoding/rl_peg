#
from src import State


def find_moves(state: State) -> {State}:
    pass


def learn(rows: int = 5):
    states = {}

    n_holes = (1 + rows) * rows // 2
    current_state = State(value=(1 << n_holes) - 2 - (1 << 3), rows=rows)

    print(current_state)

    equivs = current_state.all_equivalent()
    print(equivs)


if __name__ == '__main__':
    learn(rows=5)
