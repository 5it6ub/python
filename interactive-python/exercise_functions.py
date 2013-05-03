
""" exercise 1
Use the drawsquare function we wrote in this chapter in a program to draw the image shown below. Assume each side is 20 units. (Hint: notice that the turtle has already moved away from the ending point of the last square when the program ends.)

import turtle

def draw_square(t, length):
  for i in range(4):
    t.forward(20)
    t.left(90)

wn = turtle.Screen()
wn.bgcolor('lightgreen')

abe = turtle.Turtle()
abe.pencolor('pink')
abe.pensize(5)

for i in range(1, 5):
  draw_square(abe, 20)
  abe.penup()
  abe.goto(30*i,0)
  abe.pendown()

wn.exitonclick()
"""
""" exercise 2
Write a program to draw this. Assume the innermost square is 20 units per side, and each successive square is 20 units bigger, per side, than the one inside it.

import turtle

def draw_square(obj, num):
  obj.penup()
  obj.setpos(-10*num, -10*num)
  obj.pendown()

  for i in range(4):
    obj.forward(20*num)
    obj.left(90)

wn = turtle.Screen()
wn.bgcolor('lightgreen')

pen = turtle.Turtle()
pen.pencolor('purple')
pen.pensize(3)

for i in range(1, 6):
  draw_square(pen, i)

wn.exitonclick()
"""
""" exercise 3
Write a non-fruitful function drawPoly(someturtle, somesides, somesize) which makes a turtle draw a regular polygon. When called with drawPoly(tess, 8, 50), it will draw a shape like this:

import turtle

def drawPoly(obj, sides, size):
  angle = 360/sides
  for side in range(1, sides+1):
    obj.forward(size)
    obj.setheading(angle*side)

wn = turtle.Screen()
wn.bgcolor('lightgreen')

pen = turtle.Turtle()
pen.pencolor('purple')
pen.pensize(3)

drawPoly(pen, 8, 50)

wn.exitonclick()
"""
""" exercise 4
Draw this pretty pattern.

import turtle

def draw_square_and_tilt(obj, size, angle):
  for j in range(1, (360/angle)+1):
    for i in range(4):
      obj.forward(size)
      obj.left(90)
    obj.setheading(angle*j)

wn = turtle.Screen()
wn.bgcolor('lightgreen')

pen = turtle.Turtle()
pen.pencolor('blue')
pen.pensize(3)

draw_square_and_tilt(pen, 100, 18)

wn.exitonclick()
"""
""" exercise 5
The two spirals in this picture differ only by the turn angle. Draw both.

import turtle

wn = turtle.Screen()
wn.screensize(500, None, 'lightgreen')

def draw_whirlpool(obj, nums, tilt=90):
  for num in range(nums):
    obj.right(tilt)
    obj.forward(num+num)

pen = turtle.Turtle()
pen.pencolor('blue')
pen.pensize(1)
pen.penup()
pen.setposition(-120, 0.00)
pen.pendown()
draw_whirlpool(pen, 100)

pen2 = turtle.Turtle()
pen2.pencolor('blue')
pen2.pensize(1)
pen2.penup()
pen2.setposition(120, 0.00)
pen2.pendown()
draw_whirlpool(pen2, 100, 91)

wn.exitonclick()
"""
""" exercise 6
Write a non-fruitful function drawEquitriangle(someturtle, somesize) which calls drawPoly from the previous question to have its turtle draw a equilateral triangle.

import turtle

def drawPoly(obj, sides, size):
  angle = 360/sides
  for side in range(1, sides+1):
    obj.forward(size)
    obj.setheading(angle*side)

def drawEquitriangle(obj, size):
  drawPoly(obj, 3, 50)

wn = turtle.Screen()
wn.bgcolor('lightgreen')

pen = turtle.Turtle()
pen.pencolor('purple')
pen.pensize(1)

drawEquitriangle(pen, 50)

wn.exitonclick()
"""
""" exercise 7
Write a fruitful function sumTo(n) that returns the sum of all integer numbers up to and including n. So sumTo(10) would be 1+2+3...+10 which would return the value 55. Use the equation (n * (n + 1)) / 2.

def sumTo(n):
  return (n * (n + 1)) / 2

def main():
  print 'sumTo(10)=',sumTo(10)

if __name__ == '__main__':
  main()
"""
""" exercise 8
Write a function areaOfCircle(r) which returns the area of a circle of radius r. Make sure you use the math module in your solution.

import math

def areaOfCircle(r):
  return math.pi * r**2

def main():
  print 'area of circle w/ radius 1 =', areaOfCircle(1)

if __name__ == '__main__':
  main()
"""
""" exercise 9
Write a non-fruitful function to draw a five pointed star, where the length of each side is 100 units.

import turtle

def draw_star(obj, length):
  angle = 36
  obj.setheading(angle)

  for i in range(5):
    angle += 144
    obj.forward(length)
    obj.setheading(angle)

wn = turtle.Screen()
wn.bgcolor('lightgreen')

pen = turtle.Turtle()
pen.pencolor('purple')
pen.pensize(1)

draw_star(pen, 100)

wn.exitonclick()
"""
""" exercise 10
Extend your program above. Draw five stars, but between each, pick up the pen, 
move forward by 350 units, turn right by 144, put the pen down, and 
draw the next star. You'll get something like this:

import turtle

def draw_star(obj, length):
  angle = 36
  obj.setheading(angle)

  for i in range(5):
    angle += 144
    obj.forward(length)
    obj.setheading(angle)

wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.screensize(2000,2000)

pen = turtle.Turtle()
pen.pencolor('purple')
pen.pensize(1)

star_position = 144
for i in range(5):
  draw_star(pen, 100)
  pen.penup()
  pen.left(star_position)
  pen.forward(350)
  pen.pendown()
  star_position += 144

wn.exitonclick()
"""
""" exercise 11
Extend the star function to draw an n pointed star. (Hint: n must be an odd number greater or equal to 3).
"""
import turtle

def draw_star(obj, length, n):
  angle = 180.0/n
  angle2 = 180.0-angle
  obj.setheading(angle)

  for i in range(n):
    angle += angle2
    obj.forward(length)
    obj.setheading(angle)

wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.screensize(2000,2000)

pen = turtle.Turtle()
pen.pencolor('purple')
pen.pensize(1)

for i in range(3, 12, 2):
  draw_star(pen, 100, i)
  pen.penup()
  pen.setposition(100*i, 0)
  pen.pendown()

wn.exitonclick()
