import numpy as np
import matplotlib.pyplot as plt


plt.style.use('default')
x = np.linspace(-10, 10, 50)
y = 10*x + 3 + np.random.normal(0, 300, 50)

plt.bar(x, y, color='blue', alpha=0.5)

plt.title('Bar Plot')
plt.xlabel('X')
plt.ylabel('Y')

plt.grid()
plt.show()
