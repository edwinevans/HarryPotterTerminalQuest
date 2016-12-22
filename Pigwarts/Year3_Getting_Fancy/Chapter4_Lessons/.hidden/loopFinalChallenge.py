import turtle
import random

# Make the turtle scribble using loops and random 
# 
# Hint: random() returns a number between 0 and 1. You can multiply it by
# another number if you want a larger number. For example if you multiply by
# 10 you will get a random number between 0 and 10

turtle.speed(0)

for i in range(3000):
	tup = (random.random(), random.random(), random.random())
	turtle.pencolor(tup)
	turtle.forward(random.random() * 100)
	turtle.right(random.random() * 360)
	if turtle.position()[0] > 200:
		turtle.goto(0,0)
	if turtle.position()[0] < -200:
		turtle.goto(0,0)

	if turtle.position()[1] > 200:
		turtle.goto(0,0)
	if turtle.position()[1] < -200:
		turtle.goto(0,0)

turtle.done()
