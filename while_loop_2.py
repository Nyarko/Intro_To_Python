n1 = int(input("Input your first number: "))
n2 = int(input("Now the next digit: "))

def evens(n1,n2):
	
	while (n1 < (n2 - 1)):
		n1 = n1 + 1
		if (n1 % 2 == 0):
			print (n1)
	return 'Done'

print('The even numbers between', n1, 'and ', n2, 'are:')
print (evens(n1,n2))

print()

#prints the reverse
def reverse_evens(n1,n2):

	while (n2 > n1):
		n2 = n2 - 1
		if (n2 % 2 == 0):
			print (n2)
	return 'Done'

print('The even numbers between', n1, 'and ', n2, 'in reverse are:')
print (reverse_evens(n1,n2))