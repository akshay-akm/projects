import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt

# Define plot grid size
ROWS = 5
COLS = 5
NUM_SUBPLOTS = 10  # Number of subplots to divide into

# Generate random dataset (Soil quality & Irrigation efficiency)
np.random.seed(42)
soil_quality = np.random.randint(1, 11, size=(ROWS, COLS))
irrigation_efficiency = np.random.randint(1, 11, size=(ROWS, COLS))

# Save datasets to CSV
soil_df = pd.DataFrame(soil_quality)
irrigation_df = pd.DataFrame(irrigation_efficiency)

soil_df.to_csv("soil_quality.csv", index=False)
irrigation_df.to_csv("irrigation_efficiency.csv", index=False)

# Load datasets
soil_quality = pd.read_csv("soil_quality.csv").values
irrigation_efficiency = pd.read_csv("irrigation_efficiency.csv").values

# Calculate the quality score of a given plot division
def calculate_score(division):
    return sum(soil_quality[x, y] + irrigation_efficiency[x, y] for x, y in division)

# Generate a random initial plot division
def random_division():
    return [(random.randint(0, ROWS-1), random.randint(0, COLS-1)) for _ in range(NUM_SUBPLOTS)]

# Hill Climbing Algorithm
def hill_climbing(iterations=1000):
    current_division = random_division()
    current_score = calculate_score(current_division)
    
    for _ in range(iterations):
        # Make a small change: Swap one plot
        new_division = current_division[:]
        idx = random.randint(0, len(new_division) - 1)
        new_division[idx] = (random.randint(0, ROWS-1), random.randint(0, COLS-1))

        new_score = calculate_score(new_division)

        # Accept change if score improves
        if new_score > current_score:
            current_division, current_score = new_division, new_score

    return current_division, current_score

# Run Hill Climbing Algorithm
best_division, best_score = hill_climbing()

# Display results
print("Best Plot Division:", best_division)
print("Best Score:", best_score)

# Print the datasets
print("\nSoil Quality Data:\n", soil_quality)
print("\nIrrigation Efficiency Data:\n", irrigation_efficiency)

# Visualize the best plot division
def visualize_division(division):
    grid = np.zeros((ROWS, COLS))

    for (x, y) in division:
        grid[x, y] = 1  # Mark selected plots

    plt.figure(figsize=(6, 6))
    plt.imshow(grid, cmap="coolwarm", alpha=0.8)
    
    # Add text labels
    for i in range(ROWS):
        for j in range(COLS):
            plt.text(j, i, f"{soil_quality[i, j]}/{irrigation_efficiency[i, j]}",
                     ha="center", va="center", fontsize=10, color="black")

    plt.xticks(range(COLS))
    plt.yticks(range(ROWS))
    plt.title("Best Plot Division (Hill Climbing)")
    plt.colorbar(label="Plot Selected (1 = Selected)")
    plt.grid(color="gray", linestyle="--", linewidth=0.5)
    plt.show()

# Call visualization function
visualize_division(best_division)
