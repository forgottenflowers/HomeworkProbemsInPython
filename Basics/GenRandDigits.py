# generate a random num havin given num of digits

def w():
	x=[0,1,2,3,4,5,6,7,8,9]
	import random
n=int(raw_input("how many digits do u want in your number?"))

	y=" "

	for i in range(n):
		y+=str(random.choice(x))

	print y," "
