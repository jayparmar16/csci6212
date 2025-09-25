import matplotlib.pyplot as plt
import numpy as np

n_values = np.array([
    1000, 5000, 10000, 100000, 150000, 1000000, 1500000,
    10000000, 15000000, 100000000, 150000000, 1000000000
])

experimental_times = np.array([
    0.000050, 0.000072, 0.000062, 0.000099, 0.000109, 0.000151, 0.000165,
    0.000253, 0.000242, 0.000304, 0.000325, 0.000430
])

normalized_theoretical_times = np.array([
    0.000048, 0.000073, 0.000085, 0.000133, 0.000142, 0.000191, 0.000202,
    0.000260, 0.000273, 0.000340, 0.000355, 0.000430
])


# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 6)) # Using a single axes object

# Plot Experimental Time
ax.plot(n_values, experimental_times, marker='o', linestyle='-',
         color='royalblue', label='Experimental Time (s)')

# Plot Normalized Theoretical Time
ax.plot(n_values, normalized_theoretical_times, marker='x', linestyle='--',
         color='darkorange', label=r'Normalized Theoretical Time ($\Theta(\ln^2 N)$)')

# Set x-axis and y-axis to logarithmic scale
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_title('Time Complexity: Experimental vs. Theoretical', fontsize=16)
ax.set_xlabel('Input Size (N) - Log Scale', fontsize=12)
ax.set_ylabel('Execution Time (seconds) - Log Scale', fontsize=12)

# Add legend
ax.legend(loc='upper left', fontsize=11)

# Add grid lines
ax.grid(True, which="both", ls="--", linewidth=0.5)

fig.tight_layout() # Adjust layout to prevent labels from overlapping
plt.savefig('complexity_analysis.png', dpi=300)
print("Plot has been generated and saved as 'complexity_analysis.png'")