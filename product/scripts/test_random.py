from bandits.environment import BernoulliBandit
from bandits.agents import RandomAgent
from bandits.simulation import run


# simple end-to-end test to check the random agent runs correctly
def main() -> None:
    # bandit with one clearly better arm
    env = BernoulliBandit([0.1, 0.2, 0.8])

    # random baseline agent
    agent = RandomAgent(n_arms=env.n_arms)

    # run for a small number of steps
    result = run(env, agent, steps=1000)

    print("random agent test")
    print("total reward:", result.total_reward)
    print("total regret:", result.total_regret)


if __name__ == "__main__":
    main()
