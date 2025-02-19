
class Shape:
    def area(self):
        pass
    def peri(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def area(self):
        return self.l * self.w
    def peri(self):
        return 2 * (self.l + self.w)

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r * self.r
    def peri(self):
        return 2 * 3.14 * self.r

r = Rectangle(5, 10)
c = Circle(7)
print(r.area(), r.peri())
print(c.area(), c.peri())
