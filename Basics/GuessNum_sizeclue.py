def guess():
	import random

	num=random.randint(0,100)

	a=0

	t=0

	while a==0:
		t+=1
		temp=int(raw_input("Guess the number\n"))
		if temp==num:
			print "That's right!"
			break
		if temp<num:
			print "the number is too small. Enter a larger number"
			continue
		if temp>num:
			print "the number is too large. Enter a smaller number"
			continue

	print "You took just ",t," trials"
