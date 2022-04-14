"""
Byte Shifted Encoding object
"""
def encode(Input,encoding=8):
	"""Encodes inputed data to Byte Shift Encoding\n
	:param Input = (str): Data to input\n
	:param encoding=(int) (0-256) (Default 8)\n
	Returns:
		Returns encoded data
	"""
	decoded = ''
	encoded = []
	f = ''
	if encoding < 10:
		f = "00"+str(encoding)
	if encoding > 9 and encoding < 100:
		f = "0"+str(encoding)
	if encoding > 99:
		f = str(encoding)
	try:
		for i in f:
			encoded.append(hex(ord(i)*16))
		for i in Input:
			encoded.append(hex(ord(i)*encoding))
		for i in encoded:
			decoded += chr(round(int(i,16)))
		return decoded
	except:
		raise Exception("Invalid Encosion Level")
def decode(encoded,encoding=8):
	'''
	Decodes Byte Shift Encoding to string\n
	:param Input=(str): Data to input\n
	:param encoding=(int) (0-256) (Default 8)
	Returns:
		Decoded text
	'''
	try:
		decoded = ''
		for i in encoded[3:]:
			decoded += chr(round(ord(i)/encoding))
		return decoded
	except ZeroDivisionError:
		raise Exception("Invalid Decosion Level Must be more than zero")
def getlevel(encoded):
	'''
	Finds the encosion level of the Byte Shifted Encoded String\n

	Returns:
		encosion level as an int
	'''
	decoded = ''
	try:
		for i in encoded[0:3]:
			decoded += chr(round(ord(i)/16))
		return int(decoded)
	except:
		raise Exception("Unknown encoding level")
def autodecode(encoded,return_decosion_level=False):
	'''
	Automatically finds the encosion level and decodes it\n
	:param encoded: Encoded text\n
	:param return_decosion_level: Returns decosion level (Default: False)
	Returns:\n
		decoded text as a str\n
		*decoded text (str),encosion level (int)\n
		*if return_decosion_level is True\n
	'''
	lvl = getlevel(encoded)
	d = decode(encoded,lvl)
	if return_decosion_level == False:
		return d
	else:
		return d,lvl