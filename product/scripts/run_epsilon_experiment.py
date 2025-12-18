import csv
import os

from bandits.environment import BernoulliBandit
from bandits.agents import EpsilonGreedyAgent
from bandits.experiment import run_regret_timeseries


# runs epsilon greedy for 3 epsilon values
# saves regret values to a csv file
def main() -> None:
    
    epsilons = [0.01, 0.1, 0.3]
    steps = 80000

    # fixed environment (not needed but there for reproducibility)
    probs = [0.1, 0.2, 0.8]
    env_seed = 42
    agent_seed = 1

    # creates the output folder
    out_dir = os.path.join("product", "output")
    os.makedirs(out_dir, exist_ok=True)

    out_path = os.path.join(out_dir, "epsilon_regret_curves.csv")

    # stores the regret values from the different epsilon values
    results = {}

    for eps in epsilons:
        env = BernoulliBandit(probs, seed=env_seed)
        agent = EpsilonGreedyAgent(n_arms=env.n_arms, epsilon=eps, seed=agent_seed)
        ts = run_regret_timeseries(env, agent, steps)
        results[eps] = ts.regrets
        print("finished epsilon:", eps)

    # creates the csv file
    # contains 4 columns
    # step, regret_e0.01, regret_e0.1, and regret_e0.3
    with open(out_path, "w", newline="") as f:
        writer = csv.writer(f)
        header = ["step"] + [f"regret_e{eps}" for eps in epsilons]
        writer.writerow(header)

        for i in range(steps):
            row = [i + 1] + [results[eps][i] for eps in epsilons]
            writer.writerow(row)

    print("saved:", out_path)


if __name__ == "__main__":
    main()
