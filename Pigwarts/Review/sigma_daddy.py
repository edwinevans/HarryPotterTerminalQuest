total = 0 
while True:
	typed = raw_input('Type a number here:')
	if typed == "s":
	 	print total
	 	break
	total = total + int(typed) 
