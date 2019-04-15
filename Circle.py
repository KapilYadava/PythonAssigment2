class Circle:
    radius = 0

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius


c = Circle(3)
print('Radius: ' + str(c.radius))
print('Area of a Circle: ' + str(c.area()))
print('Circumference of a Circle: ' + str(c.circumference()))


class Circle:

    @staticmethod
    def area(radius):
        return 3.14 * radius * radius

    @staticmethod
    def circumference(radius):
        return 2 * 3.14 * radius


print('Radius: ' + str(3))
print('Area of a Circle: ' + str(Circle.area(3)))
print('Circumference of a Circle: ' + str(Circle.circumference(3)))
