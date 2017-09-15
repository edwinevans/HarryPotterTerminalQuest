import random


print "test"

colors = ["R", "O", "Y", "G", "B", "P"]

answer = []
while True:
	color = random.choice(colors)
	answer.append(color)
	if len(answer) == 4:
		break

print "don't look at this! --> ", answer

while True:
	guess_string = raw_input("Make your combo:")
	guess = []
	for char in guess_string:
		guess.append(char.upper())

	print guess

	if answer == guess:
		print "You win!!!"
		break





