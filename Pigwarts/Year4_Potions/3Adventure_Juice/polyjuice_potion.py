import time

ingredients = [("Vineger","100 grams"), ("Fluxweed", "20 grams"),("Knotgrass", "10 grams"), ("Lacewing", "5 grams")]

for ingredient in ingredients:
	weight = ingredient[1]
	print "Add " + weight + " of " + ingredient[0] + "."
	time.sleep(5)  