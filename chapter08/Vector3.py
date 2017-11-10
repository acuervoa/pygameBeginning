from math import sqrt

class Vector3(object):

    def __init__(self, x, y, z):

        self.x = x
        self.y = y
        self.z = z

    def __add__(self, x, y, z):

        return Vector3(self.x + x, self.y + y, self.z + z)

    def get_magnitude(self):

        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    
