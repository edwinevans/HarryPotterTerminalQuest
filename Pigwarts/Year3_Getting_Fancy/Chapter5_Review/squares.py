import turtle 

def DrawSquare():
	turtle.speed(10)
	turtle.forward(80)
	turtle.right(90)
	turtle.forward(80)
	turtle.right(90)
	turtle.forward(80)
	turtle.right(90)
	turtle.forward(80)
	turtle.right(90)

turtle.left(90)
DrawSquare()

for i in range(50):
	turtle.right(7)
	DrawSquare()

turtle.done()