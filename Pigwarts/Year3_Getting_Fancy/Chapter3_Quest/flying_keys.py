# todo from forbidden.keys_list import list
import keys_list 
list = keys_list.the_list

# list contains a bunch of items including a golden key
# find the golden key and you'll find a secret

in_hand = None
#print list

# look for exactly "gold*key"

print list

for key in list: 
	if key == "gold*key":
		print key  