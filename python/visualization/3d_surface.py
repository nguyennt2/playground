import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
xx, yy = np.meshgrid(x, y)
#z = xx**2 + yy**2
#z = np.sin(xx) * np.cos(yy)
z = xx**2 - yy**2


fig = plt.figure(figsize=(12, 8))
ax = plt.subplot(projection='3d')
#p = ax.plot_surface(xx, yy, z, cmap='viridis', alpha=0.5)
#ax.plot_surface(xx, yy, z, color='blue', alpha=0.5)
p = ax.contour3D(xx, yy, z, 50, cmap='viridis')
fig.colorbar(p)
ax.set_title('3D Surface Plot')
plt.show()
