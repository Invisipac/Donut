import pygame as pg
import numpy as np
from math import sin, cos, pi



class circle:

    x: float
    y: float
    z: float
    points: list[np.array]
    rad: float
    surf: pg.Surface

    def __init__(self, center : np.array, surf: pg.Surface):
        self.x = center[0]
        self.y = center[1]
        self.z = center[2]
        self.surf = surf
        self.rad = 50
        self.points = []

    def show_center(self):
        print(self.x, self.y, self.z)

    def make_circle(self):
        for theta in range(0, 30):
            px = self.rad*cos(theta*(2*pi/30))    
            py = self.rad*sin(theta*(2*pi/30))
            self.points.append(np.array([px, py, self.z]))

    def draw_circle(self, proj_scalar = 1):
        for p in self.points:
            proj_x = p[0]*proj_scalar
            proj_y = p[1]*proj_scalar
            pg.draw.circle(self.surf, (0, 0, 0), (self.x + proj_x, self.y + proj_y), 2) 
    
    def rotate_circle(self, theta, axis=0):
        rotation_yaxis = np.array([[cos(theta), 0, sin(theta)], 
                                   [0, 1, 0], 
                                   [-sin(theta), 0, cos(theta)]])
        
        for i in range(len(self.points)):
            self.points[i] = np.matmul(rotation_yaxis, self.points[i])



# c = np.array([300, 400])
