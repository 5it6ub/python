""" exercise 1
Use the drawsquare function we wrote in this chapter in a program to draw the image shown below. Assume each side is 20 units. (Hint: notice that the turtle has already moved away from the ending point of the last square when the program ends.)
"""
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
