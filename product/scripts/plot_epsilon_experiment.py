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

    # create graph plot
    plt.figure(figsize=(8, 5))

    for key, values in regrets.items():
        plt.plot(steps, values, label=key)

    plt.xlabel("Time step")
    plt.ylabel("Cumulative regret")
    plt.title("Epsilon-Greedy: Cumulative Regret Over Time")
    plt.legend()
    plt.grid(True)

    # save plot to a file inside the outputs folder
    plt.savefig(plot_path)
    plt.close()

    print("plot saved to:", plot_path)


if __name__ == "__main__":
    main()
