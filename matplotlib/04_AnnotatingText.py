import numpy as np
import matplotlib.pyplot as plt


plt.figure("HellWorld")
plt.subplot(212)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2 * np.pi * t)

plt.plot(t, s, lw = 2)

plt.annotate('Local max', xy = (2, 1), xytext = (3, 1.5), 
	arrowprops = dict(facecolor = 'red', shrink = 0.01))

plt.show()