import MeanStds
import matplotlib.pyplot as plt

plt.hist(MeanStds.sample_data,bins=MeanStds.np.arange(MeanStds.sample_data.min(),MeanStds.sample_data.max() + 1)-0.5,density=True,alpha=0.6,color='blue',edgecolor='black',label='Sample Histrogram')

x_vals=MeanStds.np.arange(0,MeanStds.population_data.max())
fit_pmf=MeanStds.poisson.pmf(x_vals,mu=MeanStds.sample_mean)

plt.plot(x_vals, fit_pmf, 'r-', lw=2, label=f'Best-fit Poisson (λ={MeanStds.sample_mean:.2f})')
plt.xlabel('Value')
plt.ylabel('Density / Probability')
plt.title('Sample Histogram vs. Best-Fit Poisson Distribution')
plt.legend()
plt.show()