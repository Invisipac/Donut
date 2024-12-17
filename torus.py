import pygame as pg
import numpy as np
from math import sin, cos, pi
from test_donut import Circle


class Torus:
    circles: list[Circle]
    rad: float
    center: np.array
    def __init__(self, center: np.array, ):
        self.center = center
        self.rad = 100
        self.circles = []

    def make_torus(self):
        for theta in range(30):
            circ = Circle(np.add(self.center, [100, 0]))
            circ.rotate_circle(2*pi/30, axis='y')
            self.circles.append(circ)
    
    def draw_torus(self, surf):
        for circ in self.circles:
            circ.draw_circle(surf)
