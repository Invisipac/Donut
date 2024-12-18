import pygame as pg
import numpy as np

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

    def draw_object(self, points: list[np.array], k=10):
        for p in points:
            proj_factor = self.dist_to_viewer/(self.dist_to_viewer + self.dist_to_center - p[2])
            projected_point = proj_factor*np.array([p[0], -p[1]])
            pg.draw.circle(self.display, (255, 255, 255), np.add(self.pos, projected_point), 5) 
            

    

        