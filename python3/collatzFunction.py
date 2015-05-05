def collatz(number):
	if (number % 2) == 0: # checks if the parameter passed to the collatz function is an even number
		number = number // 2
		print(number)
		return number
	else
		number = 3 * number + 1
		print(number)
		return number
		
print('Enter number:')

try:
	i = int(input())
except:
	print('Must enter an integer.')
	
while i != 1:
	i = (collatz(i))
