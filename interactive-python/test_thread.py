import turtle
import thread

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
#draw_whirlpool(pen, 100)

pen2 = turtle.Turtle()
pen2.pencolor('blue')
pen2.pensize(1)
pen2.penup()
pen2.setposition(120, 0.00)
pen2.pendown()
#draw_whirlpool(pen2, 100, 91)

try:
  thread.start_new_thread(draw_whirlpool, (pen, 100))
  thread.start_new_thread(draw_whirlpool, (pen2, 100, 91))
except BaseException:
  print 'Error: unable to start thread'

wn.exitonclick()
