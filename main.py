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
BLACK = (0, 0, 0)
AXIS = np.array([2, 5, 7])
AXIS = AXIS/np.linalg.norm(AXIS)


T = Torus(np.array([50, 50, 0]))
T.make_torus()
DIST_TO_SCREEN = 400 #(W/2)*(DIST_TO_CENTER - (t.rad + np.linalg.norm(t.center)))/((t.rad + np.linalg.norm(t.center)))
screen = Screen(DIST_TO_CENTER, DIST_TO_SCREEN, np.array([W/2, H/2]), (W, H))


run = True
screen.display.fill(BLACK)



while run:
    for e in pg.event.get(eventtype=pg.QUIT):
        if e is not None:
            run = False

    T.rotate_torus(pi/(FRAMES), 'x')
    T.rotate_around_certain_axis(AXIS, pi/(FRAMES))
    T.rotate_torus(pi/(2*FRAMES), 'y')
    
    screen.draw_object(T.points)

    pg.display.update()
    CLOCK.tick(FRAMES)
    screen.display.fill(BLACK)

pg.quit()