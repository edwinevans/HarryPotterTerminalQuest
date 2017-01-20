SICKLES_PER_GALLEON = 17
KNUTS_PER_SICKLE = 29
KNUTS_PER_GALLEON = KNUTS_PER_SICKLE * SICKLES_PER_GALLEON

def sickles_to_knuts(num_sickles):
	num_knuts = num_sickles * KNUTS_PER_SICKLE
	return num_knuts

# 1. Create galleons_to_knuts function

def galleons_to_knuts(num_galleons):
	num_sickles = num_galleons * SICKLES_PER_GALLEON
	num_knuts = sickles_to_knuts(num_sickles)
	return num_knuts

# 2. Create a function to convert Galleons, Sickles, Knuts to knuts function
#def convert_to_knuts(galleons, sickles, knuts):

def convert_to_knuts(galleons, sickles, knuts):
	num_knuts1 = galleons_to_knuts(galleons)
	num_knuts2 = sickles_to_knuts(sickles)
	num_knuts = num_knuts1 + num_knuts2 + knuts
	return num_knuts

# 3. Create convert from knuts function 
# Define a function that takes a number of knuts and prints out the number
# of Galleons, Sickels, and Knuts


def convert_from_knuts(knuts):
	num_galleons = knuts / KNUTS_PER_GALLEON 
	num_knuts_remainder = knuts % KNUTS_PER_GALLEON 
	num_sickles = num_knuts_remainder / KNUTS_PER_SICKLE
	num_knuts = num_knuts_remainder % KNUTS_PER_SICKLE
	return (num_galleons, num_sickles, num_knuts)


# my_sickles = 3
# my_knuts = sickles_to_knuts(my_sickles)
# print str(my_knuts)

# print str(galleons_to_knuts(2))


#print KNUTS_PER_GALLEON
#convert_from_knuts(KNUTS_PER_GALLEON + 30)
# test = 582
# print test

# galleons, sickles, knuts = convert_from_knuts(test)
# print (galleons, sickles, knuts)
# print convert_to_knuts(galleons, sickles, knuts)

for i in range(0, 600):
	print convert_from_knuts(i)



