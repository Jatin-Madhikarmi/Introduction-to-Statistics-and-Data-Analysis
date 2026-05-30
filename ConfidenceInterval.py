import numpy as np
import scipy.stats as stats

# 1. Set simulation parameters
np.random.seed(42)          # For reproducibility
mu = 50                     # True population mean
sigma = 10                  # True population standard deviation
n = 30                      # Sample size for each individual experiment
confidence_level = 0.95     # Desired confidence level (1 - alpha)
num_simulations = 10000     # Number of times to repeat the experiment

# 2. Generate random samples
# This creates a 2D matrix of shape (10000, 30) where each row is a separate sample
samples = np.random.normal(mu, sigma, (num_simulations, n))

# 3. Compute sample statistics for each simulation (axis=1 calculates across columns)
sample_means = np.mean(samples, axis=1)
sample_stds = np.std(samples, axis=1, ddof=1)  # ddof=1 ensures sample std dev (n-1)

# 4. Calculate critical t-value
degrees_of_freedom = n - 1
# stats.t.ppf finds the critical value for the specified cumulative probability
t_critical = stats.t.ppf((1 + confidence_level) / 2, df=degrees_of_freedom)

# 5. Compute Margin of Error and Confidence Intervals
margin_of_error = t_critical * (sample_stds / np.sqrt(n))
ci_lower = sample_means - margin_of_error
ci_upper = sample_means + margin_of_error

# 6. Evaluate how many intervals successfully captured the true population mean (mu)
contains_mu = (ci_lower <= mu) & (mu <= ci_upper)
success_count = np.sum(contains_mu)
proportion_success = success_count / num_simulations

# 7. Print the results
print(f"--- Simulation Summary ---")
print(f"Total Simulations Conducted : {num_simulations}")
print(f"True Population Mean (\u03bc)   : {mu}")
print(f"Intervals Containing \u03bc      : {success_count}")
print(f"Empirical Coverage Rate     : {proportion_success * 100:.2f}%")