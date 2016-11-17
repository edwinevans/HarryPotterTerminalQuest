from __future__ import division
import random

print "\n"
print "Hi Mia, here's a dumb way to figure out the probability of getting more than 1 head if flipping a coin 2 times... by actually doing it instead of thinking!"
print "Can you make it more accurate? (Think Big, I am not afraid.)"
print ""

possibilities = [1,2,3,4,5,6]
num_trials = 100000

print "Roll 2 dice for " + str(num_trials) + " times and count num where product divisible by 5"
print ""

num_hits = 0
for trial in range(num_trials):
	die1 = random.choice(possibilities)
	die2 = random.choice(possibilities)
	print "Rolled: " + str(die1) + ", " + str(die2)
	if ((die1 * die2) % 5) == 0:
		num_hits = num_hits + 1
		print "num hits=" + str(num_hits)

percent_divisible_by_five = 100 * num_hits / num_trials
print "percent=" + str(percent_divisible_by_five)
