import random
class GPGenerator:
	def generateGP():
		# g is a small prime number
		small_prime_numbers = [2,3,5,7,11,13,17,19,23,29,31,37,41]
		g = random.choice(small_prime_numbers)
		#p is a big (2000 bits) number
		p = random.getrandbits(2000)
		return (g, p)