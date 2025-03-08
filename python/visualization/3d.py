import numpy as np
import matplotlib.pyplot as plt



#x = np.linspace(-10, 10, 50)
#y = 10*x + 3 + np.random.normal(0, 300, 50)
#plt.scatter(x, y, color='red', marker='o', s=50, alpha=0.5)
#plt.title('Scatter Plot 2D')

plt.style.use('default')
fig = plt.figure(figsize=(10, 7))
ax = plt.subplot(projection='3d')
ax.scatter3D(np.random.randint(0, 100, 50), np.random.randint(0, 100, 50), np.random.randint(0, 100, 50), color='red', marker='o', s=50, alpha=0.5)
ax.set_title('Scatter Plot 3D')
ax.set_xlabel('Runtime')
ax.set_ylabel('Budget')
ax.set_zlabel('Rating')

x = [0, 1, 5, 25, 50, 100]
y = [0, 10,13, 15, 20, 25]
z = [0, 1, 5, 10, 15, 100]
ax.plot3D(x, y, z, color='blue', linestyle='-', linewidth=2)
plt.grid()
plt.show()
