import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binomtest

# Set the random seed
np.random.seed(41)

min_flips = 20
max_flips = 50

initial_flips = np.random.binomial(1, 0.5, min_flips).tolist()

n_values = []
p_values = []
current_flips = initial_flips.copy()

for n in range(min_flips, max_flips + 1):
    if n > min_flips:
        new_flip = np.random.binomial(1, 0.5)
        current_flips.append(new_flip)
        
    heads = sum(current_flips)
    result = binomtest(heads, n, p=0.5, alternative='two-sided')
    
    n_values.append(n)
    p_values.append(result.pvalue)

# --- PLOTTING CODE (FIXED) ---
plt.figure(figsize=(10, 5))
plt.plot(n_values, p_values, marker='o', linestyle='-', color='b', label='Calculated $p$-value')

# FIXED LINE: Changed '$lpha$' to '$\alpha$'
plt.axhline(y=0.05, color='r', linestyle='--', label='Significance Threshold ($\\alpha$ = 0.05)')

plt.title('P-Hacking Demonstration: Sequential Stopping of Data Collection')
plt.xlabel('Number of Coin Flips ($n$)')
plt.ylabel('$p$-value')
plt.xlim(min_flips, max_flips)
plt.ylim(0, 1)
plt.legend()
plt.grid(True)
plt.show()