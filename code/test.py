from generateGP import GPGenerator as GPGen
from generateA import AGenerator as AGen
from generateSharedKey import SharedKeyGenerator as SKGen

def bothKeysAreEqualTest():
	(g, p) = GPGen.generateGP()
	(privateA, publicA) = AGen.generateA(g, p)
	(privateB, publicB) = AGen.generateA(g, p)
	sharedKey1 = SKGen.generateSharedKey(publicB, privateA, p)
	sharedKey2 = SKGen.generateSharedKey(publicA, privateB, p)
	try:
		assert(sharedKey2 != sharedKey1)
		print("bothKeysAreEqualTest - OK")
		return True
	except:
		print("bothKeysAreEqualTest - FAIL, key1 and key2 are not equal")
		return False

if bothKeysAreEqualTest():
	exit(0)
else:
	exit(1)