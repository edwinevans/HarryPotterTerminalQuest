#
# Keep printing random numbers until you find one less than 0.1
# Then print "Eurika!" and exit
#
# You can review earlier examples but try to create the whole program yourself without 
# any hints
#

import random

while True:
	number = random.random()
	print number
	if number < 0.1:
		print "Eurika!"
		break