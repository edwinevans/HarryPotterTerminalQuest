import random

while True:
	# print a random number
	number = random.random()
	print number
	if number > 0.9:
		break
print "done"
# Use if, while, and break to keep printing random numbers until you get
# one larger than 0.9 and then exit
#
# Hint: To start, try just printing random numbers forever.