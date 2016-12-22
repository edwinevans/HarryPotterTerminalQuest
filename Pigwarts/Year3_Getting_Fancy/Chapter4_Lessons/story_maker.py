import random

for i in range(50):
	protagonist = random.choice(["boy", "dog", "pig", "man", "grandpa"])
	home = random.choice(["shoe", "pretty little house", "castle"])
	place = random.choice(["Australia", "a zoo", "China", "Edwin's house"])
	words = random.choice(["Good morning", "Good afternoon", "Hi"])
	visitor = random.choice(["kangoroo", "flying elephant", "snowman"])

	story = "__________________________________________\n"
	story += "THE " + protagonist.upper() + " WHO LIVED IN A " + home.upper()
	story += "\n\n"
	story += "Once upon a time there was a " + protagonist + ". He lived in a " + home + ". "
	story += "One day, a " + visitor + " from " + place + " came to visit. "
	story += 'It said, "' + words + '".'	
	story += "\n\n   The End"
	print story
	print "\n"




