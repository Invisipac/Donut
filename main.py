import pygame as pg

pg.init()

W, H = 800, 600
CLOCK = pg.time.Clock()
pg.display.set_mode((W, H))

run = True

while run:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False

    pg.display.update()
    CLOCK.tick(60)

pg.quit()