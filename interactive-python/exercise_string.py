""" exercise 1
What is the result of each of the following:

print 'Python'[1]
print "Strings are sequences of characters."[5]
print len("wonderful")
print 'Mystery'[:4]
print 'p' in 'Pineapple'
print 'apple' in 'Pineapple'
print 'pear' not in 'Pineapple'
print 'apple' > 'pineapple'
print 'pineapple' < 'Peach'
"""

""" exercise 1
Write a function which removes all punctuation from string and counts the number of words in your text that contain the letter 'e'. Your program should print an analysis of the text like this:

Your text contains 243 words, of which 109 (44.8%) contain an 'e'.

import string

sherlock_homes_quote = '''
How often have I said to you that when you have eliminated the impossible, whatever remains, however improbable, must be the truth?
'''
word_count = 0
e_count = 0
words = ""
quote = ""
ratio = 0.0

for c in sherlock_homes_quote:
    if c not in string.punctuation:
        quote += c
        
words = string.split(quote, ' ')
word_count = len(words)

for word in words:
    if 'e' in word:
        e_count += 1

ratio = (1.0*e_count/word_count)*100
#print 'words = ', words
#print 'word_count = %d' % word_count
#print 'e_count = %d' % e_count
print 'quote = ', quote
#print 'ratio = %2.2f%%' % (ratio)

print 'Your text contains %d words, of which %d (%2.2f%%) contain an 'e'.' % (word_count, e_count, ratio)
"""
""" exercise 2
Print out a neatly formatted multiplication table, up to 12 x 12.
"""
for x in xrange(1,13):
    for y in xrange(1,13):
        print '%5d' % (x*y),
    print '\n'

