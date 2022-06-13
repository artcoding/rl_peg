import numpy as np
from src import State, Action


class Qclass:

    def __init__(self, epsilon: float):
        self.eps = epsilon
        self.value = {}
        self.eligibility = {}

    def choose_action(self, state: State) -> Action:
        """
        Epsilon-greedy algorithm to choose next action.

        :param state:   Current state
        :return:        Action to take
        """
        actions = self.value[state]
        m = len(actions)
        eps_m = self.eps / m
        i_max = np.argmax(actions.values())

        rand = np.random.uniform()
        if rand < eps_m * i_max:
            i = int(rand / eps_m)
        elif rand < eps_m * i_max + 1 - self.eps:
            i = i_max
        else:
            i = m - 1 - int((1 - rand) / eps_m)
        return actions[i]

    def add(self, state: State, action: Action, delta: float):
        if state not in self.value:
            self.value[state] = {action: delta}
        elif action not in self.value[state]:
            self.value[state][action] = delta
        else:
            self.value[state][action] += delta
