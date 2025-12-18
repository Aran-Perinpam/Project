from bandits.environment import BernoulliBandit
from bandits.agents import EpsilonGreedyAgent
from bandits.simulation import run


# testing if the epsilon greedy agents functions
def main() -> None:
    probs = [0.1, 0.2, 0.8]
    steps = 5000

    env = BernoulliBandit(probs)
    agent = EpsilonGreedyAgent(n_arms=env.n_arms, epsilon=0.1, seed=1)

    result = run(env, agent, steps)

    print("epsilon-greedy test")
    print("steps:", steps)
    print("epsilon:", 0.1)
    print("total reward:", result.total_reward)
    print("total regret:", result.total_regret)


if __name__ == "__main__":
    main()
