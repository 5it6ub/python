""" exercise 1
Write a program that prints We like Python's turtles! 1000 times.

for i in range(1000):
  print "We like Python's turtles!"
"""
""" exercise 2
Give three attributes of your cellphone object. 
Give three methods of your cellphone.
"""
# icon, sounds, shape
# click icon, make sounds, chat

""" exercise 3
Write a program that uses a for loop to print

    One of the months of the year is January
    One of the months of the year is February
    One of the months of the year is March
    etc ...

for month in ['January', 'Februrary', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']:
  print 'One of the months of the year is %s' % (month)
"""
""" exercise 4
Assume you have the assignment xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

    Write a loop that prints each of the numbers on a new line.
    Write a loop that prints each number and its square on a new line.

xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for i in xs:
  print 'number: ', i, ' its square: ', i*i
"""
""" exercise 5
Use for loops to make a turtle draw these regular polygons 
(regular means all sides the same lengths, all angles the same):

    An equilateral triangle
    A square
    A hexagon (six sides)
    An octagon (eight sides)

import turtle
wn = turtle.Screen()

triangle = turtle.Turtle()
triangle.color("blue")
for i in range(3):
  triangle.forward(100)
  triangle.left(120)

square = turtle.Turtle()
square.color('red')
for i in range(4):
  square.forward(80)
  square.left(90)

hexagon = turtle.Turtle()
hexagon.color('green')
for i in range(6):
  hexagon.forward(50)
  hexagon.left(60)

octagon = turtle.Turtle()
octagon.color('purple')
for i in range(8):
  octagon.forward(30)
  octagon.left(45)

wn.exitonclick()
"""
""" exercise 6
A drunk pirate makes a random turn and then takes 100 steps forward, 
makes another random turn, takes another 100 steps, turns another 
random amount, etc. A social science student records the angle of 
each turn before the next 100 steps are taken. Her experimental data 
is [160, -43, 270, -97, -43, 200, -940, 17, -86]. (Positive angles are 
counter-clockwise.) Use a turtle to draw the path taken by our drunk friend.

import turtle

wn = turtle.Screen()
drunk = turtle.Turtle()
for angle in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
  drunk.left(angle)
  drunk.forward(100)

wn.exitonclick()
"""
""" exercise 7
Enhance your program above to also tell us what the drunk pirate's heading
is after he has finished stumbling around.

import turtle

wn = turtle.Screen()
drunk = turtle.Turtle()
for angle in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
  drunk.left(angle)
  drunk.forward(100)
print drunk.heading()

wn.exitonclick()
"""
""" exercise 12
Create a turtle, and assign it to a variable. When you print its type,

    what do you get?

import turtle
instance_1 = turtle.Turtle()
print type(instance_1)
"""
""" exercise 13
Write a program to draw a Sprite where the number of legs is provided by 
the user.
"""
import turtle
legs = input("Enter the number of legs: ")
wn = turtle.Screen()
sprite = turtle.Turtle()
for i in range(360):
  sprite.forward(1)
  sprite.left(1)
sprite.right(45)
for i in range(legs):
  sprite.forward(40)
  sprite.up()
  sprite.backward(40)
  sprite.down()
  sprite.right(90/(legs-1))
wn.exitonclick()
