import math

shape = raw_input('Type a shape -- S for Square or C for Circle:')
widthstr = raw_input('How wide is the shape?')

width = int(widthstr)

if shape == 'S':
	area = width * width

else:
	r = width / 2.0
	r2 = r * r
	area = math.pi  * r2 


print "The area of your shape is " + str(area)