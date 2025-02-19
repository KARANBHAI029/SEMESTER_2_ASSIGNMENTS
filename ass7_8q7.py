import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mag(self):
        return math.sqrt(self.x**2 + self.y**2)

    def rot(self):
        return math.atan2(self.y, self.x)

    def dist(self, o):
        return math.sqrt((self.x - o.x)**2 + (self.y - o.y)**2)

class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def mag(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

v1 = Vector2D(3, 4)
v2 = Vector3D(1, 2, 3)
print(v1.mag(), v2.mag())
