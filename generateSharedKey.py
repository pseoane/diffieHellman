class SharedKeyGenerator:
	def generateSharedKey(publicB, privateA, p):
		return pow(publicB, privateA) % p