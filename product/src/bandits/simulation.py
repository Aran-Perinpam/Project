from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from .environment import BanditEnv

# interface for any bandit-solving agent
# any agent must be able to choose an arm and update based on the reward
class Agent(Protocol):
    # choose what arm to pull next
    def select_arm(self) -> int: ...
    # updates the agent's internal estimate after observing a reward
    def update(self, arm: int, reward: float) -> None: ...


@dataclass
# stores the final results of a run
class RunResult:
    total_reward: float
    total_regret: float

# runs an agent in a bandit environment for a fixed number of steps
def run(env: BanditEnv, agent: Agent, steps: int) -> RunResult:
    # tracks cumulative rewards
    total_reward = 0.0
    # tracks cumulative regret
    total_regret = 0.0

    # tries to read the optimal expected reward from the environment
    optimal = getattr(env, "optimal_mean_reward", None)

    for _ in range(steps):
        # agent chooses an arm
        arm = agent.select_arm()
        # environment returns a reward
        reward = env.pull(arm)
        # agent updates its estimates using the observed reward
        agent.update(arm, reward)

        # accumulate total reward
        total_reward += reward

        # if optimal is avaliable, compute regret for this step
        if optimal is not None:
            total_regret += (optimal - reward)

    # return totals as a single result object
    return RunResult(total_reward=total_reward, total_regret=total_regret)
