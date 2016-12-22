field_guide1 = [("mockingbird", "sky"), ("fish", "water"), ("worm", "ground")]

#print field_guide1

field_guide2 = {"mockingbird":"sky", "fish":"water", "worm":"ground"}

#print field_guide2

for t in field_guide1:
	if t[0] == "fish":
		print t[1]
		break




#print field_guide2["mockingbird"]