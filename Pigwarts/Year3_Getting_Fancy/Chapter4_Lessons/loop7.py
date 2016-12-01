#
# Print multiples of 4s up to 20
# Then print powers of 2 up to 32
#
# Hint 1: Do the first part and then the second
# Hint 2: For powers of 2 a good approach is to use an extra variable that
#	will keep getting bigger.

'''
Make the output look exactly like

4
8
12
16
20
---
1
2
4
8
16
32

'''

import random

number = 0

for i in range (5):
	number = number + 4
	print number

print "---"

number = 1
for i in range(6):
	print number
	number = number * 2




print ""
print "Alternate way"
print "---"

for i in range (1, 6):
	print i * 4

print "---"

for i in range (6):
	print 2 ** i
