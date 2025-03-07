# Transform a square matrix into an upper triangular form, from top to bottom (standard Gaussian elimination order).

def upm():
	
	n=int(raw_input("Enter number of dimensions in the matrix "))  #take matrix elements from user
	
	print "Enter the elements of the matrix",n,"X",n

	x=[[0]*n for _ in [0]*n]

	for s in range(0,n):
		for w in range(0,n):

			x[s][w]=int(raw_input("Enter x"+str(s+1)+str(w+1)+": "))



	for i in range(0,n-1):
		for j in range(i+1,n):
	
			temp=1.0*x[j][i]/x[i][i]

			for k in range(0,n):	
				x[j][k]-=(temp)*x[i][k]

	print x

upm()
