import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# Points
n_values = np.array([
    1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000
], dtype=np.float64)

experimental_times = np.array([
    0.003153, 0.018297, 0.035509, 0.156415, 0.331907, 1.983047, 4.152013, 24.257462, 50.650553
])

normalized_theoretical_times = np.array([
    0.002171, 0.013369, 0.028938, 0.169894, 0.361775, 2.061451, 4.340618, 24.094520, 50.650553
])

# Plotting
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 6))

# Plot Experimental Time
ax.plot(n_values, experimental_times, marker='o', linestyle='-',
        color='royalblue', label='Experimental Time')

# Plot Normalized Theoretical Time
ax.plot(n_values, normalized_theoretical_times, marker='s', linestyle='--',
        color='crimson', label=r'Theoretical Time ($O(n \log n)$)')

# Axis Configuration
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_title('Experimental vs. Theoretical Runtime for Convex Hull', fontsize=16)
ax.set_xlabel('Input Size (N) - Logarithmic Scale', fontsize=12)
ax.set_ylabel('Execution Time (seconds) - Logarithmic Scale', fontsize=12)
ax.legend(loc='upper left', fontsize=11)
ax.grid(True, which="both", ls="--", linewidth=0.5)

# Use a more readable format for the axis ticks
ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))
ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y:.4f}'))


fig.tight_layout()
plt.savefig('convex_hull_complexity_analysis.png', dpi=300)
print("Plot has been generated and saved as 'convex_hull_complexity_analysis.png'")