import pygame as pg
import numpy as np
from math import sin, cos, pi
from test_donut import Circle


class Torus:
    points: list[np.ndarray]
    rad: float
    center: np.array
    def __init__(self, center: np.array):
        self.center = center
        self.rad = 100
        self.points = []
        self.num_circles = 100

    def make_torus(self):
        root_circle = Circle(20, self.center + self.rad)
        root_circle.make_circle()
        for theta in range(self.num_circles):
            self.points.extend(root_circle.points)
            root_circle.rotate_circle(theta*(2*pi/self.num_circles))
    
    def rotate_torus(self, theta, axis='x'):
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
    # def draw_torus(self, surf):
    #     for circ in self.circles:
    #         circ.draw_circle(surf)
