#!/usr/local/bin/python -tt

import os
import sys

def main():
  args = sys.argv[1:]

  if not args or args[0] < 0:
    print 'usage: positive_int '
    sys.exit(1)

  """ Create simple HTML file """
  index = open('index.html', 'w')
  index.write('<html><body>\n')

  for i in range(int(args[0])+1):
    local_name = 'img%d' % i
    index.write('<img src=%s>' % (local_name))

  index.write('</body></html>\n')
  index.close()

if __name__ == '__main__':
  main()
