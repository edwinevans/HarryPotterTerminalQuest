
import turtle

def write_harry_potter():
	turtle.speed(1)
	turtle.setheading(0)
	turtle.left(90)
	turtle.forward(80)
	turtle.right(180)


spell = "accio"
spell_name = raw_input('spell:')
if spell_name == spell:
	print "Harry Potter"
	write_harry_potter()

else:
	print "pow!"

turtle.done()