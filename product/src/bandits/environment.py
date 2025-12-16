from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol
import random

# interface for a multi-armed bandit environment
class BanditEnv(Protocol):
    # the number of arms
    n_arms: int

    # method to pull the specified arm and return a reward
    def pull(self, arm: int) -> float:

        ...


@dataclass
# a k-armed Bernoulli bandit environment
# it returns either 1 or 0 for each arm dependent on probability
class BernoulliBandit:

    # list of probability of reward for each arm
    probs: list[float]
    seed: int | None = None

    def __post_init__(self) -> None:
        
        # ensure there is at least 2 arms
        if len(self.probs) < 2:
            raise ValueError("Need at least 2 arms.")
        # ensures all probabilities are valid
        if not all(0.0 <= p <= 1.0 for p in self.probs):
            raise ValueError("All probabilities must be in [0, 1].")
        
        # stores number of arms
        self.n_arms = len(self.probs)
        # creates a random number generator
        self._rng = random.Random(self.seed)

    def pull(self, arm: int) -> float:
        
        # checks if arm index is valid
        if arm < 0 or arm >= self.n_arms:
            raise ValueError(f"Invalid arm: {arm}")
        # pulls a random number and returns a Bernoulli reward
        return 1.0 if self._rng.random() < self.probs[arm] else 0.0

    @property
    # returns the highest expected reward of any arm
    def optimal_mean_reward(self) -> float:
        return max(self.probs)
