#!/usr/local/bin/python -tt

import sys

""" At run time, functions must be defined by the execution of a "def" before they are called. It's typical to def a main() function towards the bottom of the file with the functions it calls above it.
"""
# Function
def repeat(s, exclaim):
  """Returns the string s repeated 3 times.
  If exclaim is true, add exclamation marks.
  """

  result = s + s + s # can also use "s * 3" which is faster
  if exclaim:
    result = result + '!!!'
  return result

def main():
  """ There is another import form that looks like this: "from sys import argv, exit". That makes argv and exit() available by their short names; however, we recommend the original form with the fully-qualified names because it's a lot easier to determine where a function or attribute came from.
  """
  name = sys.argv[1]
  print 'Hello there', name

  """ This is one area where languages with a more verbose type system, like Java, have an advantage ... they can catch such errors at compile time (but of course you have to maintain all that type information ... it's a tradeoff).
  """
  if name == 'Guido':
    print repeeeat('Yay', False)
  else:
    print repeat('Woo Hoo', True)

""" call a main() function when the module is run directly, 
but not when the module is imported by some other module.
"""
if __name__ == '__main__':
  main()

""" Online Help
help(len) -- docs for the built in len function (note here you type "len" not "len()" which would be a call to the function)
help(sys) -- overview docs for the sys module (must do an "import sys" first)
dir(sys) -- dir() is like help() but just gives a quick list of the defined symbols
help(sys.exit) -- docs for the exit() function inside of sys
help('xyz'.split) -- it turns out that the module "str" contains the built-in string code, but if you did not know that, you can call help() just using an example of the sort of call you mean: here 'xyz'.foo meaning the foo() method that runs on strings
"""
