#If we list all the natural numbers below 10 that are 
#multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of 
#these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

count = 999
summation = 0

while count > 0:
	if (count/3.0).is_integer():
		summation += count
	elif (count/5.0).is_integer():
		summation += count
	count -= 1


print summation