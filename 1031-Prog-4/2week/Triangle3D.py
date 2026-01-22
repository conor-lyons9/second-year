#!/usr/bin/env python3

import math

class Dot3D:
    def __init__(self, x, y, z, label=None):
        self.x = x
        self.y = y
        self.z = z
        self.label = label

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + 
                    (self.y - other.y)**2 +
                    (self.z - other.z)**2)

    def add_vector(self, other):
        newX = self.x + other.x
        newY = self.y + other.y
        newZ = self.z + other.z

        newLabel = self.label + "+" + other.label
        return Dot3D(newX, newY, newZ, newLabel)

# Task 2
class Triangle3D:
    def __init__(self, dot1, dot2, dot3):
        self.dot1 = dot1
        self.dot2 = dot2
        self.dot3 = dot3

    def calculate_perimeter(self):
        edge1 = self.dot1.distance_to(self.dot2)
        edge2 = self.dot1.distance_to(self.dot3)
        edge3 = self.dot2.distance_to(self.dot3)
        return edge1 + edge2 + edge3

    def calculate_area(self):
        edge1 = self.dot1.distance_to(self.dot2)
        edge2 = self.dot1.distance_to(self.dot3)
        edge3 = self.dot2.distance_to(self.dot3)

        s = (edge1 + edge2 + edge3) / 2 # s = semi-perimeter
        area = math.sqrt(s * (s - edge1) * (s - edge2) * (s - edge3))
        return area

