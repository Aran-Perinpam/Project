import csv
import os
import matplotlib.pyplot as plt


# plots a graph of cululative regret per step 
# takes data from the .csv file
def main() -> None:
    csv_path = os.path.join("product", "output", "epsilon_regret_curves.csv")
    plot_path = os.path.join("product", "output", "epsilon_regret_plot.png")

    steps = []
    regrets = {}

    # reads the csv data
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)

        # initialise lists for each epsilon value
        for field in reader.fieldnames:
            if field != "step":
                regrets[field] = []

        for row in reader:
            steps.append(int(row["step"]))
            for key in regrets:
                regrets[key].append(float(row[key]))


        # converts cumulative regret to average regret per step
        # instead of plotting cumulative regret against time steps
        # to achieve the expected curve on the graph
        scale = 1000.0

        plt.figure(figsize=(8, 5))

        for key, cumulative_values in regrets.items():
            avg_values = [(cumulative_values[i] / steps[i]) * scale for i in range(len(steps))]
            plt.plot(steps, avg_values, label=key)

        plt.xlabel("Time step")
        plt.ylabel("Regret (average per step × 1000)")
        plt.title("Epsilon-Greedy: Regret Over Time")
        plt.legend()
        plt.grid(True)
        plt.savefig(plot_path)
        plt.close()

    print("plot saved to:", plot_path)


if __name__ == "__main__":
    main()
