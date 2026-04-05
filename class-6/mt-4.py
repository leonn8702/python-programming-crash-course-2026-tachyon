import matplotlib.pyplot as plt
import numpy as np

# Generate a normal distribution
data = np.random.normal(100, 15, 1000)

plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.axvline(np.mean(data), color='red', linestyle='dashed', linewidth=2, label='Mean')
plt.title("IQ Distribution Simulation")
plt.legend()
plt.show()