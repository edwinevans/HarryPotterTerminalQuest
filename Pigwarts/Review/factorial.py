# 1! = 1
# 2! = 2
# 3! = 6
# 4! = 24
# 5! = 120
# 1, 2, 6, 24, ...

def factorial(number):
	result = 1
	line = 1
	while True:
		result = line * result
		# print "line=" + str(line) + ", result=" + str(result)
		if line == number:
			break
		line = line + 1
	return result

print factorial(1726)

# x = 1
# number = 1
# while True:
# 	x = number * x
# 	number = number + 1
# 	print x

