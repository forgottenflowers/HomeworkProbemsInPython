# User is asked to guess a randomly generated number.
# User is given the option to try again or quit.

def guess():
	import random

	n=1
	x=random.randrange(100)
	t=1
	y=int(raw_input("Guess the number....its between 0 and 100 "))

	while n==1:
		if y==x:
			print "Congratulations! You are right! " 
			break
 
		elif y<x: 
			print "your number is smaller than the required number "

 		else:
			print "your number is larger than the required number "

		op=raw_input("Do you want to try again? y/n ")
 
		if op=="y": 
  			t=t+1 
 			y=int(raw_input("Okay...so what's your guess? "))
      			continue
 
		elif op=="n":
 			break

		else: 
   
			print "error!goodbye.."  
			break

	print "You have made "+str(t)+" trials" 
