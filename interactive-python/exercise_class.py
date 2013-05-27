""" exercise 1
Add a method area to the Rectangle class that returns the area of any instance:

r = Rectangle(Point(0, 0), 10, 5)
test(r.area(), 50)

exercise 2
Write a perimeter method in the Rectangle class so that we can find the perimeter of any rectangle instance:

r = Rectangle(Point(0, 0), 10, 5)
test(r.perimeter(), 30)

exercise 3
Write a transpose method in the Rectangle class that swaps the width and the height of any rectangle instance:

r = Rectangle(Point(100, 50), 10, 5)
test(r.width, 10)
test(r.height, 5)
r.flip()
test(r.width, 5)
test(r.height, 10)

exercise 4
Write a new method in the Rectangle class to test if a Point falls within the rectangle. For this exercise, assume that a rectangle at (0,0) with width 10 and height 5 has open upper bounds on the width and height, i.e. it stretches in the x direction from [0 to 10), where 0 is included but 10 is excluded, and from [0 to 5) in the y direction. So it does not contain the point (10, 2). These tests should pass:

r = Rectangle(Point(0, 0), 10, 5)
test(r.contains(Point(0, 0)), True)
test(r.contains(Point(3, 3)), True)
test(r.contains(Point(3, 7)), False)
test(r.contains(Point(3, 5)), False)
test(r.contains(Point(3, 4.99999)), True)
test(r.contains(Point(-3, -3)), False)
"""
class Rectangle:
    def __init__(self, point, x, y):
        self.x = x
        self.y = y
        self.point = point

    def __str__(self):
        return 'point=' + str(self.point) + ' x=' + str(self.x) + ' y=' + str(self.y)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def area(self):
        a = (self.x-self.point.getX()) * (self.y-self.point.getY())
        return a

    def perimeter(self):
        """ 2(a + b) """
        return 2*(self.x + self.y)

    def flip(self):
        tmp = self.x
        self.x = self.y
        self.y = tmp

    def contains(self, point):
        bool_x = point.getX() < self.x and point.getX() >= self.point.getX()
        bool_y = point.getY() < self.y and point.getY() >= self.point.getY()
        return bool_x and bool_y

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return 'x=' + str(self.x) + ' y=' + str(self.y)
    def getX(self):
        return self.x
    def getY(self):
        return self.y

def test(area, ans):
    print area == ans

def main():
    r = Rectangle(Point(0,0), 10, 5)
    test(r.area(), 50)
    test(r.perimeter(), 30)
    r.flip()
    test(r.getX(), 5)
    test(r.getY(), 10)

    r.flip()
    test(r.contains(Point(0, 0)), True)
    test(r.contains(Point(3, 3)), True)
    test(r.contains(Point(3, 7)), False)
    test(r.contains(Point(3, 5)), False)
    test(r.contains(Point(3, 4.99999)), True)
    test(r.contains(Point(-3, -3)), False)

if __name__ == '__main__':
    main()
