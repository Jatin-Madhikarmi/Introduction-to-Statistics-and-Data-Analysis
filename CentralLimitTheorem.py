import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 1. Setup Parameters
num_simulations = 10000  # How many sample means we will collect
sample_size = 50         # Size of each individual sample (n)

# 2. Define a non-normal underlying population (Exponential Distribution)
# For an exponential distribution, mean = scale, and variance = scale^2
pop_scale = 2 
true_mean = pop_scale
true_var = pop_scale ** 2
# Expected standard error of the mean (CLT prediction)
expected_std = np.sqrt(true_var / sample_size)

# 3. Run the Simulation
sample_means = []
for _ in range(num_simulations):
    # Draw a random sample of size 'n' from the skewed population
    sample = np.random.exponential(scale=pop_scale, size=sample_size)
    # Calculate the mean of this specific sample (X-bar)
    sample_means.append(np.mean(sample))

# 4. Plotting the Results
plt.figure(figsize=(10, 6))

# Plot the histogram of the simulated sample means
plt.hist(sample_means, bins=50, density=True, alpha=0.6, color='g', edgecolor='black', label='Simulated $\\bar{X}$')

# Plot the theoretical Normal Distribution curve predicted by the CLT
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
# CLT states: Mean = true_mean, Std Dev = true_std / sqrt(n)
p = norm.pdf(x, true_mean, expected_std)

plt.plot(x, p, 'r-', linewidth=2.5, label='CLT Normal Approximation')

# Formatting the plot
plt.title(f'Normal Approximation to Distribution of $\\bar{{X}}$\n(Sample Size $n$ = {sample_size})', fontsize=14)
plt.xlabel('Value of $\\bar{{X}}$ (Sample Mean)', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.legend(fontsize=11)
plt.grid(axis='y', alpha=0.3)

plt.show()