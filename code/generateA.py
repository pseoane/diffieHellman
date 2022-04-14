import random

class AGenerator:
	def generateA(g, p):
		a = random.randint(1, 100) 
		A = ((pow(g, a)) % p)
		return (a, A)