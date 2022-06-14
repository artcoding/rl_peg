# Entry point for the Q-learning algorithm

from math import exp
import numpy as np
import matplotlib.pyplot as plt

import src
from src import State, Action, Qclass, all_actions, apply_action


def reward(state: State):
    return 10 if bin(state.value).count("1") == 1 else 0


def learn(rows: int = 5):

    src.State.rows = rows
    src.Action.rows = rows

    alpha = 0.9
    lmbda = 0.5

    epsilon = 1.0
    eps_decay = 500
    # eps_decay = 2000

    gamma = 1.0
    n_episodes = 1000

    all_space_moves = all_actions(rows)
    q = Qclass(epsilon, alpha, lmbda)
    n_holes = (1 + rows) * rows // 2

    start_state = State(value=(1 << n_holes) - 2 - (1 << 17))
    q.add_state(start_state, all_space_moves)

    episode = 0
    total_rew = []
    epsilons = []
    while True:     # over episodes
        eps = exp(-0.5 * episode * episode / eps_decay / eps_decay)
        q.eps = eps
        epsilons.append(eps)
        q.reset_eligibility()
        state = start_state
        action = Action(move_from=3, kill=1, move_to=0)

        total_reward = 0.0

        while True:     # moves in one episode
            new_state = apply_action(action, state)
            q.add_state(new_state, all_space_moves)

            new_action = q.choose_action(new_state)
            # print(new_action)
            q.eligibility[state][action] += 1

            rew = reward(new_state)
            total_reward += rew
            delta = rew + gamma * q(new_state, new_action) - q(state, action)
            q.update(delta)

            state = new_state
            if new_action is None:
                break
            else:
                action = new_action

        print(f"Episode = {episode}, total reward = {total_reward}, state = {state}")
        episode += 1
        total_rew.append(total_reward)
        if episode == n_episodes:
            return total_rew, epsilons


if __name__ == '__main__':
    rev, eps = np.array(learn(rows=6))
    window = 50
    means = np.zeros(len(rev) - window + 1)
    for i in range(len(means)):
        means[i] = rev[i: i + window].sum() / window

    # plt.figure()
    f, (ax1, ax2) = plt.subplots(2, 1)
    ax1.plot(rev)
    ax1.plot(means)
    # plt.show()

    # plt.figure()
    ax2.plot(eps)
    # plt.plot(means)
    plt.show()

