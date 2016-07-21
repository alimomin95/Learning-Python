from random import randint

while 1:
	getspace = raw_input("Press enter to roll the dice!")
	number1 = randint(1,6)
	if number1 == 6:
		print "You rolled a 6!"
		getspace = raw_input("Press enter to roll again")
		number2 = randint(1,6)
		if number2 == 6:
			print "You rolled a 6 again!"
			getspace = raw_input("Press enter to roll again")
			number3 = randint(1,6)
			if number3 == 6:
				print "You rolled a 6 :("
				print "Sorry! You rolled three sixes in a row. Better luck next time."
				continue
			else:
				print "You rolled a " + str(number1) + " " + str(number2) + "and a "+ str(number3) + "."
				continue
		else:
			print "You rolled a " + str(number1) + " and a "+ str(number2) + "."
			continue
	else:
		print "You rolled a " + str(number1) + "."
		continue


