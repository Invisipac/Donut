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
        self.root_circle = Circle(20, np.array([self.rad, 0, 0]))
        self.root_circle.make_circle()

    def make_torus(self):
        for theta in range(self.num_circles + 1):
            self.points.extend(self.root_circle.points)
            self.root_circle.rotate_circle(theta*(2*pi/self.num_circles))
        
        for i in range(len(self.points)):
            self.points[i] = np.add(self.points[i], self.center)
    
    def find_normal(self, point: int):
        points = [
            self.points[(point + 1)%self.root_circle.num_points],
            self.points[(point - 1)%self.root_circle.num_points],
            self.points[(point + self.root_circle.num_points)%self.num_circles],
            self.points[(point - self.root_circle.num_points)%self.num_circles],
        ]
        v1 = np.subtract(points[0], points[1])
        v2 = np.subtract(points[2], points[3])
        norm = np.cross(v1, v2)
        return norm
    
    def illuminate_torus(self):
        for p in self.points:
            norm = self.find_normal(p)
            light = np.array([0, 0, -1])
            illumination = np.dot(norm, light)

            # if 

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
