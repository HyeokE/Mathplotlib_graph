import matplotlib.pyplot as plt
import numpy as np
plt.subplot(2,3,1)

x = np.linspace(-10, 10, 5000)

y = (np.where((x<-0.5 )| (x>0.5), 0, 1))
plt.axis([-10, 10, -0.5, 1.5])
plt.plot(x, y)
plt.grid()

plt.subplot(2,3,2)
x = np.linspace(-10, 10, 5000)
y = (np.where((x<-2.5 )| (x>2.5), 0, 1))
plt.axis([-10, 10, -0.5, 1.5])
plt.plot(x, y)
plt.grid()

plt.subplot(2,3,3)
x = np.linspace(-10, 10, 5000)

y = (np.where((x<-5 )| (x>5), 0, 1))
plt.axis([-10, 10, -0.5, 1.5])
plt.plot(x, y)
plt.grid()

plt.subplot(2,3,4)
x = np.linspace(-3, 3, 5000)
y = np.sin(np.pi*x)/(x*np.pi)
plt.plot(x, y)
plt.grid()

plt.subplot(2,3,5)
x = np.linspace(-3, 3, 5000)
y = (np.sin(np.pi*x*5))/(x*np.pi*5)
plt.plot(x, y)
plt.grid()

plt.subplot(2,3,6)
x = np.linspace(-3, 3, 5000)
y = (np.sin(np.pi*x*10))/(x*np.pi*10)
plt.plot(x, y)

plt.grid()
plt.show()

plt.subplot(1,2,1)
x = np.linspace(-0.1, 0.1, 5000)

y = (np.where((x>0.05 )| (x<-0.05), 0, 1)) * (np.cos(2 * np.pi * x * 100))
plt.axis([-0.1, 0.1, -1.5, 1.5])
plt.plot(x, y)
plt.grid()

plt.subplot(1,2,2)
x = np.linspace(-200, 200, 5000)
y1 = (0.5)*((np.sin((0.1*(x-100))*np.pi))/(np.pi*(0.1*(x-100)))
            +(np.sin((0.1*(x+100))*np.pi))/(np.pi*(0.1*(x+100))))
y = np.where(y1 < 0, -y1, y1)
plt.axis([-200, 200, 0, 0.6])
plt.plot(x, y)
plt.grid()
plt.show()

