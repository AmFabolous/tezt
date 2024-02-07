import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# generate some random data
x = np.array([0.6, 4.6, 6.6, 11.1, 14.9, 19.5, 22, 23, 24.1, 25.9, 27, 27.4, 28, 30.1])
y = np.array([2.36, 3.02, 3.22, 3.55, 3.89, 4.13, 4.35, 4.46, 4.61, 4.98, 5.64, 10.22, 11.08, 11.71])

# create an interpolation function
f = interp1d(x, y, kind='linear')

# create a new set of x-values for the fitted curve
x_new = np.linspace(x[0], x[-1], num=1000, endpoint=True)

# evaluate the interpolation function at the new x-values
y_new = f(x_new)

# create the scatter plot
plt.scatter(x, y)

# add the fitted curve to the plot
plt.plot(x_new, y_new, color='red')

# set the axis labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Interpolation')

# show the plot
plt.show()
