# User enters numbers
# If enter "a" output the average of all the numbers

sum = 0
num_numbers = 0
while True:
	user_num = raw_input("Type a number here: ")
	if (user_num == "a"):
		if num_numbers == 0:
			print "No average"
		else:
			print float(sum) / num_numbers
		break
	num_numbers = num_numbers + 1
	sum = sum + int(user_num)
