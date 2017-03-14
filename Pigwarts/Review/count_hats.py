l = ["glove", "hat", "mittens", "hat", "hat", "pants"]

def count_hats(list):
	result = 0
	for item in list:
		if item == "hat":
			result = result + 1
	return result

count = count_hats(l)
print count
