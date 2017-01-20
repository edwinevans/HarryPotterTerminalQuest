# Function takes a number and a string (denomination) and return a number (knuts)


def galleons_to_knuts(num_galleons):
	num_sickles = num_galleons * 17
	num_knuts = num_sickles * 29
	return num_knuts

def sickles_to_knuts(num_sickles):
	num_knuts = num_sickles * 29
	return num_knuts

# num_knuts = nuble_duble(2, "sickles")
# print num_knuts # 58


# Example: 2, "Sickles" -> 58
def amount_to_knuts(amountOf, denomination):
	if denomination == 'knuts':
		return amountOf
	if denomination == 'sickles':
		return sickles_to_knuts(amountOf)
	if denomination == 'galleons':
		return galleons_to_knuts(amountOf)


i_have_this_many_sickles = 2
i_have_this_many_knuts = sickles_to_knuts(i_have_this_many_sickles)
print str(i_have_this_many_knuts)


# buyables = {'beetle eyes':(15, 'knuts', 15), 'unicorn horn':(10, 'galleons', 4930),'stinkweed':(3, 'sickles', 87)}
# buyables = {'beetle eyes':(15, 'knuts'), 'unicorn horn':(10, 'galleons'),'stinkweed':(3, 'sickles')}


# product_amt = ???AMT
# product_amt_denomination = ???DENOMINATION
# product_knuts =  ???AMT * 29
i_have_this_many_of_something = 3
that_something_is = "galleons"
num_knuts_i_have = amount_to_knuts(3, "galleons")
print "Answer is " + str(num_knuts_i_have)

num_knuts_i_have = amount_to_knuts(2, "sickles")
print "Answer is " + str(num_knuts_i_have)


i_have_this_many_galleons = 9
i_have_this_many_knuts = galleons_to_knuts(i_have_this_many_galleons)
print str(i_have_this_many_knuts)