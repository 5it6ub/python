""" exercise 3
Write a function which is given an exam mark, and it returns a string - the grade for that mark - according to this scheme:
Let xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

Test your function by printing the mark and the grade for all the elements in this list.

def grade(scores):
  for score in scores:
    if score >= 90:
      print 'score=', score, 'grade is A'
    elif score >= 80:
      print 'score=', score, 'grade is B'
    elif score >= 70:
      print 'score=', score, 'grade is C'
    elif score >= 60:
      print 'score=', score, 'grade is D'
    else:
      print 'score=', score, 'grade is F'

def main():
  xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
  grade(xs)

if __name__ == '__main__':
  main()
"""
""" exercise 4
Modify the turtle bar chart program so that the bar for any value of 200 or more is filled with red, values between [100 and 200) are filled yellow, and bars representing values less than 100 are filled green.
"""
import turtle

def fill_color(num):
  if num >= 200:
    return 'red'
  elif num >= 100:
    return 'yellow'
  else:
    return 'green'

def draw_barchart(obj, xs):
  for x in xs:
    obj.fillcolor(fill_color(x))
    obj.begin_fill()
    obj.left(90)
    obj.forward(x)
    obj.right(90)
    obj.forward(2)
    obj.right(90)
    obj.forward(x)
    obj.left(90)
    obj.end_fill()

def main():
  wn = turtle.Screen()

  pen = turtle.Turtle()
  pen.pensize(1)
  pen.pencolor('purple')

  xs = [10,30,50,70,90,110,130,150,170,190,200,300]
  wn.setworldcoordinates(0, 0, len(xs)*2 + 1, max(xs)+1)
  draw_barchart(pen, xs)

  wn.exitonclick()

if __name__ == '__main__':
  main()
