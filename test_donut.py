import pygame as pg
import numpy as np
from math import sin, cos, pi


class Circle:

    x: float
    y: float
    z: float
    points: list[list[np.ndarray, float, np.ndarray]]
    rad: float
    num_points: float
    pos: np.ndarray

    def __init__(self, rad: float, pos: np.ndarray):
        self.x, self.y, self.z = pos[0], pos[1], pos[2]
        self.pos = pos
        self.rad = rad
        self.points = []
        self.num_points = 20

    def show_center(self):
        print(self.x, self.y, self.z)

    def make_circle(self):
        for theta in range(0, self.num_points):
            px = self.pos[0] + self.rad*cos(theta*(2*pi/self.num_points))    
            py = self.pos[1] + self.rad*sin(theta*(2*pi/self.num_points))
            point = [np.array([px, py, 0]), 255, np.array([0, 0, 0])]
            point[2] = np.subtract(point[0], self.pos)
            point[2] = point[2]/np.linalg.norm(point[2])
            self.points.append(point)
            

    def draw_circle(self, surf: pg.Surface, dist_to_screen = 100):
        for p in self.points:
            proj_scalar = dist_to_screen/(p[2] + self.dist_from_view + dist_to_screen)
            # print(dist_to_screen, p[2], proj_scalar)
            proj_p = np.array([p[0]*proj_scalar, 
                               p[1]*proj_scalar])
            
            pg.draw.circle(surf, (0, 0, 0), np.add(self.screen_center, proj_p), 20) 
    
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
            self.points[i][0] = np.matmul(rotation_axis, self.points[i][0])
            self.points[i][2] = np.matmul(rotation_axis, self.points[i][2])
            
            

    



# c = np.array([300, 400])
