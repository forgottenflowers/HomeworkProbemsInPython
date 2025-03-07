# This program implements the Gauss elimination method for solving a system of linear equations Ax=b

def Gauss():
	n=int(raw_input("Enter number of dimensions in coefficient matrix "))  #take matrix elements from user
	print "Enter the elements of coefficient matrix",n,"X",n
	x=[[0]*n for _ in [0]*n]
	for s in range(0,n):
		for w in range(0,n):
			x[s][w]=int(raw_input("Enter x"+str(s+1)+str(w+1)+": "))
	print "Now enter the elements of the constant matrix ",n,"X1"
	for s in range(0,n):
		x[s].append(int(raw_input("Enter d1"+str(s+1)+": ")))  #join the coefficient matrix with the constant matrix
	

  # Gaussian elimination procedure
	for s in range(0,n):
		temp1=x[s][s]
		for w in range(0,n+1):
			x[s][w]=(1.0*x[s][w])/temp1 #normalisation (making the pivot elements 1)
			

	
		for w in range(0,n):
			if s!=w:
				temp2=x[w][s]
				for q in range(s,n+1):
					x[w][q]-=temp2*x[s][q] #row operations (elimination)
				

	print "The solutions are: "
	for s in range(0,n):
		print x[s][n]


Gauss()					
