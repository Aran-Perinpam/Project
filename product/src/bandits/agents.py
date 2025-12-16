from __future__ import annotations

from dataclasses import dataclass
import random


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
