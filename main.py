import pygame as pg
import test_donut as td
import numpy as np
from math import pi
from torus import Torus
from viewer import Screen
from button import Button
from rotation import Rotation
pg.init()

W, H = 800, 600
DIST_TO_CENTER = 50
FRAMES = 60
CLOCK = pg.time.Clock()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCREEN = pg.display.set_mode((W, H))

T = Torus(np.array([0, 0, 0]))
T.make_torus()
DIST_TO_SCREEN = 400 #(W/2)*(DIST_TO_CENTER - (t.rad + np.linalg.norm(t.center)))/((t.rad + np.linalg.norm(t.center)))
screen = Screen(DIST_TO_CENTER, DIST_TO_SCREEN, np.array([W/2, H/2]), (W, H))
B = Button(pg.Rect(50, 50, 40, 25))


run = True
spin_torus = True

rotation = Rotation()
axis = np.array([2, 5, 7])
axis = axis/np.linalg.norm(axis)

screen.display.fill(BLACK)



while run:
    for e in pg.event.get(eventtype=[pg.QUIT, pg.MOUSEBUTTONDOWN, pg.MOUSEBUTTONUP]):
        if e.type == pg.QUIT:
            run = False
        elif e.type == pg.MOUSEBUTTONDOWN:
            rotation.get_axis_start()
            print('a')
            if B.press_or_release_button() and B.release_press:
                B.set_button_pressed_down(True)
                B.set_button_release(False)
                spin_torus = not spin_torus
        elif e.type == pg.MOUSEBUTTONUP:
            if B.press_or_release_button and B.press_down:
                B.set_button_release(True)
                B.set_button_pressed_down(False)
        
    if any(pg.mouse.get_pressed()):
        
        rotation.get_axis()
        if not spin_torus and rotation.can_turn:
            T.rotate_around_certain_axis(rotation.axis, rotation.angle)    
    B.draw_button(screen.display)
    if spin_torus:
        # T.rotate_torus(pi/(FRAMES), 'x')
        T.rotate_around_certain_axis(rotation.axis, pi/(FRAMES))
        # T.rotate_torus(pi/(2*FRAMES), 'y')
    

    T.draw_torus(SCREEN, DIST_TO_SCREEN, DIST_TO_CENTER)

    pg.display.update()
    CLOCK.tick(FRAMES)
    screen.display.fill(BLACK)

pg.quit()