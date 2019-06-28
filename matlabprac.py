# %matplotlib inline
# form scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 3, .001)
axes = plt.axes()
axes.set_xlim(0, 10)
axes.set_ylim(-5, 5)
axes.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
axes.set_yticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
plt.xlabel("This is x axis")
plt.ylabel("This is y axis")
axes.grid()
x = np.arange(-5, 5, 1)
y = np.arange(5, -5, -1)
plt.plot(x,'b-')
plt.plot(y, 'r ')
plt.show()
