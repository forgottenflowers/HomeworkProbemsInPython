# Find prime factors

def prime():
	list=[]
	
n=int(raw_input("Enter the number\n"))
	for i in range (2,n+1):
		if n%i==0:
			list.append(i)
			n=n/i
	print list
