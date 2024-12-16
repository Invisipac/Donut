import pygame as pg
import test_donut as td
import numpy as np
from math import pi

pg.init()

W, H = 800, 600
DIST_TO_SCREEN = 10
CLOCK = pg.time.Clock()
WHITE = (255, 255, 255)
screen = pg.display.set_mode((W, H))

c = td.circle(np.array([W/2, H/2, 10]), screen)
c.make_circle()

run = True
screen.fill(WHITE)

while run:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False

    c.rotate_circle(pi/10)
    c.draw_circle(DIST_TO_SCREEN/c.z)


    pg.display.update()
    CLOCK.tick(20)
    screen.fill(WHITE)

pg.quit()