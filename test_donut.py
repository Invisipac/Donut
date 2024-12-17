import pygame as pg
import numpy as np
from math import sin, cos, pi



class Circle:

    x: float
    y: float
    z: float
    center: np.array
    points: list[np.array]
    rad: float
    num_points: float

    def __init__(self, center: np.array):
        self.x = center[0]
        self.y = center[1]
        self.dist_from_view = center[2] + 90
        self.screen_center = np.array([self.x, self.y])
        self.center = center
        self.rad = 90
        self.points = []
        self.num_points = 50

    def show_center(self):
        print(self.x, self.y, self.z)

    def make_circle(self):
        for theta in range(0, self.num_points):
            px = 90+self.rad*cos(theta*(2*pi/self.num_points))    
            py = self.rad*sin(theta*(2*pi/self.num_points))
            self.points.append(np.array([px, py, 0]))

    def draw_circle(self, surf: pg.Surface, dist_to_screen = 100):
        for p in self.points:
            proj_scalar = dist_to_screen/(p[2] + self.dist_from_view + dist_to_screen)
            # print(dist_to_screen, p[2], proj_scalar)
            proj_p = np.array([p[0]*proj_scalar, 
                               p[1]*proj_scalar])
            
            pg.draw.circle(surf, (0, 0, 0), np.add(self.screen_center, proj_p), 2) 
    
    def rotate_circle(self, theta, axis='y'):
        match axis:
            case 'x':
                rotation_axis = np.array([[1, 0, 0],
                                          [0, cos(theta), -sin(theta)],
                                          [0, sin(theta), cos(theta)]])
            case 'y':
                rotation_axis = np.array([[cos(theta), 0, sin(theta)], 
                                   [0, 1, 0], 
                                   [-sin(theta), 0, cos(theta)]])
            case 'z':
                rotation_axis = np.array([[cos(theta), -sin(theta), 0], 
                                   [sin(theta), cos(theta), 0], 
                                   [0, 0, 1]])
        
        
        for i in range(len(self.points)):
            self.points[i] = np.matmul(rotation_axis, self.points[i])
    



# c = np.array([300, 400])
