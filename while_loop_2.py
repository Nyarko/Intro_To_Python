n1 = int(input("Input your first number: "))
n2 = int(input("Now the next digit: "))

def evens(n1,n2):
	
	while (n1 < (n2 - 1)):
		n1 = n1 + 1
		if (n1 % 2 == 0):
			return n1
	return 0


print (evens(n1,n2))