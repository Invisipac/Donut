import pygame as pg
import numpy as np
from math import sin, cos, isclose, pi
from test_donut import Circle
import copy
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
        for theta in range(1, self.num_circles + 1):
            self.points.append(copy.deepcopy(self.root_circle.points))
            self.root_circle.rotate_circle(2*pi/self.num_circles)
        
        for i in range(len(self.points)):
            for j in range(len(self.points[0])):
                self.points[i][j][0] = np.add(self.points[i][j][0], self.center)
                # self.points[i][j][2] = self.find_normal(i, j)
        
        self.illuminate_torus()
    
    def find_normal(self, i: int, j: int):
        R = self.rad
        r = self.root_circle.rad
        # points = [
        #     self.points[(i - 1)%self.num_circles][j][0],
        #     self.points[(i + 1)%self.num_circles][j][0],
        #     self.points[i][(j - 1)%self.root_circle.num_points][0],
        #     self.points[i][(j + 1)%self.root_circle.num_points][0],
        # ]
        # v1 = np.subtract(points[0], points[1])
        # v1 = v1/np.linalg.norm(v1)
        # v2 = np.subtract(points[2], points[3])
        # v2 = v2/np.linalg.norm(v2)
        theta = np.arcsin(self.points[i][j][0][1]/r)
        # print(round(-self.points[i][j][0][2]/(R + r*cos(theta)), 4))
        phi = np.arcsin(round(-self.points[i][j][0][2]/(R + r*cos(theta)), 4))
        v1 = np.array([
            cos(phi)*(-r*sin(theta)),
            r*cos(theta),
            -sin(phi)*(- r*sin(theta)),
        ])
        v2 = np.array([
            -(R + r*cos(theta))*sin(phi),
            0,
            -cos(phi)*(R + r*cos(theta)),
        ])
        v1 = v1/np.linalg.norm(v1)
        v2 = v2/np.linalg.norm(v2)
        norm = np.cross(v1, v2)
        return norm
    
    def illuminate_torus(self):
        for i in range(len(self.points)):
            for j in range(len(self.points[0])):
                # norm = self.find_normal(i, j)
                light = np.array([0, 0, 1])
                illumination = np.dot(self.points[i][j][2], light)
                # if -5 < self.points[i][j][0][1] < 5:
                # print(self.points[i][j][0], illumination)
                if isclose(illumination, 0) or illumination == 0 or illumination < 0:
                    self.points[i][j][1] = 0
                else:
                    self.points[i][j][1] = 255*illumination 
                
                # print(self.points[i][j][1])

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
            for j in range(len(self.points[0])):
                self.points[i][j][0] = np.matmul(rotation_axis, self.points[i][j][0])
                self.points[i][j][2] = np.matmul(rotation_axis, self.points[i][j][2])

        self.illuminate_torus()
    # def draw_torus(self, surf):
    #     for circ in self.circles:
    #         circ.draw_circle(surf)
