# Final Year Project

This repository contains my Final Year Project work. So far, the repository contains two main components:

- **A multi armed bandit solver**
- **Connect Four game**

## Structure

- 'diary.md' -- Weekly progress diary
- 'product/' -- Source code
- 'documents/' -- reports and supporting documents

## Requirements

- Python 3.10+
- pip

## Required Python packages

- pygame
- matplotlib

## Running the Bandit tests

From the repository root run:

set PYTHONPATH=product\src
python product\scripts\test_random_agent.py
python product\scripts\test_ucb1_agent.py
python product\scripts\test_epsilon_greedy.py

## Running the Bandit Experiment

First run these commands to generate the regret data:

set PYTHONPATH=product\src
python product\scripts\run_epsilon_experiment.py

To generate the .csv file

product/output/epsilon_regret_curves.csv

## Plotting Bandit Results

To generate a graph from the experiment data run:

set PYTHONPATH=product\src
python product\scripts\plot_epsilon_experiment.py
python product\scripts\plot_epsilon_experiment_2.py

To generate two .png files:

product/output/epsilon_regret_plot.png
product/output/epsilon_regret_plot_2.png

## Running Connect Four

To run the game:

set PYTHONPATH=product\src
python product\scripts\connect4_pygame.py

- Left mouse click drops a disc in the hovered column
- 'r' Restarts the game to its default state
- Close the window to exit
