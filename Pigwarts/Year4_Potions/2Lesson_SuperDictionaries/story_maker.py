import random

for i in range(50):
	protagonist = random.choice(["boy", "dog", "pig", "man", "grandpa"])
	home = random.choice(["shoe", "pretty little house", "castle"])
	place = random.choice(["Australia", "a zoo", "China", "Edwin's house"])
	visitor = random.choice(["kangaroo", "flying elephant", "snowman"])

	problem_dict = {"kangaroo":"There isn't enough food to eat, please help!", 
				"flying elephant":"I have an invitation fom the Bean of England for you to come and be a guest at the royal SandCastle", 
				"snowman":"My friends and I are in grave danger. In fact, I risked my life to deliver this message. OUR HOME IS MELTING!"}
	solution_dict = {"kangaroo":"why don't you start farming? While you're waiting though, I can share my food with you",
				"flying elephant":"Sure i'll come. When must I go?", 
				"snowman":"I can help, take me to your home . I wil bring ice and other stuff to keep your home livable."}


	# story_elements = 
	# 	{"kangaroo":
	# 		{ 
	# 			"problem" : "There isn't enough food to eat, please help!", 
	# 		  	"solution" : "why don't you start farming? While you're waiting though, I can share my food with you"
	# 		 }
	# 	}


	solu
	story = "__________________________________________\n"
	story += "THE " + protagonist.upper() + " WHO LIVED IN A " + home.upper()
	story += "\n\n"
	story += "Once upon a time there was a " + protagonist + ". He lived in a " + home + ". "
	story += "One day, a " + visitor + " from " + place + " came to visit. "
	story += 'It said, "' + problem_dict[visitor]+ '".'	
	story += 'The ' + protagonist + " said '" + solution_dict[visitor] + "'."
	story += "\n\n   The End"
	print story
	print "\n"