import random 

total = 0
while True:
	number = random.random()
	print number
	total = total + number
	if number > 0.8:
		break
print total