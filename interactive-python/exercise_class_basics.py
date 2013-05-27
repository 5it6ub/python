""" exercise 1
Rewrite the distance function from chapter 5 so that it takes two Points as parameters instead of four numbers.

import math

class Point:
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

def distance(point1, point2):
    xdiff = point2.getX() - point1.getX()
    ydiff = point2.getY() - point1.getY()

    dist = math.sqrt(xdiff**2 + ydiff**2)
    return dist

p = Point(4,3)
q = Point(0,0)
print(distance(p,q))
print p
print q
"""
""" exercise 2
Add a method reflect_x to Point which returns a new Point, one which is the reflection of the point about the x-axis. For example, Point(3, 5).reflect_x() is (3, -5)

import math

class Point:
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

def distance(point1, point2):
    xdiff = point2.getX() - point1.getX()
    ydiff = point2.getY() - point1.getY()

    dist = math.sqrt(xdiff**2 + ydiff**2)
    return dist

def reflect_x(point):
    return Point(point.getX(), -point.getY())
    
p = Point(4,3)
q = Point(0,0)
print distance(p,q)
print p
print q
print reflect_x(p)
print reflect_x(q)
"""
""" exercise 3
Add a method slope_from_origin which returns the slope of the line joining the origin to the point.

import math

class Point:
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

    def slope_from_origin(self):
        try:
            return self.y / self.x
        except ZeroDivisionError:
            print "ZeroDivisionError occurred"
            return 0

def distance(point1, point2):
    xdiff = point2.getX() - point1.getX()
    ydiff = point2.getY() - point1.getY()

    dist = math.sqrt(xdiff**2 + ydiff**2)
    return dist

def reflect_x(point):
    return Point(point.getX(), -point.getY())
    
p = Point(4.0,3.0)
q = Point(0,0)
print distance(p,q)
print p
print q
print reflect_x(p)
print reflect_x(q)
print p.slope_from_origin()
print q.slope_from_origin()
"""
""" exercise 4
The equation of a straight line is 'y = ax + b', (or perhaps 'y = mx + c'). The coefficients a and b completely describe the line. Write a method in the Point class so that if a point instance is given another point, it will compute the equation of the straight line joining the two points. It must return the two coefficients as a tuple of two values.
"""
import math

class Point:
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

    def get_line_to(self,point):
        # y = ax + b --> b = y_1 - a*x_1
        # y = a*x + y_1 - a*x_1
        a = (self.getY()-point.getY()) / (self.getX()-point.getX())
        b = self.getY() - a*self.getX()
        coefficients = a, b
        return coefficients
        
print Point(4,11).get_line_to(Point(6,15)) # return (2,3)

""" exercise 5
Given four points that fall on the circumference of a circle, find the midpoint of the circle.
"""
0,0    sqrt(abs(x-0)**2 + abs(y-0)**2)
2,0
1,1
-1,-1
