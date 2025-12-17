from bandits.environment import BernoulliBandit
from bandits.agents import UCB1Agent


# testing to see if ucb1 learns which is the best arm
def main() -> None:
    # clear optimal arm
    probs = [0.1, 0.2, 0.8]
    steps = 10000

    env = BernoulliBandit(probs)
    agent = UCB1Agent(n_arms=env.n_arms, c=1.0)

    # counts how often each arm is selected
    counts = [0] * env.n_arms

    for _ in range(steps):
        arm = agent.select_arm()
        reward = env.pull(arm)
        agent.update(arm, reward)
        counts[arm] += 1

    # works out the optimal arm based on the probablities
    best_arm = max(range(env.n_arms), key=lambda i: probs[i])

    print("ucb1 arm selection check")
    print("steps:", steps)
    print("arm probabilities:", probs)
    print("selection counts:", counts)
    print("optimal arm:", best_arm)

    # informs the user if the best arm was identified
    if counts[best_arm] == max(counts):
        print("check: pass (best arm selected most often)")
    else:
        print("check: warning (best arm not selected most often)")


if __name__ == "__main__":
    main()
