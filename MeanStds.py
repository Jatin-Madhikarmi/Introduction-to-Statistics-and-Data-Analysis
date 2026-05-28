import numpy as np

# Here we specify the value of the seed number becuase we want to reproduce the same result again and again if we omit this line then
# everytime we get a new values for our poulation_data and hence all the other values like mean and standard deviation of populatin and
# sample would differ
np.random.seed(42)


# In a Poisson Distribution which is used to determine how many events occurs in a given amount of time or space, the parameter lamda 
# represents both the expected average and variance of the distribution  
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