""" exercise 2
You look at the clock and it is exactly 2pm. 
You set an alarm to go off in 51 hours. 
At what time does the alarm go off?

current_time = 14
hour = (51 + current_time) / 24
minutes = (51 + current_time) % 24

print "The alarm goes off at %d:%d" % (hour, minutes)
"""
""" exercise 3
Write a Python program to solve the general version of the above problem. 
Ask the user for the time now (in hours), and ask for the number of hours 
to wait. Your program should output what the time will be on the clock when 
the alarm goes off.

time = input("What time is it now (in hours)?: ")
alarm = input("Please input the number of hours to wait: ")

hour = (time + alarm) % 24

print "The alarm goes off at %d:00" % (hour)
"""
""" exercise 4
You go on a wonderful holiday leaving on day number 3 (a Wednesday). 
You return home after 137 nights. Write a general version of the program 
which asks for the starting day number, and the length of your stay, and 
it will tell you the number of day of the week you will return on.

leaving_day = input("Starting day number?: ")
length_of_stay = input("Length of your stay?: ")
return_day = (leaving_day + length_of_stay) % 7

print "You will return on day number %d" % return_day
"""
""" exercise 5
Take the sentence: All work and no play makes Jack a dull boy. 
Store each word in a separate variable, then print out 
the sentence on one line using print.

str = 'All work and no play makes Jack a dull boy.'
words = str.split()
print words
"""
""" exercise 6
Add parenthesis to the expression 6 * 1 - 2 to change its value from 4 to -6.

print 6 * (1 - 2)
"""
""" exercise 7

The formula for computing the final amount if one is 
earning compound interest is given on Wikipedia as
formula for compound interest

Write a Python program that assigns the principal amount of 10000 to 
variable P, assign to n the value 12, and assign to 
r the interest rate of 8% (0.08). Then have the program prompt the user 
for the number of years, t, that the money will be compounded for. 
Calculate and print the final amount after t years.

P = 10000
n = 12
r = 0.08
t = input("The number of years: ")

A = P * ((1 + r/n) ** (n * t))

print A
"""
""" exercise 8
Write a program that will compute the area of a circle. 
Prompt the user to enter the radius and print a nice message back to 
the user with the answer.

pi = 3.141592
r = input("Enter the radius: ")
area = pi * r ** 2
print "The area of a circle is %f" % area
"""
""" exercise 9
Write a program that will compute the area of a rectangle. 
Prompt the user to enter the width and height of the rectangle. 
Print a nice message with the answer.

width = input("Enter the width: ")
height = input("Enter the height: ")
area = width * height / 2.0
print "The are of a rectangle %f" % area
"""
""" exercise 10
Write a program that will compute MPG for a car. 
Prompt the user to enter the number of miles driven and 
the number of gallons used. Print a nice message with the answer.

miles = input("Enter the number of miles driven: ")
gallons = input("Enter the number of gallons used: ")
MPG = miles / gallons
print "MPG is %d" % MPG
"""
""" exercise 11
Write a program that will convert degrees celsius to degrees fahrenheit.

celsius = input("Enter the degrees celsius: ")
fahrenheit = celsius*1.8 + 32
print "Degree fahrenheit is %f" % (fahrenheit)
"""
""" exercise 12
Write a program that will convert degrees fahrenheit to degrees celsius.
"""
fahrenheit = input("Enter the degrees fahrenheit: ")
celsius = (fahrenheit - 32) / 1.8
print "Degree celsius is %f" % (celsius)
