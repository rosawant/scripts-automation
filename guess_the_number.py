import random

guess = random.randrange(10)

counter = 0

while counter < 3:
	number = input("Enter no. betweeen 1-10")

	if guess == number :
		print "you got it"
	else:
		print "try next time"
	counter = counter + 1
