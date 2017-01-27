

# Ask the user for a word. If the length of the word is over 5 letters, print "That's a long word!", otherwise print "That's a short word". You can find the length of a string using the "len" function, for example: len("delicious") # returns 9


user_word = raw_input('Type a word here: ')

if len(user_word) <= 5:
	print "That's a short word"

else:
	print "That's a long word!"