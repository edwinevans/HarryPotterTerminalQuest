import turtle
from time import sleep

turtle.addshape("robot2.gif")
turtle.shape("robot2.gif")
turtle.speed(0)
turtle.penup()
frame = 0


def draw_bridge():
	turtle.hideturtle()
	turtle.setpos(100, 0)
	angle = 0
	bridge_down_time = 10 
	if frame < bridge_down_time:
		angle = 90
	elif frame < bridge_down_time + 90:
		angle = 90 - (frame - bridge_down_time)
	else:
		angle = 0

	turtle.setheading(angle)	
	turtle.pendown()
	turtle.forward(150)
	turtle.penup()

def draw_robot():
	turtle.setpos(-200 + frame, 0)
	turtle.showturtle()
	turtle.stamp()


def draw_scene():
	#draw_bridge()
	draw_robot()


while True:
	draw_scene()
	sleep(0.5) # Time in seconds.
	turtle.clear()
	frame = frame + 2

turtle.done()