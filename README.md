# Diffie Hellman Demo
Program to illustrate the functioning of the Diffie Hellman algorithm. It has a main menu with 3 options:
- Generate p and g
- Calculate A = (g^a mod p), where "a" is a randomly generated number. When selecting this option, p and g should be asked.
- Calculate shared key (ask for g, p and A)

We will simulate the algorithm by opening 2 windows of this script (Alice and Bob):
- In Alice's window, we will generate p and g (both public parameters)
- In Alice's and Bob's window, we will calculate A and B 
- In Alice's and Bob's window, we will demonstrate how the same key is generated when inputing B in Alice's window and A in Bob's window
