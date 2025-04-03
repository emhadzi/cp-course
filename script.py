# filepath: c:\Users\ManosChatzigeorgiou\Documents\cp-course\additions_counter.py
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate the number of additions
def count_additions(n):
    additions = 0
    for i in range(n):
        for j in range(i, n):
            additions += (j - i + 1)
    return additions

# Values of n
n_values = [5, 7, 10, 12, 15, 18, 22]
additions = [count_additions(n) for n in n_values]

# Continuous function for real number of additions
def continuous_additions(n):
    return (n * (n + 1) * (n + 2)) / 6

# Generate continuous values for the plot
n_continuous = np.linspace(min(n_values), max(n_values), 500)
additions_continuous = continuous_additions(n_continuous)

# Print results
print("| n   | Additions |")
print("|-----|-----------|")
for n, add in zip(n_values, additions):
    print(f"| {n:<3} | {add:<9} |")

# Plot the graph
plt.figure(figsize=(8, 5))
plt.plot(n_values, additions, marker='o', color='b')  # No label for the blue line
plt.plot(n_continuous, additions_continuous, color='r', linestyle='--', 
         label='(n * (n + 1) * (n + 2)) / 6')  # Updated label
plt.title('Number of Additions vs n')
plt.xlabel('n')
plt.ylabel('Number of Additions')
plt.grid(True)
plt.legend()
plt.savefig('additions_graph.png')
plt.show()