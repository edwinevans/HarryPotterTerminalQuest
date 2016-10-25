import random

print "\n"
print "Hi Mia, here's a dumb way to figure out the probability of getting more than 1 head if flipping a coin 2 times... by actually doing it instead of thinking!"
print "Can you make it more accurate? (Think Big, I am not afraid.)"
print ""

possibilities = ['HEADS', 'TAILS']
num_trials = 1000
num_flips = 2

print "Flip a coin for " + str(num_flips) + " times and count result and then do this " + str(num_trials) + " times!"
print ""

# Flip a coin 2 times, 1000 times and count how many times it comes up: 0 heads, 1 head, or 2 heads!
results = { }
for trial in range(num_trials):
	number_of_heads = 0
	for x in range(num_flips):
		result = random.choice(possibilities)
		if result == 'HEADS':
			number_of_heads = number_of_heads + 1
	results[trial] = number_of_heads

# Accumulate the results
flip_counts_result = {}
for flip_count in range(num_flips+2):
		flip_counts_result[flip_count] = 0

for trial in range(num_trials):
	num_heads = results[trial]
	flip_counts_result[num_heads] = flip_counts_result[num_heads] + 1

for i in range(num_flips+1):
	flips_histogram = flip_counts_result[i]
	print "Trials resulting in " + str(i) + " heads = " + str(flips_histogram) + " \t(" + str(flips_histogram / float(num_trials)) + " fraction)"

print "\n"
print "Once you learn the art of python you will be able to do crazy stuff like this too!"
print "\n"

