import pygame as pg
import numpy as np
from math import pi

class Rotation:
    def __init__(self, vec: np.ndarray = np.array([1, 0, 0])):
        self.axis = vec
        self.angle = 0
        self.can_turn = True
        self.start = None
        self.perp_direction = np.array([0, 0, 0])
        self.turn_direction = np.array([0, 0, 0])
        self.end = np.array([0, 0])

    def get_axis_start(self):
        x, y = pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]
        self.start = np.array([x, y])
        self.end = np.array([self.start[0], self.start[1]])

    def check_parallel(self, vec1: np.ndarray, vec2: np.ndarray):
        newVec1 = vec1/np.linalg.norm(vec1)
        newVec2 = vec2/np.linalg.norm(vec2)

        if all(newVec1[i] == newVec2[i] for i in range(len(vec1))):
            return 1
        elif all(newVec1[i] == -newVec2[i] for i in range(len(vec1))):
            return -1
        elif all(newVec1[i] == 0 for i in range(len(vec1))) or all(newVec2[i] == 0 for i in range(len(vec1))):
            return 1
        else:
            return 0

    def get_axis(self):
        m_x, m_y = pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]

        if any((m_x, m_y)[i] != self.end[i] for i in range(2)):
            self.can_turn = True
            vec = np.subtract((m_x, m_y), self.end)
            print(vec)
            
            direction = self.check_parallel(vec, self.perp_direction)

            if  direction != 0:
                self.perp_direction = np.subtract((m_x, m_y), self.start)
                self.end = np.array([m_x, m_y])
                self.angle = (direction * pi)/30
            else:
                self.start = np.array([self.end[0], self.end[1]])
                self.perp_direction = vec


            self.axis = np.array([-self.perp_direction[1], self.perp_direction[0], 0])
            self.axis = self.axis/np.linalg.norm(self.axis)
        else:
            self.can_turn = False

        # print(self.start, self.end, self.axis)
    


