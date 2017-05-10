import numpy as np
import matplotlib.pyplot as plt

from matplotlib.ticker import NullFormatter #userful for 'logit' scale

#Fixing random state in the intervel ]0, 1[
y = np.random.normal(loc = 0.5, scale = 0.4, size = 10)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

# plot with various axes scales
plt.figure(1)

# linear
plt.subplot(221)
plt.title('linear')
plt.plot(x, y)
plt.yscale('linear')
plt.grid(True)

# log
plt.subplot(222)
plt.title('log')
plt.plot(x, y)
plt.yscale('log')
plt.grid(True)

# symmentric log
plt.subplot(223)
plt.title('symlog')
plt.plot(x, y - y.mean())
plt.yscale('symlog')
plt.grid(True)

# logit
plt.subplot(224)
plt.title('logit')
plt.plot(x, y)
plt.yscale('logit')
plt.grid(True)

# Format the minor tick labels of the y-axis into empty strings with
# 'NullForamtter', to avoid cumbering the axis with too many labels.
plt.gca().yaxis.set_minor_formatter(NullFormatter())
# adjust the subplot layout, bacause the logit one way take more space
# than usual, due to y-tick label like '1 - 10^{-1}'
plt.subplots_adjust(top = 0.92, bottom =0.05, left = 0.10, right = 0.95, hspace = 0.25, wspace = 0.35)

print(y)
print(x)

plt.show()