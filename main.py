import pygame as pg
import test_donut as td
import numpy as np
from math import pi
from torus import Torus
from viewer import Screen

pg.init()

W, H = 800, 600
DIST_TO_CENTER = 50
FRAMES = 60
CLOCK = pg.time.Clock()
WHITE = (255, 255, 255)
c = td.Circle(100, np.array([200, 0, 0]))
c.make_circle()
DIST_TO_SCREEN = (W/2)*(DIST_TO_CENTER - (np.linalg.norm(c.pos)))/((W/2) - (c.rad + np.linalg.norm(c.pos)))
screen = Screen(DIST_TO_CENTER, DIST_TO_SCREEN, np.array([W/2, H/2]), (W, H))


t = Torus(np.array([0, 0, 0]))
t.make_torus()
# print(t.points)
run = True
screen.display.fill(WHITE)

while run:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False

    #c.rotate_circle(pi/(3*FRAMES))
    # c.draw_circle(screen, DIST_TO_SCREEN)
    #screen.draw_object(c.points)
    t.rotate_torus(pi/FRAMES, 'x')
    t.rotate_torus(pi/FRAMES, 'y')
    t.rotate_torus(pi/FRAMES, 'z')
    screen.draw_object(t.points)
    # t.draw_torus(screen)
    pg.display.update()
    CLOCK.tick(FRAMES)
    screen.display.fill(WHITE)

pg.quit()