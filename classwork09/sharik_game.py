def game(screen, COLORS, FPS_local, FPS_total):
    '''
    Основная функция, запускает процесс игры, считает попадания, вырождает новые порции объектов
    в рандомные моменты выводит на экран очень дорогие, но очень маленькие белые точки
    :param screen: экран на котором все происходит
    :param COLORS: список цветов объектов
    :param FPS_local: тики, с которыми перемещается данная партия шаров
    :param FPS_total: тики, с которыми вырождаются новые порции объектов
    '''
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    score = 0
    while not finished:
        current_balls = new_ball(COLORS)
        dot_exist = False
        if randint(1, 20) == 1:
            dot_exist = True
            current_dot = dot()
        for i in range(int(FPS_local // FPS_total)):
            clock.tick(FPS_local)
            current_balls = motion(current_balls)
            if dot_exist:
                make_dot(current_dot)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print('Click!')
                    if popal(event, current_balls):
                        score += 1
                        print('ПОПАЛ! счет:', score)
                    if popal_dot(event, current_dot):
                        score += 10
                        print('ПОПАЛ В ТОЧКУ! счет:', score)
            pygame.display.update()

        pygame.display.update()
        screen.fill((0, 0, 0))


def make_dot(current_dot):
    '''
    создает точку в данном месте
    :param current_dot: параметры точки (координаты и радиус)
    :return: ничего
    '''
    x = current_dot[0]
    y = current_dot[1]
    r = current_dot[2]
    circle(screen, (255, 255, 255), (x, y), r)
    return
def dot():
    '''
    создает точку
    :return: координаты и радиус точки
    '''
    x = randint(101, 1099)
    y = randint(101, 799)
    r = 3
    circle(screen, (255, 255, 255), (x, y), r)
    current_dot = [x, y, r]
    return current_dot

def popal_dot(event, current_dot):
    '''
    определяет местоположение клика и показывает, попал ли игрок по шару
    mx, mу - координаты мыши при нажатии
    x, y - координаты точки при нажатии
    dest - расстояние от цетнра точки до курсора при нажатия
    popadanie - переменная попадания или промаха

    '''
    mx = event.pos[0]
    my = event.pos[1]
    popadanie_hot_v_odin = False

    x = current_dot[0]
    y = current_dot[1]
    r = current_dot[2]
    dest = ((mx - x) ** 2 + (my - y) ** 2) ** 0.5
    if dest <= r:
        popadanie = True
    return popadanie

def popal(event, current_balls):
    '''
    определяет местоположение клика и показывает, попал ли игрок по шару
    mx, mу - координаты мыши при нажатии
    x, y - координаты шаров при нажатии
    dest - расстояние от цетнра шара до точки нажатия
    popadanie - список попаданий или промахов
    popadanie_hot_v_odin -  переменная отвечающая за результат клика
    '''
    mx = event.pos[0]
    my = event.pos[1]
    popadanie_hot_v_odin = False
    for ball in current_balls:
        x = ball[0]
        y = ball[1]
        r = ball[2]
        dest = ((mx - x) ** 2 + (my - y) ** 2) ** 0.5
        if dest <= r:
            popadanie_hot_v_odin = True
    return popadanie_hot_v_odin


def make_colors():
    '''создает список цветов'''
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    MAGENTA = (255, 0, 255)
    CYAN = (0, 255, 255)
    return [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball(COLORS):
    '''
    COLORS - список возможных цветов
    n - количество шаров в данной партии

    рисует новую партию шариков с рандомными параметрами
    и возвращает массив current_balls cо списками из 6 значений:
    x - координатаданного шара по x
    y - координатаданного шара по у
    r - радиус данного шара
    color - цвет данного шара
    speed_x - скорость по х данного шара
    speed_y - скорость по у данного шара
    '''
    n = randint(1, 4)
    current_balls = []
    for i in range(n):
        x = randint(101, 1099)
        y = randint(101, 799)
        r = randint(10, 100)
        speed_x = randint(-20, 20)
        speed_y = randint(-20, 20)
        color = COLORS[randint(0, 5)]
        circle(screen, color, (x, y), r)
        current_balls.append([x, y, r, color, speed_x, speed_y])
    return current_balls

def motion(current_balls):
    '''
    в соответствии с параметром скорости speed сдвигает каждый шарик в данной партии и возвращает
    текущие состояние системы, если шарик близок к стенке, меняет направление его скорости
    x - координатаданного шара по x
    y - координатаданного шара по у
    r - радиус данного шара
    color - цвет данного шара
    speed_x - скорость по х данного шара
    speed_y - скорость по у данного шара
    '''
    screen.fill((0, 0, 0))
    for i in current_balls:
        x = i[0]
        y = i[1]
        r = i[2]
        color = i[3]
        speed_x = i[4]
        speed_y = i[5]
        circle(screen, color, (x + speed_x, y + speed_y), r)
        i[0] = x + speed_x
        i[1] = y + speed_y
        if x > 1200 - r or x < r:
            i[4] = -1 * i[4]
            i[0] = x - 2 * speed_x
        if y > 900 - r or y < r:
            i[5] = -1 * i[5]
            i[1] = y - 2 * speed_y
    return current_balls


import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS_total = 0.1
FPS_local = 10
screen = pygame.display.set_mode((1200, 900))
COLORS = make_colors()

game(screen, COLORS, FPS_local, FPS_total)

pygame.quit()