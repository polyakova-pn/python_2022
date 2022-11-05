import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

screen.fill((255, 255, 255))
circle(screen, (0, 0, 0), (200, 175), 152)
circle(screen, (255, 255, 0), (200, 175), 150)


circle(screen, (255, 0, 0), (150, 130), 30)
circle(screen, (0, 0, 0), (150, 130), 10)

circle(screen, (255, 0, 0), (250, 130), 18)
circle(screen, (0, 0, 0), (250, 130), 6)

polygon(screen, (0, 0, 0), [(90,80),(90+5,80-15),(180+5,110 - 15),(180,110)])
polygon(screen, (0, 0, 0), [(400-90,80),(400-90-5,80-15),(400-180-5,110 - 15),(400-180,110)])

polygon(screen, (0, 0, 0), [(120,250),(120,220),(280,220),(280,250)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()