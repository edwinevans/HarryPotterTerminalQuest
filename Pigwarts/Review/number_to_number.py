# numbers = (1,2,3,4,5,6,7,8,9,10)

# usernum1a = raw_input('Type a number from 1 to 10 here:')
# usernum2a= raw_input('Type another number from 1 to 10 here:')

# usernum1b = int(usernum1a)
# usernum2b = int(usernum2a)

# print numbers[usernum1b -1: usernum2b]


# def print_range(num,number):
# 	# while (num <= number):
# 	# 	print num
# 	# 	num = num + 1
# 	for i in range(num,number+1):
# 		print i

#  print_range(2,53)
def multiply_range(start, end):
 	result = 1
 	for i in range(start, end + 1):
 		result = result * i
 	return result
# print multiply_range(2,4)

def factorial(number):
	result = multiply_range(1, number)
	return result

answer = factorial(5)
print answer















