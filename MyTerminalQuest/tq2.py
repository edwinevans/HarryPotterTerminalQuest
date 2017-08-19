import sys


shirt = """
    /-----\______/-----\\
   /_____         ______\\
         |        |
         |        |
         |________|
"""



toilet = """
         /------------\\
      ___|            | 
     \\___             |
         |            | 
         |            |
           ----------
          /  _____   \\
         |  /     \   |
         |  \_____/   |
          \\__________/    
"""






home = [ 
			{ 
				"type":"directory", "name":"closet", "items":
				[
					{"type":"file", "name":"shirt", "contents":shirt},
					{"type":"file", "name":"pants", "contents":"Pretty pants"},
					{"type":"file", "name":"skirt"},
					{"type":"file", "name":"dress"}
				]
			},
			{ 
				"type":"directory", "name":"bathroom", "items":
				[
					{"type":"file", "name":"toilet", "contents":toilet},
					{"type":"file", "name":"bathtub"},
					{"type":"file", "name":"mirror"},
					{"type":"file", "name":"sink"}
				]
			}
		]

current_path = home



				  # "bed":["pajamas","pillow", "blanket", "secret box"],
				  # "drawer":["hair clips", "hair bands", "note", "mirror"],
				  # "bathroom":["toilet", "bathtub", "mirror", "sink"], 
				  # "bookshelf":["Atlas World", "The Defanglers", "The Brothers Grimmm"]}]




print "You are in a room. Use the 'ls' command to look around."
i = 0
while True:
	typed = raw_input(">")
	words = typed.split()
	if len(words) <= 0:
		continue
	command = words[0]
	if command == "ls":
		for item in current_path:
			print item["name"]
	elif command == "cat":
		file_name = words[1]
		for item in current_path:
			if item["name"] == file_name:
				print item["contents"]
	elif command == "cd":
		directory_name = words[1]
		if directory_name == "..":
			current_path = home
		else:	
			i = 0
			for item in current_path:
				if item["name"] == directory_name:
					current_path = home[i]["items"]
					break
				i += 1
			
		# if directory_name == "closet":
		# 	current_path = home[0]["items"]	
		# 	print " Hi! My name is Bob and i'm an idiot!"
		# elif directory_name == "bathroom":
		# 	current_path = home[1]["items"]

	else:
		i += 1
		if i > 2:
			print "you're booted out!!"
			sys.exit()
		print "type a valid command or you will be boosted out of this room!"


