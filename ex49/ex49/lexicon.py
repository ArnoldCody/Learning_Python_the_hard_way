# coding: utf-8
# lexicon.py

def scan(stuff):
	direction = [
		'north', 'south', 'east', 'west', 'down', 'up', 'left',
		'right', 'back'
		]
	verb = ['go', 'stop', 'kill', 'eat']
	prep = ['the', 'in', 'of', 'from', 'at', 'it']
	noun = ['door', 'beer', 'princess', 'cabinet']
	
	result = []
	words = stuff.split(' ')

	for i in range(0, len(words)):
		if convert_number(words[i]):
			d = ('dig', words[i])
			result.append(d)
		
		elif words[i] in direction:
			d = ('direction', words[i])
			result.append(d)
		
		elif words[i] in verb:
			d = ('verb', words[i])
			result.append(d)

		elif words[i] in prep:
			d = ('prep', words[i])
			result.append(d)

		elif words[i] in noun:
			d = ('noun', words[i])
			result.append(d)

		else:
			d = ('error', words[i])
			result.append(d)
			
	return result

def convert_number(word):
	try:
		return int(word)
	except ValueError:
		return None
	