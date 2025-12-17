from bandits.environment import BernoulliBandit
from bandits.agents import RandomAgent, UCB1Agent
from bandits.simulation import run


# testing the UCB1 agent against the random agent
def main() -> None:
    # clear optimal arm
    # should cause a sizable gap between the two agents rewards and regret
    probs = [0.1, 0.2, 0.8]
    steps = 5000

    # random agent baseline
    env_random = BernoulliBandit(probs)
    random_agent = RandomAgent(n_arms=env_random.n_arms)
    random_result = run(env_random, random_agent, steps)

    # ucb1 agent 
    env_ucb = BernoulliBandit(probs)
    ucb_agent = UCB1Agent(n_arms=env_ucb.n_arms, c=1.0)
    ucb_result = run(env_ucb, ucb_agent, steps)

    # test results printed
    print("ucb1 vs random smoke test")
    print("steps:", steps)
    print("random total reward:", random_result.total_reward)
    print("ucb1   total reward:", ucb_result.total_reward)
    print("random total regret:", random_result.total_regret)
    print("ucb1   total regret:", ucb_result.total_regret)


if __name__ == "__main__":
    main()
