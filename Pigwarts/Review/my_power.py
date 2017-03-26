# 3 => 8
# 

def calculate_2_to_power_of_n(number):
	power = 1
	for i in range(number):
		power = power * 2
	return power	


print calculate_2_to_power_of_n(3)
