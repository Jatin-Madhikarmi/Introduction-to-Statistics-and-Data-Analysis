import numpy as np

np.random.seed(42)

lamda_val=10
population_size=10000

population_data=np.random.poisson(lamda_val,population_size)

sample_size=200
sample_data=np.random.choice(population_data,sample_size,False)

population_mean=np.mean(population_data)
population_std=np.std(population_data)

sample_mean=np.mean(sample_data)
sample_std=np.std(sample_data)

print(f"Population Mean: {population_mean}")
print(f"Population Standard Deviation: {population_std}")
print(f"Sample Mean: {sample_mean}")
print(f"Sample Standard Deviation: {sample_std}")