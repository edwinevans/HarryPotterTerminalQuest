buyables = {"porcupine quills":(20,'knuts',20),"beetle eyes":(15,'knuts',15),"dragon liver":(1,'galleon',493),"wand":(7,'galleons',3451),"robe":(1,'galleon',493)}

print "Here are your options, what do you want to buy:"

for item in buyables:
	print item + " - " + str(buyables[item][0]) + " " + buyables[item][1]

print "***Checkout: Put your items here"

items_bought = []
while True:
	item = raw_input()
	if item == "done":
		break
	
	if item in buyables: 
		print "***Checkout: " + str(buyables[item][2]) + " knuts."
		items_bought.append(item)
	else:
		print 'You will have to check a different store for this item.'

total = 0

print "***RECEIPT***"

for item in items_bought:
	print item + " - " + str(buyables[item][2]) + " knuts."
	total = total + buyables[item][2]

print "TOTAL: " + str(total) + " knuts."

# Here's what you can buy:
# beetle eys - 15 Knuts
# unicorn horn - 10 Galleons
# Stinkweed - 3 Sickles

# *** Checkout: Please add your items
# beetle eyes
# *** Checkout: 15 Knuts
# beetle eyes
# *** Checkout: 30 Knuts
# unicorn horn
# *** Checkout: ?? Knuts
# done
# *** 
# Your Receipt

# beetle eyes - 15 Knuts
# beetle eyes - 15 Knuts
# unicorn horn - ?? Knuts
# TOTAL: ?? Knuts

# Thank you for shopping at Mia's Emporium!

