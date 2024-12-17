import pygame as pg
import numpy as np
from math import sin, cos, pi
from test_donut import Circle


class Torus:
    points: list[np.ndarray]
    rad: float
    center: np.array
    def __init__(self, center: np.array, ):
        self.center = center
        self.rad = 100
        self.points = []

    def make_torus(self):
        for theta in range(30):
            pass
    
    def draw_torus(self, surf):
        for circ in self.circles:
            circ.draw_circle(surf)
