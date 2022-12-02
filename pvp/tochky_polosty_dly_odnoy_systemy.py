import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sympy import solve, Symbol

'''
def vec(A, B):
    # vector AB
    mod = (((A - B) ** 2).sum()) ** 0.5
    dir = (B - A) / mod
    return mod, dir


def dist_ax(A):
    dist = (A[0] ** 2 + A[1] ** 2) ** 0.5
    return dist


def g(m, mod_r, dir_r):
    G = 5.9 * 10 ** 12
    mod_g = G * m / mod_r ** 2
    dir_g = -1 * dir_r
    return dir_g * mod_g


def cen_acc(A, T):
    dist = dist_ax(A)
    cen_acc_mod = 4 * np.pi ** 2 / T ** 2 * dist
    vspom = np.array([1, 1, 0]) * A
    cen_acc_dir = vspom / ((vspom[0] ** 2 + vspom[1] ** 2) ** 0.5)
    return cen_acc_dir * cen_acc_mod


def acceleration_point(point, m1, m2, a):
    mod_r1, dir_r1 = vec(np.array([0, 0, 0]), point)
    g1 = g(m1, mod_r1, dir_r1)
    mod_r2, dir_r2 = vec(np.array([a, 0, 0]), point)
    g2 = g(m2, mod_r2, dir_r2)
    T = (a ** 3 / (m1 + m2)) ** 0.5
    cen_ac = cen_acc(point, T)
    return g1 + g2 + cen_ac


def pole_(limit, step, m1, m2, a):
    pole_ = []
    diapozon = np.arange(-limit, limit, step)
    for x in diapozon:
        pole_.append([])
        ix = int(x / step + limit / step)
        for y in diapozon:
            pole_[ix].append([])
            iy = int(y / step + limit / step)
            for z in diapozon:
                iz = z / step + limit / step
                pole_[ix][iy].append(acceleration_point(np.array([x, y, z]), m1, m2, a))
    return pole_


def is_in_lobe(point, pole):
    x = point[0]
    y = point[1]
    z = point[2]
    ix = int(x / step + limit / step)
    iy = int(y / step + limit / step)
    iz = int(z / step + limit / step)
    acc = pole[ix][iy][iz]
    acc_dir = acc / ((acc ** 2).sum()) ** 0.5
    if np.dot(acc_dir, point) < 0:
        return True
    else:
        print(acc_dir, point)
        return False
'''

def grav_potencial(point_m_vec, m):
    '''считает грав потенциал от массы m в точке, вектор из которой в массу m - point_m_vec'''
    G = 6.67 * 10 ** (-11)
    pot = -1 * G * m / (np.dot(point_m_vec, point_m_vec)) ** 0.5
    return pot


def centr_potetial(point, T, a, m1, m2):
    '''считает центробежный потенциал от массы m в точке, радиус вектор которой - point'''
    omega = 2 * np.pi / T
    A_sht_vec = np.array([a * m2 / (m1 + m2), 0, 0])
    vec = point * np.array([1, 1, 0]) - A_sht_vec
    pot = -1 * abs(np.dot(vec, vec)) * omega ** 2 / 2
    return pot


def total_potential(point, m1, m2, a):
    '''считает суммарный потенциал в точке point'''
    G = 6.67 * 10 ** (-11)
    a = a * 150000000000
    m1 = m1 * 2 * 10 ** 30
    m2 = m2 * 2 * 10 ** 30
    #T = 2 * np.pi * (a ** 3/ G / (m1 + m2)) ** 0.5
    T = 2 * np.pi * (a ** 3 / (m1 + m2) / G) ** 0.5
    pot = grav_potencial(point, m1) + grav_potencial(point - np.array([a, 0, 0]), m2) + centr_potetial(point, T, a, m1,
                                                                                                       m2)
    return pot


def pole_(limit, step, m1, m2, a):
    '''создает поле (трехмерный массив из потенциалов размером 2а * 2а вокруг звезды с размером ячейки, приближающей точку step)'''
    pole_ = []
    diapozon = np.arange(-limit, limit, step)
    for x in diapozon:
        pole_.append([])
        ix = int(x / step + limit / step)
        for y in diapozon:
            pole_[ix].append([])
            iy = int(y / step + limit / step)
            for z in diapozon:
                iz = z / step + limit / step
                pole_[ix][iy].append(total_potential(np.array([x, y, z]), m1, m2, a))
    #print(pole_[20][20][39])
    return pole_

'''
def solving_x5(a0, a1, a2, a3, a4, a5, a):
    beg = 0
    end = a
    fig = plt.figure(figsize=(7, 4))
    ax = fig.add_subplot()
    axx = np.arange(0, a, 0.01)
    ax.plot(axx, a5 * axx ** 5 + a4 * axx ** 4 + a3 * axx ** 3 + a2 * axx ** 2 + a1 * axx + a0)
    # plt.show()
    for i in range(20):
        x = (end - beg) / 2
        if a5 * x ** 5 + a4 * x ** 4 + a3 * x ** 3 + a2 * x ** 2 + a1 * x + a0 > 0:
            beg = (end - beg) / 2
        else:
            end = (end - beg) / 2
    print(beg)
    return beg
'''

def solving_x3(b1, b2, b3, a):
    ''' решает уравнение для нахождения расстояния до точки лагранжа L1(бин поиск)'''
    beg = 0
    end = a
    '''
    fig = plt.figure(figsize=(7, 4))
    ax = fig.add_subplot()
    axx = np.arange(0.1 * a, 0.9 * a, 1000000)
    ax.plot(axx / a, b1 / (axx ** 2) + b2 / ((a - axx) ** 2) + (axx - a * m2 / (m1 + m2)) * b3)
    plt.show()
    '''
    for i in range(100):
        x = (end + beg) / 2
        if b1 / (x ** 2) + b2 / ((a - x) ** 2) + (x - a * m2 / (m1 + m2)) * b3 < 0:
            beg = (end + beg) / 2
        else:
            end = (end + beg) / 2
    # print(beg / a)
    # print(b1 / beg ** 2 + b2 / (a - beg) ** 2 + (beg - a * m2 / (m1 + m2)) * b3)
    # print()
    # print(b1 / beg ** 2)
    # print(b2 / (a - beg) ** 2)
    # print((beg - a * m2 / (m1 + m2)) * b3)
    return beg


def L1_potential(m1, m2, a):
    ''' считает потенциал точки L1 и возвращает расстоние до нее'''
    G = 6.67 * 10 ** (-11)
    omega = 2 * np.pi / (a ** 3 / (m1 + m2)) ** 0.5
    av = a * 150000000000
    m1v = m1 * 2 * 10 ** 30
    m2v = m2 * 2 * 10 ** 30
    omega = 1 / (av ** 3 / (m1v + m2v) / G) ** 0.5
    par = G
    b1 = - 1 * m1v * par
    b2 = par * m2v
    b3 = omega ** 2
    a0 = G * m1 * a ** 2
    a1 = -2 * G * m1 * a
    a2 = G * (m1 - m2) - a ** 3 * omega ** 2
    a3 = 3 * omega ** 2 * a ** 2
    a4 = -3 * omega ** 2 * a
    a5 = omega ** 2
    # solving_x3(b1, b2, b3, a)
    l = solving_x3(b1, b2, b3, av) / 150000000000
    pot = total_potential(np.array([l, 0, 0]), m1, m2, a)
    '''
    T = (a ** 3 / (m1 + m2)) ** 0.5
    point = np.array([l, 0, 0])
    g1 = grav_potencial(point, m1)
    g2 = grav_potencial(point - np.array([a, 0, 0]), m2)
    cpot = centr_potetial(point, T, a, m1, m2)
    print()
    print(g1, g2, cpot)
    print()
    pot = grav_potencial(point, m1) + grav_potencial(point - np.array([a, 0, 0]), m2) + centr_potetial(point, T, a, m1, m2)
    '''
    #print('l1p', pot)
    return pot, l


def is_lobe(point, pole, LP1, tochnost):
    ''' проверяет, является ли точка point границей полости(сравнивая с потенциалом L1), учитывая точность определения границы полости и шаг отрисовки'''
    x = point[0]
    y = point[1]
    z = point[2]
    ix = int(x / step + limit / step)
    iy = int(y / step + limit / step)
    iz = int(z / step + limit / step)
    P = pole[ix][iy][iz]
    if pole[ix][iy][iz] < LP1 + tochnost and pole[ix][iy][iz] > LP1 - tochnost:
        return 1
    else:
        return 0


def lobe(m1, m2, a, limit, step):
    ''' создает пространство точек со значением 1, если они часть полости и 0 если нет, создает масивы xg, yg, xg с координатами точек полости'''
    xg = []
    yg = []
    zg = []
    pole = pole_(limit, step, m1, m2, a)
    space = []
    lp1, l1 = L1_potential(m1, m2, a)
    l1_ = l1 + a / limit * step
    tochnost = abs(total_potential(np.array([l1_, 0, 0]), m1, m2, a) - lp1) * 3 ** 0.5
    #print(tochnost)
    diapozon = np.arange(-limit, limit, step)
    for x in diapozon:
        space.append([])
        ix = int(x / step + limit / step)
        for y in diapozon:
            space[ix].append([])
            iy = int(y / step + limit / step)
            for z in diapozon:
                iz = int(z / step + limit / step)
                param = is_lobe(np.array([x, y, z]), pole, lp1, tochnost)
                if param == 1:
                    xg.append(x)
                    yg.append(y)
                    zg.append(z)
                space[ix][iy].append(param)
    xg = np.array(xg)
    yg = np.array(yg)
    zg = np.array(zg)
    return space, xg, yg, zg, l1_


m1 = 1
m2 = 100
a = 1

n = m1 / m2

limit = a
step = 0.05
lobe, xg, yg, zg, l1_ = lobe(m1, m2, float(a), limit, step)
#print()
c = 0

''' рисуем модель полости по полученным данным'''

fig = plt.figure(figsize=(5, 5))
ax_3d = Axes3D(fig)
ax_3d.scatter(xg, yg, zg, color='g', s=5)
ax_3d.scatter(np.array([0]), np.array([0]), np.array([0]), color='r', s=20)
ax_3d.scatter(np.array([a]), np.array([0]), np.array([0]), color='b', s=20)
ax_3d.scatter(np.array([l1_]), np.array([0]), np.array([0]), color='y', s=20)
ax_3d.set_xlabel('x')
ax_3d.set_ylabel('y')
ax_3d.set_zlabel('z')
ax_3d.set_xlim([-a, 2 * a])
ax_3d.set_ylim([-a, a])
ax_3d.set_zlim([-a, a])
plt.show()

'''
for x in lobe:
    for y in x:
        for z in y:
            if z == 1:
                c += 1
print(c)
'''





