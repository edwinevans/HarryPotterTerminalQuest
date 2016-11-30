# THE ENTRY PAINTING
# 

import random


print "Hellllo my child. Let me know the combo number and I can unlock the door for you."
print "I will try to unlock it as fast as I can but I only can hear the words Oyyyy and GAH!!"
print "Say Oyyyy if I guess too low and GAH!! if I guess too high. Or YAY! if I get it"
print ""
print " The guess variable is your guess. If the human says you guessed too high"
print "         how should you cnage your guess (the variable)?"
print ""
print " A variable can appear on the left or right of the equal sign. For example"
print "x = 3"
print "y = x # Now y will be 3"
print ""

max = 1000 * 1000
combo = random.randrange(1, max)

# The next door (gasp!!)
# combo = random.randrange(1, 100000)

print "(the number is " + str(combo) + ")"
print ""
# ----
N1 = 1
N2 = max
guess = None
guessNumber = 1
while True:
	guess = ( N2 - N1 ) / 2 + N1

	response = raw_input("Guess " + str(guessNumber) + ": Is it " + str(guess) + " (n)ah (g)ah (y)ah ")
	guessNumber = guessNumber + 1

	if response == "g":
		N2 = guess

	if response == "n":
		N1 = guess

	if response == "y":
		break

	if response == "q":
		print "Quitters never win. Winners never quit."
		break

# ---
if guess == combo:
	print "Tada!!! The door slowly swings open with a creaking, sputtering, grumbling noise."



