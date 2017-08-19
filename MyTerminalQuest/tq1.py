import sys

home = [ {"type":"directory", "name":"closet", "items":
					[
					`{"type":"file", "name":"shirt", "contents":shirt},
					`{"type":"file", "name":"pants"},
					`{"type":"file", "name":"skirt"},
					`{"type":"file", "name":"dress"}
					],
					
				  "bed":["pajamas","pillow", "blanket", "secret box"],
				  "drawer":["hair clips", "hair bands", "note", "mirror"],
				  "bathroom":["toilet", "bathtub", "mirror", "sink"], 
				  "bookshelf":["Atlas World", "The Defanglers", "The Brothers Grimmm"]
				 ]


shirt = """
    /-----\______/-----\\
   /_____         ______\\
         |        |
         |        |
         |________|
"""

print "You are in a room. Use the 'ls' command to look around."
i = 0
while True:
	typed = raw_input(">")
	words = typed.split()
	command = words[0]
	if command == "ls":
		for item in home:
			print item
	elif command == "cat":
		file_name = words[1]
		print home[file_name]
	# elif typed == "cat closet" or typed == "cat bed" or typed == "cat drawer":
	# 	if typed == "cat closet":
	# 		print "shirt  pants  skirt  dress"
	# 	elif typed == "cat bed":
	# 		print "pajamas  pillow  blanket  secret box"
	# elif typed == "cat shirt":
	else:
		i += 1
		if i > 2:
			print "you're booted out!!"
			sys.exit()
		print "type a valid command or you will be boosted out of this room!"


