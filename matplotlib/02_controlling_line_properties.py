import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0., 5., 0.1)


plt.plot(t, t, linewidth=2.0)

lines = plt.plot(t, t ** 2, t * 1.1, t ** 3)
# use keyword args
plt.setp(lines, color='r', linewidth=2.0)
# or MATLAB style string value pairs
plt.setp(lines, 'color', 'r', 'linewidth', 2.0, 'alpha', 0.1)

plt.show()