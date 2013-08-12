from sys import argv

script, filename = argv

# check open() mode 'w'
fd = open(filename, 'w')
fd.close()
print 'mode w: ', open(filename).read()

# check open() mode 'w+'
fd = open(filename, 'w+')
fd.close()
print 'mode w+: ', open(filename).read()
