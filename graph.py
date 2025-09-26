import matplotlib.pyplot as plt
import numpy as np

n_values = np.array([
    100000, 300000, 1000000, 3000000, 10000000, 30000000, 100000000, 300000000, 500000000, 750000000
], dtype=np.float64)

experimental_times = np.array([
    0.00010386, 0.00013012, 0.00016331, 0.00019525, 0.00022194,0.00026990, 0.00030066, 0.00034757, 0.00036685, 0.00037869
])

normalized_theoretical_times = np.array([
    0.000120, 0.000144, 0.000173, 0.000202, 0.000236,0.000269, 0.000308, 0.000345, 0.000364, 0.000379
])


#  Plotting 
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 6))

# Plot Experimental Time
ax.plot(n_values, experimental_times, marker='o', linestyle='-',
         color='royalblue', label='Experimental Time (s)')

# Plot Normalized Theoretical Time
ax.plot(n_values, normalized_theoretical_times, marker='x', linestyle='--',
         color='darkorange', label=r'Theoretical Time ($\Theta(\ln^2 N)$)')

#  Axis Configuration 
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_title('Time Complexity: Experimental vs. Theoretical', fontsize=16)
ax.set_xlabel('Input Size (N) - Logarithmic Scale', fontsize=12)
ax.set_ylabel('Execution Time (seconds) - Logarithmic Scale', fontsize=12)
ax.legend(loc='upper left', fontsize=11)
ax.grid(True, which="both", ls="--", linewidth=0.5)

fig.tight_layout()
plt.savefig('complexity_analysis.png', dpi=300)
print("Plot has been generated and saved as 'complexity_analysis.png'")