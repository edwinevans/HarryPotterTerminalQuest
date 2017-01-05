# 1 Galleon = 17 Sickles
# 1 Sickle = 29 Knuts

# Numbers
# String
# List
# Tuple
# Dictionary

num_galleons_string = raw_input('Enter number of Galleons:')
num_galleons_number = int(num_galleons_string)

num_sickles_entered_string = raw_input('Enter number of Sickles: ')	
num_sickles_entered_number = int(num_sickles_entered_string)

num_sickles = num_galleons_number * 17
num_sickles_total = num_sickles_entered_number + num_sickles
num_knuts = num_sickles_total * 29

num_knuts_string = str(num_knuts)

print num_galleons_string + " Galleons and " + num_sickles_entered_string + \
	" Sickles is " + num_knuts_string + " knuts."



# num_sickles_string = int(num_sickles) + (num_galleons_string) * 17
# num_knuts_string = int(num_sickles) * 29


# print (num_sickles_string) + " sickles is " + str(num_knuts) + " Knuts."
