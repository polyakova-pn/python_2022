import numpy as np
import matplotlib.pyplot as plt

fig1 = plt.figure(figsize=(6.4, 4.8))
fig2 = plt.figure(figsize=(6.4, 4.8))
ax1 = fig1.add_subplot(1, 1, 1)
ax2 = fig2.add_subplot(1, 1, 1)
ax2.minorticks_on()
ax2.grid(which='major')
ax2.grid(which='minor', linestyle = ':')


x1 = np.array(np.arange(0, 100, 10))
x2 = np.array(np.arange(10, 100, np.pi / 100))
ax1.plot(x1, [np.sin(i) * 1 / i ** 2 for i in x1])
ax2.plot(x2, [np.exp(-1 * x * np.sin(x)) for x in x2])
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax2.set_xlabel('x')
ax2.set_ylabel('y')

ax2.set_ylim([0, 100])


ax1.grid()


#третий график
fig3 = plt.figure(figsize=(6.4, 4.8))
ax3 = fig3.add_subplot(1, 1, 1)
x3 = np.array(np.arange(10, 100, np.pi / 100))
ax3.scatter(x3, [np.exp((x ** 0.5) * np.sin(x)) for x in x3])
ax3.set_xlabel('x')
ax3.set_ylabel('y')
#четвертый график
fig4 = plt.figure(figsize=(6.4, 4.8))
ax4 = fig4.add_subplot(1, 1, 1)
x4 = np.array(np.arange(50, 100, np.pi / 100))
ax4.plot(x4, [x * (np.sin(x) ** 2) for x in x4], label = 'x * sin^2(x)')
plt.yscale('log')
ax4.set_xlabel('x')
ax4.set_ylabel('log(y)')
ax4.legend()
ax4.grid()
plt.show()