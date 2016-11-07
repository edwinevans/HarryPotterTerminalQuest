# Help at https://docs.python.org/2/library/turtle.html
import turtle

def drawM():
	turtle.forward(100)
	turtle.right(135)
	turtle.forward(141)
	turtle.left(90)
	turtle.forward(141)
	turtle.right(135)
	turtle.forward(100)
	turtle.left(180)
	turtle.penup()
	turtle.setpos(0,0)
	turtle.pendown()

turtle.speed(10)

turtle.left(90)
drawM()

for i in range(90):
	turtle.right(7)
	drawM()

turtle.done()