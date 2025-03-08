import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


plt.style.use('default')
raw = pd.read_csv('data/population.csv')
#population = np.random.randint(100, 1000, 6)
#year = [2019, 2020,2021, 2022, 2023, 2024]
plt.plot(raw['year'], raw['population'], color='red', linestyle='--', linewidth=2, label='Population')
plt.plot(raw['year'], raw['gdp'], color='blue', linestyle='-', linewidth=4, label='GDP')
plt.legend(loc='upper left')
# plt.legend(['Population', 'GDP'])
plt.xticks(raw['year'])
plt.yticks(np.arange(0, 2000, 200))
plt.title('Population and GPD') # title
plt.xlabel('Year') # x-axis label
plt.ylabel('Millions') # y-axis label
plt.xlim(2019, 2022)
plt.grid()
plt.show()
