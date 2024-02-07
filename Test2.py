import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# generate some random data
x = np.array([1.1, 9.9, 14.8, 19.8, 21.7, 21.9, 22, 22.1, 22.5, 24.6, 25, 29.2, 30.4])
y = np.array([1.08, 1.45, 1.73, 2.31,3.39, 4.00, 9.99, 10.36, 11.05, 11.73, 11.79, 12.14, 12.19])

# create an interpolation function
f = interp1d(x, y, kind='linear')

# create a new set of x-values for the fitted curve
x_new = np.linspace(x[0], x[-1], num=1000, endpoint=True)

# evaluate the interpodsfkjaffdlksafdalkjflation function at the new x-values
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
