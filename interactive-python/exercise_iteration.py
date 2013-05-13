""" exercise 2
Write a function print_triangular_numbers(n) that prints out the first n triangular numbers. A call to print_triangular_numbers(5) would produce the following output:

1       1
2       3
3       6
4       10
5       15


def print_triangular_numbers(n):
  return 0.5*n*(n+1)

for i in range(1, 6):
  print print_triangular_numbers(i)
"""
""" exercise 3
Write a function, is_prime, which takes a single integer argument and returns True when the argument is a prime number and False otherwise.

def is_prime(n):
  if n == 1 or n == 2 or n == 3:
    return True
  elif n%2 != 0 and n%3 != 0:
    return True
  else:
    return False

for i in range(1,15):
  print '%d: %s' % (i, is_prime(i))
"""
""" exercise 4
Modify the the Random turtle walk program so that the turtle turns around when it hits the wall and goes the other direction. This bouncing off the walls should continue until the turtle has hit the wall 4 times.

import turtle
import random
import math

def go_turtle(obj, init_heading, max_w, max_h):
  heading = init_heading
  obj.setheading(heading)
  hit_wall_count = 0
  while hit_wall_count < 5:
    x, y = obj.position()
    if abs(x) >= max_w/2 or abs(y) >= max_h/2:
#      print 'x, y, max_w/2, max_h/2, heading', x, y, max_w/2, max_h/2, heading
      heading = (heading+150)%360
      obj.setheading(heading)
      hit_wall_count += 1
    obj.forward(1)
    
def main():
  wn = turtle.Screen()
  t = turtle.Turtle()
  t.shape("turtle")
  t.up()
  wn_w, wn_h = 400, 300
  wn.screensize(wn_w, wn_h)
#  print wn_w, wn_h
  angle = random.randint(0, 360)
#  print angle
  go_turtle(t, angle, wn_w, wn_h)

  wn.exitonclick()

if __name__ == '__main__':
  main()

"""
""" exercise 5
Modify the previous program so that you have two turtles each with a random starting location. Keep the turtles moving and bouncing off the walls until they collide with each other.

import turtle
import random
import math

def go_turtle(obj, obj2, init_heading, init_heading2, max_w, max_h):
  heading = init_heading
  heading2 = init_heading2
  obj.setheading(heading)
  obj2.setheading(heading2)

  x, y = obj.position()
  x2, y2 = obj2.position()
  while int(x) != int(x2) or int(y) != int(y2):
    if abs(x) >= max_w/2 or abs(y) >= max_h/2:
      heading = (heading+150)%360
      obj.setheading(heading)
    if abs(x2) >= max_w/2 or abs(y2) >= max_h/2:
      heading2 = (heading2+150)%360
      obj2.setheading(heading2)

    obj.forward(1)
    obj2.forward(1)
    x, y = obj.position()
    x2, y2 = obj2.position()

  print "collide @ (%d, %d) (%d, %d)" % (x, y, x2, y2)
    
def main():
  wn = turtle.Screen()
  wn_w, wn_h = 10, 10
  wn.screensize(wn_w, wn_h)
#  print wn_w, wn_h

  t = turtle.Turtle()
  t.shape("turtle")
#  t.pencolor("lightgreen")
  t.fillcolor("lightgreen")
  t.up()
  pos_x = random.randint(0, wn_w/2)
  pos_y = random.randint(0, wn_h/2)
  t.setposition(pos_x, pos_y)

  t2 = turtle.Turtle()
  t2.shape("turtle")
#  t2.pencolor("purple")
  t2.fillcolor("purple")
  t2.up()

pos_x = random.randint(0, wn_w/2)
  pos_y = random.randint(0, wn_h/2)
  t2.setposition(pos_x, pos_y)

  angle = random.randint(0, 360)
  angle2 = random.randint(0, 360)
#  print angle
  go_turtle(t, t2, angle, angle2, wn_w, wn_h)

  wn.exitonclick()

if __name__ == '__main__':
  main()
"""
""" exercise 6
Modify the previous program so that rather than a left or right turn the angle of the turn is determined randomly at each step. When the turtle hits the wall you must calculate the correct angle for the bounce.
"""
import turtle
import random
import math

def set_heading_x(n):
  if n <= 90:
    angle = 180 - n
  elif 90 < n and n <= 180:
    angle = 180 - n
  elif 180 < n and n <= 270:
    angle = 540 - n
  else:
    angle = 540 - n

  return angle

def set_heading_y(n):
  if n <= 90:
    angle = 360 - n
  elif 90 < n and n <= 180:
    angle = 360 - n
  elif 180 < n and n <= 270:
    angle = 360 - n
  else:
    angle = 360 - n

  return angle

def go_turtle(obj, obj2, init_heading, init_heading2, max_w, max_h):
  heading = init_heading
  heading2 = init_heading2
  obj.setheading(heading)
  obj2.setheading(heading2)

  x, y = obj.position()
  x2, y2 = obj2.position()
  while int(x) != int(x2) or int(y) != int(y2):
    if abs(x) >= max_w/2:
      heading = set_heading_x(heading)
      obj.setheading(heading)
    elif abs(y) >= max_h/2:
      heading = set_heading_y(heading)
      obj.setheading(heading)

    if abs(x2) >= max_w/2:
      heading2 = set_heading_x(heading2)
      obj2.setheading(heading2)
    elif abs(y2) >= max_h/2:
      heading2 = set_heading_y(heading2)
      obj2.setheading(heading2)

    obj.forward(1)
    obj2.forward(1)
    x, y = obj.position()
    x2, y2 = obj2.position()

  print "collide @ (%d, %d) (%d, %d)" % (x, y, x2, y2)
    
def main():
  wn = turtle.Screen()
  wn_w, wn_h = 100, 100
  wn.screensize(wn_w, wn_h)
#  print wn_w, wn_h

  t = turtle.Turtle()
  t.shape("turtle")
#  t.pencolor("lightgreen")
  t.fillcolor("lightgreen")
  t.up()
  pos_x = random.randint(0, wn_w/2)
  pos_y = random.randint(0, wn_h/2)
  t.setposition(pos_x, pos_y)

  t2 = turtle.Turtle()
  t2.shape("turtle")
#  t2.pencolor("purple")
  t2.fillcolor("purple")
  t2.up()

  pos_x = random.randint(0, wn_w/2)
  pos_y = random.randint(0, wn_h/2)
  t2.setposition(pos_x, pos_y)

  angle = random.randint(0, 360)
  angle2 = random.randint(0, 360)
#  print angle
  go_turtle(t, t2, angle, angle2, wn_w, wn_h)

  wn.exitonclick()

if __name__ == '__main__':
  main()
