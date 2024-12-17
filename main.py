import pygame as pg
import test_donut as td
import numpy as np
from math import pi
from torus import Torus

pg.init()

W, H = 800, 600
DIST_TO_SCREEN = 250
FRAMES = 15
CLOCK = pg.time.Clock()
WHITE = (255, 255, 255)
screen = pg.display.set_mode((W, H))

c = td.Circle(np.array([W/2, H/2, 80]))
c.make_circle()
t = Torus(np.array([W/2, H/2, 80]))
run = True
screen.fill(WHITE)

while run:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False

    c.rotate_circle(pi/(2*FRAMES))
    c.draw_circle(screen, DIST_TO_SCREEN)

    # t.draw_torus(screen)

    pg.display.update()
    CLOCK.tick(FRAMES)
    screen.fill(WHITE)

pg.quit()