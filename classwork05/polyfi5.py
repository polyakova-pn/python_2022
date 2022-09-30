import numpy as np
import matplotlib
from matplotlib import pyplot as plt

def mnk0(x, y):
    x_sq_avr = (x**2).mean()
    x_avr_sq = (x.mean())**2
    y_sq_avr = (y**2).mean()
    y_sq_avr = (y.mean())**2
    xy_avr = (x * y).mean()
    x_avr = (x).mean()
    y_avr = (y).mean()
    k = (xy_avr - x_avr * y_avr) / (x_sq_avr - x_avr_sq)

    return k, b

def mnk_deg1(x, y):
    n = len(x)
    sy = y.sum()
    sx = x.sum()
    sxy = (x * y).sum()
    sxx = (x * x).sum()

    k = (-1 * sx * sy + sxy * n) / (-1 * sx * sx + sxx * n)
    b = sy / n - k * sx / n
    return k, b

def mnk_deg2(x,y):
    sy = sum(y)
    sx = sum(x)
    sxy = sum(x[i] * y[i] for i in range(len(x)))
    sxx = sum(i ** 2 for i in x)
    k = (-1 * sx * sy + sxy) / (-1 * sx * sx + sxx)
    b = sy - k * sx
    return k, b

matplotlib.rcParams.update(matplotlib.rcParamsDefault)


def get_numbers(student):
    return student, (student + 4) % 5 + 3, student % 2 * 10 + 12, (student % 5 * 3 + 7) * 3


def fake_data_generator(seed, vmin=0, vmax=10, size=100):
    import numpy as np
    np.random.seed(seed)
    data = np.random.randint(vmin, vmax, size=20)
    mean = data.mean()
    std = data.std()
    noise = np.random.normal(loc=mean, scale=std ** .5, size=size)
    fake_x = np.array([-5 + i * 20 / size for i in range(size)])

    linear = lambda x, k=(.5 - np.random.rand()) * 15, b=np.random.rand() * 10: k * x + b
    linear_data = linear(fake_x)
    fake_y = linear_data + noise
    return fake_x, fake_y


student = 10  # Teacher's number
x, y = fake_data_generator(*get_numbers(student))

fig = plt.figure(figsize=(6.4, 4.8))
ax = fig.add_subplot()
ax.scatter(x, y)
k, b = mnk_deg1(x, y)
print()
print(k, b)
print(mnk_deg2(x, y))
ax.plot([-5, 15],[-5 * k + b, k * 15 + b], '--', color = 'r', alpha = 1, label = 'mnk')
kp, bp = np.polyfit(x, y, 1)
print(kp, bp)
ax.plot([-5, 15],[-5 * kp + bp, kp * 15 + bp], ':', color = 'b', alpha = 1, label = 'polyfit')
ax.set_xlabel('X')
ax.set_ylabel('Y')
plt.grid()
plt.legend()
plt.show()