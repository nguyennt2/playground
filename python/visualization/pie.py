import numpy as np
import matplotlib.pyplot as plt

plt.style.use('default')
data = np.random.randint(1, 100, 8)
subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'English', 'History', 'Geography', 'Art']
plt.pie(data, labels=subjects, autopct='%1.1f%%', startangle=90, shadow=True, explode=(0, 0, 0, 0.2, 0, 0, 0, 0.1))
#plt.show()
plt.savefig('pie.png')
