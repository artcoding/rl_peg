# Entry point for the Q-learning algorithm

from src import State, Qclass, find_moves, space_moves


def learn(rows: int = 5):
    q = Qclass()

    print(space_moves(rows))

    n_holes = (1 + rows) * rows // 2
    current_state = State(value=(1 << n_holes) - 2)

    print(f"current state = {current_state.value}")
    print(f"moves = {find_moves(current_state)}")

    equivs = current_state.all_equivalent()
    print(equivs)

    symmetry_map = {}

    while True:
        if current_state not in symmetry_map:
            all_transforms = current_state.all_equivalent()
            for state in all_transforms:
                symmetry_map[state] = current_state



        break


if __name__ == '__main__':
    learn(rows=5)
