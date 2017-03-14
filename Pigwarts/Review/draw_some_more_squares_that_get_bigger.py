import turtle

def square(num):
	turtle.forward(num)
	turtle.right(90)
	turtle.forward(num)
	turtle.right(90)
	turtle.forward(num) 
	turtle.right(90)	
	turtle.forward(num)
	turtle.right(90)

square(10)

# x = 0
# for i in range(20):
# 	square(x)
# 	x = x + 10

turtle.done() 