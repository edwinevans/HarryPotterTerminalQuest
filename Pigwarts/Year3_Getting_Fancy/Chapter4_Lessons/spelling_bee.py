import random
from subprocess import call

words = []

words += [ "smirk", "destiny", "monkeys", "studio", "nifty", "janitor", "pottery", "wonderful", 
			"square", "belief","contract", "anteater", "pouring", "lantern", "subtracting", "portable", 
			"twine", "estate", "umbrella", "timidly" ]

words += [ "observe", "trance", "elderly", "liquid", "deadline", "country", "flexible", 
			"promote", "massive", "bronze", "climbed", "teaspoon", "balance", "knitting", "merely", "furnish", "passage", 
			"complaints", "thunderbolt", "nonsense" ]
words += [ "mansion", "laundry", "available", "lodging", "portions", "gallant", "veins", "mountain", "whistling", 
			"voyage", "hooves", "funnel", "gravely", "hiccups", "performance", "specific", "dowdy", "indicate", "clause", "failure"]

for x in range(3):
	word = random.choice(words)
	repeat = True
	while repeat:
		repeat = False
		call(["say", word])
		answer = raw_input('Enter your input:')
		if answer == "repeat":
			repeat = True
		elif answer == word:
			print "Yay!"
		else:
			print "Incorrect. The answer is " + word


