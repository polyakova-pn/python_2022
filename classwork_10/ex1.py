import math
from random import choice
import pygame
import numpy as np
from random import randint

FPS = 300
RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
WIDTH = 800
HEIGHT = 600

class Ball:

    def __init__(self, screen: pygame.Surface, x=40, y=560):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30
        self.kolud = 0

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600) + замедление при ударах.
        """
        if self.kolud < 10:
            self.x += self.vx
            self.y -= self.vy
            self.vy -= 0.025
            if self.x > 800 - self.r:
                self.x = 800 - self.r
                self.vx = -0.8 * self.vx
                self.vy = 0.8 * self.vy
            if self.y > 600 - self.r:
                self.y = 600 - self.r
                self.vy = -0.5 * self.vy
                self.vx = 0.8 * self.vx
                self.kolud += 1
        else:
            self.y = 600 - self.r
            return 1
        return 0

    def draw(self):
        '''
        рисует шарик с заданными параметрами радиуса, цвета и коордиаты
        '''
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        dist = ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) ** 0.5
        if dist < (self.r + obj.r):
            return True
        return False

class Gun:

    def __init__(self, screen):
        '''
         f2_power - начальная сила выстрела
         f2_on - нажата ли лкм (нет)
         an - начальный угол
         lenth - начальная длина
        '''
        self.screen = screen
        self.f2_power = 1
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.lenth = 20

    def fire2_start(self):
        self.f2_on = 1

    def loading(self):
        '''
        удлинняет прибор
        '''
        if self.f2_on == 1 and self.lenth < 60:
            self.lenth += 0.05

    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        создает новый мяч new_ball с параметрами, зависящами от силы выстрела f2_power и угла наклона пушки an
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 1
        self.lenth = 20
        target.hit()

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши.
        Высчитывает угол наклона пушки an в зависимости от положения мыши
        """
        if event:
            delta_x = event.pos[0] + 1
            delta_y = 600 - event.pos[1] + 1
            self.an = math.atan(delta_y / delta_x)

    def draw(self, screen):
        '''
        рисует пушку (прямоугольник) в зависимости от угла прицеливания аn
        '''
        x_end = 40 + self.lenth * np.cos(float(self.an))
        y_end = 560 - self.lenth * np.sin(float(self.an))
        pygame.draw.line(screen, self.color, (40, 560), (x_end, y_end), width=12)
        pass

    def power_up(self):
        '''
        увиличивает мощность выстрела на 1%, если зажата лкм
        '''
        if self.f2_on:
            if self.f2_power < 10:
                self.f2_power += 0.01
            self.color = RED
        else:
            self.color = GREY


class Target:

    def __init__(self):
        '''
        points - количество попыток попасть в данную цель
        vx - скорость по х
        vy - скорость по у
        '''
        self.points = 0
        self.new_target()
        self.screen = screen
        self.vx = randint(-3, 0)
        self.vy = randint(-3, 0)

    def text(self):
        '''
        формирует текст сообщения о попадании по мишени
        points количество выстрелов по данной мишени
        :return: текст сообщения
        '''
        s = 'вы попали за ' + str(self.points) + ' BULLET'
        f1 = pygame.font.Font(None, 30)
        text1 = f1.render(s, True, (0, 0, 0))
        return text1

    def move(self):
        """Переместить мишень по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y -= self.vy
        if self.x > 800 - self.r:
            self.x = 800 - self.r
            self.vx = -1 * self.vx
        if self.y > 600 - self.r:
            self.y = 600 - self.r
            self.vy = -1 * self.vy
        if self.x < self.r:
            self.x = self.r
            self.vx = -1 * self.vx
        if self.y < self.r:
            self.y = self.r
            self.vy = -1 * self.vy

    def new_target(self):
        """ Инициализация новой цели.
        x, y - случайные координаты
        r - случайный радиус
        color - цвет
        """
        self.x = randint(600, 780)
        self.y = randint(300, 550)
        self.r = randint(2, 50)
        self.color = RED

    def hit(self):
        """
        счетчик выстрелов
        points - количество выстрелов
        :return:
        """
        self.points += 1

    def draw(self):
        '''
        рисует мишень с заданными для нее параметрами х, у и color
        '''
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), self.r * 2 / 3)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
clock = pygame.time.Clock()
gun = Gun(screen)
target1 = Target()
target2 = Target()
targets = [target1, target2]
finished = False
text_showen = 0

while not finished:
    clock.tick(FPS)
    screen.fill(WHITE)
    gun.draw(screen)
    for target in targets:
        target.draw()
    for b in balls:
        b.draw()
    gun.loading()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start()
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
    for target in targets:
        target.move()
    for b in balls:
        delete_this_ball = b.move()
        for target in targets:
            if b.hittest(target):
                text_showen = 1
                text_to_write = target.text()
                target.live = 0
                target.hit()
                targets.remove(target)
                balls.remove(b)
                new_target = Target()
                targets.append(new_target)
        if delete_this_ball:
            balls.remove(b)
    if text_showen > 0:
        screen.blit(text_to_write, (15, 50))
        text_showen += 1
    if text_showen >= 2 * FPS:
        text_showen = 0
    gun.power_up()
    pygame.display.update()

pygame.quit()
