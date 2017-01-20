num_knuts_string = raw_input('Enter number of Knuts: ')
num_knuts_number = int(num_knuts_string)

sickles_amount = num_knuts_number / 29
sickles_remainder = num_knuts_number % 29

galleons_amount = sickles_amount / 17
galleons_remainder = sickles_amount % 17

print num_knuts_string + " Knuts is " + str(galleons_amount) + " Galleons, " +  str(galleons_remainder) + " Sickles, and " + \
	str(sickles_remainder) + " Knuts." 
	