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
"""
""" exercise 5
In the turtle bar chart program, what do you expect to happen if one or more of the data values in the list is negative? Try it out. Change the program so that when it prints the text value for the negative bars, it puts the text below the bottom of the bar.

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

  xs = [10,30,50,70,-90,110,130,150,-170,190,200,300]
  wn.setworldcoordinates(0, min(xs)-1, len(xs)*2 + 1, max(xs)+1)
  draw_barchart(pen, xs)

  wn.exitonclick()

if __name__ == '__main__':
  main()
"""
""" exercise 6
Write a function findHypot which, given the length of two sides of a right-angled triangle, returns the length of the hypotenuse. (Hint: x ** 0.5 will return the square root, or use sqrt from the math module)

import math

def findHypot(x, y):
    print 'hypotense of right-angled triangle is ', math.hypot(x, y)

def main():
    findHypot(10, 20)

if __name__ == '__main__':
    main()
"""
""" exercise 7
Write a function called is_even(n) that takes an integer as an argument and returns True if the argument is an even number and False if it is odd.

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def main():
    print is_even(3)
    print is_even(4)

if __name__ == '__main__':
    main()
"""
""" exercise 8 & 9
Now write the function is_odd(n) that returns True when n is odd and False otherwise.
Modify is_odd so that it uses a call to is_even to determine if its argument is an odd integer.

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def is_odd(n):
    return not is_even(n)

def main():
    print is_odd(3)
    print is_odd(4)

if __name__ == '__main__':
    main()
"""
""" exercise 10
Write a function is_rightangled which, given the length of three sides of a triangle, will determine whether the triangle is right-angled. Assume that the third argument to the function is always the longest side. It will return True if the triangle is right-angled, or False otherwise.

import math

def is_rightangled(a, b, longest):
    if math.hypot(a, b) == longest:
        return True
    else:
        return False

print is_rightangled(1, 1, 2**0.5)
"""
""" exercise 11
Extend the above program so that the sides can be given to the function in any order.

import math

def is_rightangled(a, b, c):
    lists = [a, b, c]
    lists.sort()
    if math.hypot(lists[0], lists[1]) == lists[2]:
        return True
    else:
        return False

print is_rightangled(1, 2**0.5, 1)
"""
""" exercise 12
A year is a leap year if it is divisible by 4 unless it is a century that is not divisible by 400. Write a function that takes a year as a parameter and returns True if the year is a leap year, False otherwise.
"""
def is_leapyear(n):
    if n % 4 == 0 and n % 400 != 0:
        return True
    else:
        return False

print is_leapyear(2000)
print is_leapyear(1000)
print is_leapyear(1990)
print is_leapyear(2016)

""" exercise 13
Implement the Date of Easter program as described in class.
"""
