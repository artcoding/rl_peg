from src import State, Action


class Qclass:

    def __init__(self):
        self.Q = {}

        pass

    def add(self, state: State, action: Action, delta: float):
        if state not in self.Q:
            self.Q[state] = {action: delta}
        elif action not in self.Q[state]:
            self.Q[state][action] = delta
        else:
            self.Q[state][action] += delta
