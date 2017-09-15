
testNeedles1 = [ 8, 10, 17, 22 ]
testHaystack1 = [ 1, 8, 10, 11, 17, 22]

# def check_haystack_contains_all_items(haystack, items):
# 	needles = 0
# 	length_list = len (items)
# 	for i in items:
# 		if i in haystack:
# 			needles = needles + 1
# 			if needles == length_list:
# 				return True
# 	return False


# def check_haystack_contains_all_items(haystack, items):
# 	needles = 0
# 	length_list = len (items)
# 	for i in items:
# 		if i not in haystack:
# 			return False
# 		else:
# 			continue
# 	return True


def check_haystack_contains_all_items(haystack, items):
	for i in items:
		if i not in haystack:
			return False
	return True



contains_all = check_haystack_contains_all_items(testHaystack1,testNeedles1)
print contains_all

# def check_needle_in_haystack(haystack, item):
# 	if item in haystack:
# 		return True	
# 	else:
# 		return False	

	

# result = check_needle_in_haystack(testHaystack1, 7)
# print result

