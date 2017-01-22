
def encrypt(text, rot):
	message = ''
	for c in text:
		message+= rotate_character(c, rot)
	return message

def rotate_character(char, rot):
	lowlist = 'abcdefghijklmnopqrstuvwxyz'
	uplist = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	if not char.isalpha():
		return char
	position = alphabet_position(char)
	if char.isupper():
	    return uplist[(position+rot)%26]
	else:
		return lowlist[(position+rot)%26] 


def alphabet_position(letter):
	alphalist = 'abcdefghijklmnopqrstuvwxyz'
	return alphalist.find(letter.lower())
