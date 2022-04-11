from generateGP import GPGenerator as GPGen
from generateA import AGenerator as AGen
from generateSharedKey import SharedKeyGenerator as SKGen

MENU = """---------------------------
Select an option:
 - 1: generate p and q
 - 2: calculate A
 - 3: generate shared key
 - 4: exit
---------------------------
"""

privateA = -1

def handleGPOption():
	(g, p) = GPGen.generateGP()
	print(f"g: {g}")
	print(f"p: {p}")	

def handleGenerateAOption():
	global privateA
	try:
		g = int(input("Introduce g: "))
		p = int(input("Introduce p: "))
		assert(g < p)
		(privateA, publicA) = AGen.generateA(g, p)
		print(f"Public A parameter is {publicA}. Private parameter stored internally")
	except:
		print("Invalid parameters. Ensure g < p")

def handleGenerateKeyOption():
	try: 
		p = int(input("Introduce p: "))
		publicB = int(input("Introduce your friend's public A: "))
	except:
		print("Invalid parameter")
		return
	if privateA == -1:
		print("Private a parameter not set. Option 2 must be called before generating shared key")
	else:
		sharedKey = SKGen.generateSharedKey(publicB, privateA, p)
		print(f"Shared Key {sharedKey}")

def handleOption(option):
	if option == 1:
		handleGPOption()
	elif option == 2:
		handleGenerateAOption()
	elif option == 3:
		handleGenerateKeyOption()
	elif option == 4:
		return -1
	else:
		print("Invalid option")
		return 0
	return 0

def main():
	while True:
		try:
			option = int(input(MENU))
			print("---------------------------")
			if handleOption(option) != 0:
				break
		except:
			print("Invalid option")


main()
