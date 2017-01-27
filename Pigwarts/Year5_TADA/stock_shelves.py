import turtle

def stock_shelf(x, y, item_name, size, amount):
	turtle.penup()
	turtle.setx(x)
	turtle.sety(y)
	turtle.pendown()
	for i in range(amount):
		if item_name == 'wand':
			draw_wand(size)
			turtle.setheading(0)
			turtle.forward(20)
	
def draw_wand(size):
	turtle.fill(True)
	turtle.setheading(90)
	turtle.forward(size)
	turtle.right(90)
	turtle.forward(size / 25)
	turtle.right(90)
	turtle.forward(size)
	turtle.right(90)
	turtle.forward(size / 25)
	turtle.fill(False)
	

turtle.speed(9)
stock_shelf(0, 0, "wand", 100, 10)
stock_shelf(0, 150, "wand", 120, 8)

turtle.done()