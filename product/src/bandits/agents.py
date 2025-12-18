from __future__ import annotations

from dataclasses import dataclass
import random
import math


# random baseline agent
# selects an arm at random every step
# does not learn between steps
@dataclass
class RandomAgent:

    # number of available arms
    n_arms: int
    seed: int | None = None

    def __post_init__(self) -> None:
        # ensure there are at least 2 arms
        if self.n_arms < 2:
            raise ValueError("Need at least 2 arms.")

        # random number generator
        self._rng = random.Random(self.seed)

    def select_arm(self) -> int:
        # chooses an arm randomly
        return self._rng.randrange(self.n_arms)

    def update(self, arm: int, reward: float) -> None:
        # random agent does not learn so no update needed
        pass

# ucb1 agent
# balances exploration and exploitation using an upper confidence bound
@dataclass
class UCB1Agent:

    # number of available arms
    n_arms: int
    # exploration constant
    # higher the constant, higher the exploration
    c: float = 1.0

    def __post_init__(self) -> None:
        # ensure there are at least 2 arms
        if self.n_arms < 2:
            raise ValueError("Need at least 2 arms.")
        # ensure constant is valid
        if self.c <= 0:
            raise ValueError("c must be > 0")

        # how many times each arm has been selected
        self.counts = [0] * self.n_arms
        # estimated mean reward for each arm
        self.values = [0.0] * self.n_arms

    def select_arm(self) -> int:
        # ensure each arm is tried at least once
        for i in range(self.n_arms):
            if self.counts[i] == 0:
                return i

        # total pulls so far
        total_pulls = sum(self.counts)
        log_t = math.log(total_pulls)

        # compute ucb score for each arm and choose the best
        best_arm = 0
        best_score = float("-inf")

        for i in range(self.n_arms):
            mean = self.values[i]
            bonus = self.c * math.sqrt((2.0 * log_t) / self.counts[i])
            score = mean + bonus

            if score > best_score:
                best_score = score
                best_arm = i

        return best_arm

    def update(self, arm: int, reward: float) -> None:
        # update pull count
        self.counts[arm] += 1
        n = self.counts[arm]

        # incremental mean update for the selected arm
        # updates the average without storing all past rewards
        self.values[arm] += (reward - self.values[arm]) / n


# epsilon greedy agent
# best estimated arm is used most of the time
# epsilon probability cause it to explore other arms
@dataclass
class EpsilonGreedyAgent:

    # number of available arms
    n_arms: int
    # epsilon probability
    # rate that it explores
    epsilon: float = 0.1
    seed: int | None = None

    def __post_init__(self) -> None:
        # ensure there are at least 2 arms
        if self.n_arms < 2:
            raise ValueError("Need at least 2 arms.")
        # ensure epsilon value is valid
        if not (0.0 <= self.epsilon <= 1.0):
            raise ValueError("epsilon must be in [0, 1]")

        # how many times each arm has been selected
        self.counts = [0] * self.n_arms
        # estimates the mean reward for each arm
        self.values = [0.0] * self.n_arms

        # random number generator 
        self._rng = random.Random(self.seed)

    def select_arm(self) -> int:
        # checks whether the agent should explore
        if self._rng.random() < self.epsilon:
            return self._rng.randrange(self.n_arms)

        # otherwise chooses the best know arm
        # if it is equal, a random choice is made between the possible arms
        best_value = max(self.values)
        best_arms = [i for i, v in enumerate(self.values) if v == best_value]
        return self._rng.choice(best_arms)

    def update(self, arm: int, reward: float) -> None:
        # update pull count
        self.counts[arm] += 1
        n = self.counts[arm]

        # updates the mean for the selected arm
        self.values[arm] += (reward - self.values[arm]) / n