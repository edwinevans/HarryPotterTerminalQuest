total = 0

shopping_list = (("potatoes", 2.50), ("milk", 3.25), ("butter", 1.50))

for inner_tuple in shopping_list:
	cost = inner_tuple[1]
	print inner_tuple[0] + ', $' + "{:0.2f}".format(cost)
	total = total + inner_tuple[1] 

print "Total: $" +  "{:0.2f}".format(total)