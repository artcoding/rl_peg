import numpy as np
from src import State, Action, find_moves
from typing import Optional


class Qclass:

    def __init__(self, eps: float, alpha: float, lmbda: float):
        self.eps = eps
        self.alpha = alpha
        self.lmbda = lmbda

        self.value = {}
        self.eligibility = {}

    def choose_action(self, state: State) -> Optional[Action]:
        """
        Epsilon-greedy algorithm to choose next action.

        :param state:   Current state
        :return:        Action to take
        """
        actions = self.value[state]
        m = len(actions)
        if m == 0:
            return None
        eps_m = self.eps / m
        val = np.fromiter(actions.values(), dtype=float)
        i_max = np.argmax(val)

        # print(f"max Q = {np.max(val)}")

        rand = np.random.uniform()
        if rand < eps_m * (i_max - 1):
            i = int(rand / eps_m)
        elif rand < eps_m * i_max + 1 - self.eps:
            i = i_max
        else:
            i = m - 1 - int((1 - rand) / eps_m)
        return list(actions)[i]

    def reset_eligibility(self):
        for state, actions in self.eligibility.items():
            for action in actions:
                self.eligibility[state][action] = 0

    def add_state(self, state: State, all_space_moves):
        if state not in self.value:
            moves = find_moves(state, all_space_moves)
            self.value[state] = {act: 0.0 for (act, st) in moves}
            self.eligibility[state] = {act: 0.0 for (act, st) in moves}

    def update(self, delta: float):
        for state, actions in self.value.items():
            for action in actions:
                self.value[state][action] += self.alpha * delta * self.eligibility[state][action]
                self.eligibility[state][action] *= self.lmbda

    def __call__(self, state, action):
        if action is None:
            return 0
        return self.value[state][action]
