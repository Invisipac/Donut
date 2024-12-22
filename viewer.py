import pygame as pg
import numpy as np
import torus
import button
class Screen():
    dist_to_center: float
    dist_to_viewer: float
    pos: np.array
    display: pg.Surface
    def __init__(self, dist_to_center:float, dist_to_viwer: float, pos: np.ndarray, dimension: tuple[float]):
        self.dist_to_center = dist_to_center
        self.dist_to_viewer = dist_to_viwer
        self.pos = pos
        self.display = pg.display.set_mode((dimension[0], dimension[1]))

    def draw_torus(self, t: torus.Torus, k=10):
        t.points.sort(key=lambda ring: ring[0][0][2])
        for i in range(len(t.points)):
            for j in range(len(t.points[0])):
                p = t.points[i][j]
                if p[1] != 0:
                    proj_factor = self.dist_to_viewer/(self.dist_to_viewer + self.dist_to_center - p[0][2])
                    projected_point = proj_factor*np.array([p[0][0], p[0][1]])
                    # if i == 10 and j == 5:
                    #     print(p[0], p[2])
                    #     pg.draw.circle(self.display, (255, 0, 0), np.add(self.pos, projected_point), 5)
                    print('a')
                    pg.draw.circle(self.display, (p[1], p[1], p[1]), np.add(self.pos, projected_point), 2) 

            

    

        