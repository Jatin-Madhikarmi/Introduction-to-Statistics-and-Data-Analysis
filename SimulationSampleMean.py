import MeanStds
import scipy.stats as stats
import matplotlib.pyplot as plt

num_simulation=100
small_sample_size=30

sample_means=[]

for _ in range(num_simulation):
    sim_sample=MeanStds.np.random.choice(MeanStds.population_data,small_sample_size,False)
    sample_means.append(MeanStds.np.mean(sim_sample))

plt.hist(sample_means,bins=15,density=True,alpha=0.6,color='skyblue',edgecolor='black',label='Empirical X-bar')

std_err=MeanStds.population_std/MeanStds.np.sqrt(small_sample_size)
x_axis=MeanStds.np.linspace(MeanStds.population_mean-4*std_err,MeanStds.population_mean+4*std_err,100)
plt.plot(x_axis,stats.norm.pdf(x_axis,MeanStds.population_mean,std_err),'y-',lw=3,label='CLT Normal Approx')

plt.xlabel('Sample Mean (X-Bar)')
plt.ylabel('Density')
plt.title(f'Distribution of Sample Means (n={small_sample_size})')
plt.legend()
plt.show()