table = {'A': '._', 'B':'_...', 'C':'_._.', 'D': '_..', 'E':'.', 'F':'.._.',
'G':'__.', 'H':'....', 'I':'..', 'J':'.___', 'K':'_._', 'L':'._..', 'M':'__',
'N':'_.', 'O':'___', 'P':'.__.', 'Q':'__._', 'R':'._.', 'S':'...','T':'_','U':'.._',
'V':'..._','W':'.__','X':'_.._','Y':'_.__','Z':'__..','1':'.____','2':'..___',
'3':'...__','4':'...._','5':'.....','6':'_....','7':'__...','8':'___..','9':'____.','0':'_____'}

reverse_table = {}

for k, v in table.items():
   	reverse_table[v] = k

sentence = raw_input('type something in morse code here:')

sentence_split = sentence.split(' ')

for item in sentence_split:
	print reverse_table[item],
