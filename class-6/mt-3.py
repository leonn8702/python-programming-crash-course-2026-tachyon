import matplotlib.pyplot as plt
import numpy as np

# Generate random data with a linear trend
x = np.linspace(0, 50, 50)
y = x + np.random.normal(0, 5, 50)

plt.scatter(x, y, color='purple', alpha=0.6, edgecolors='black')
plt.title("Study Hours vs. Exam Score")
plt.xlabel("Hours Studied")
plt.ylabel("Score")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()