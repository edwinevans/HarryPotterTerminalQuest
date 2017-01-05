# 1 Galleon = 17 Sickles
# 1 Sickle = 29 Knuts

buyables = {'beetle eyes':(15, 'Knuts', 15), 'unicorn horn':(10, 'Galleons', 4930),'stinkweed':(3, 'sickles', 87)}
total = 0

print "Here's what you can buy:"

# Show items name and price including unit
# Each line should look like:, for example: Stinkweed - 3 Sickles
for item in buyables:
	print item + " - " + str(buyables[item][0]) +  " " + buyables[item][1]

print "Checkout: Please add your items"

items_bought = []
while True:
	item_str = raw_input() # Example "stinkweed"
	if item_str == "done":
		break
	items_bought.append(item_str)
	the_tuple = buyables[item_str] # 87
	print "Checkout: " + str(the_tuple[2]) + " knuts"

print "Checkout: Ok, done"


print "*** Your Reciept"

for item in items_bought:
	print item + " - " + str(buyables[item][2]) + " knuts."

# Checkout: Please add your items
# unicorn horn
# *** Checkout: 4930 Knuts
# beetle eyes
# *** Checkout: 15 Knuts
# done
#***Checkout: Ok, done
# *** 
# Your Receipt

# unicorn horn - 4930 Knuts
# beetle eyes - 15 Knuts
# TOTAL: 4945 Knuts

# Thank you for shopping at Mia's Emporium!
# ***




#if item in buyables:
#
# 	item_price = int(buyables[item])
# 	total = total + buyables[item]
# 	total = str (total)
# 	print "Checkout:" + total

