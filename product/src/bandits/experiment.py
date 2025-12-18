from __future__ import annotations

from dataclasses import dataclass

from .environment import BernoulliBandit
from .simulation import Agent


@dataclass
# stores each value of regret over the course of one run
class TimeSeriesResult:
    regrets: list[float]


# selected agent runs for fixed number of steps
# cumulative regret is recorded at each time step
def run_regret_timeseries(env: BernoulliBandit, agent: Agent, steps: int) -> TimeSeriesResult:
    regrets: list[float] = []

    # cumulative total
    total_regret = 0.0

    # uses the best arm probability per step
    optimal = env.optimal_mean_reward

    for _ in range(steps):
        arm = agent.select_arm()
        reward = env.pull(arm)
        agent.update(arm, reward)

        # works out the regret
        # how much reward is missed compared to the optimal arm
        total_regret += (optimal - reward)
        regrets.append(total_regret)

    return TimeSeriesResult(regrets=regrets)
