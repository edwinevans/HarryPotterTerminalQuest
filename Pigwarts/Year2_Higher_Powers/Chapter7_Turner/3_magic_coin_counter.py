import random

possibilities = ['HEADS', 'TAILS']
for trial in range(10):
	number_of_heads = 0
	for x in range(5):
		result = random.choice(possibilities)
		if result == 'HEADS':
			number_of_heads = number_of_heads + 1
	print number_of_heads		