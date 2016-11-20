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

combo = random.randrange(1, 100)
print "(the number is " + str(combo) + ")"
print ""
# ----

guess = 100
while True:
	response = raw_input("Is it " + str(guess) + "? (n)ah (g)ah (y)ah ")

	if response == "g":
		guess = guess - 1
		print guess

	if response == "y":
		break

	if response == "q":
		print "Quitters never win. Winners never quit."
		break

# ---
if guess == combo:
	print "Tada!!! The door slowly swings open with a creaking, sputtering, grumbling noise."



