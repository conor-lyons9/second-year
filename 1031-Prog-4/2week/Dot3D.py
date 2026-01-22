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

