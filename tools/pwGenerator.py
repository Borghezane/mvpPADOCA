import random
import string

class PwGenerator:
	def genPw(nDigits):
		#characters = string.ascii_letters + string.digits + string.punctuation
		characters = string.ascii_letters + string.digits
		password = ''.join(random.choice(characters) for i in range(nDigits))

		return password
