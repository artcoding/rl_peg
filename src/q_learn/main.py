# Entry point for the Q-learning algorithm

from src import State, Action, Qclass, all_actions, apply_action


def reward(state: State):
    return 100 if bin(state.value).count("1") == 0 else 1


def learn(rows: int = 5):

    alpha = 0.1
    lmbda = 0.5
    epsilon = 0.2
    gamma = 1.0

    all_space_moves = all_actions(rows)
    q = Qclass(epsilon, alpha, lmbda)
    n_holes = (1 + rows) * rows // 2

    start_state = State(value=(1 << n_holes) - 2)
    q.add_state(start_state, all_space_moves)

    while True:     # over episodes
        q.reset_eligibility()
        state = start_state
        action = Action(move_from=3, kill=1, move_to=0)

        while True:     # moves in one episode
            new_state = apply_action(action, state)
            q.add_state(new_state, all_space_moves)

            new_action = q.choose_action(new_state)
            q.eligibility[state][action] += 1

            rew = reward(new_state)
            delta = rew + gamma * q(new_state, new_action) - q(state, action)
            q.update(delta)

            state = new_state
            if new_action is None:
                break
            else:
                action = new_action

        if rew == 100:
            break


if __name__ == '__main__':
    learn(rows=5)
