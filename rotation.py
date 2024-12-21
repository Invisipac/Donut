import pygame as pg
import numpy as np


class Rotation:
    def __init__(self, vec: np.ndarray = None):
        self.axis = vec
        self.angle = 0
        self.start = None
        self.end = np.array([-1, -1])

    def get_axis(self):
        m_x, m_y = pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]

        if self.start is None:
            self.start = np.array([m_x, m_y])
        
        self.end = np.array([m_x, m_y])

        vec = np.subtract(self.end, self.start)

        self.axis = np.array([-vec[1], vec[0]])


