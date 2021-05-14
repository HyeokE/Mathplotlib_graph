from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

# t = np.linspace(-10, 10, 500)
# plt.plot(t, signal.square(2 * np.pi * 5 * t),'b')
# plt.ylim(-2, 2)
plt.grid(0.5)
# plt.show()
plt.plot([-10,-5, 0, 5, 10], [0,0,1,0,0])
plt.xlim(-10, 10)
plt.ylim(0.5, 1.5)
plt.show()