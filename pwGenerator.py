import random
import string

class pwGenerator:
	def genPw(nDigits):
		characters = string.ascii_letters + string.digits + string.punctuation
		password = ''.join(random.choice(characters) for i in range(nDigits))

		return password
