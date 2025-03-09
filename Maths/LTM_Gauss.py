# Transform a square matrix into an lower triangular form

def ltm():
	
	n=int(raw_input("Enter number of dimensions in the matrix "))  #take matrix elements from user
	print "Enter the elements of the matrix",n,"X",n
	x=[[0]*n for _ in [0]*n]
	for s in range(0,n):
		for w in range(0,n):
			x[s][w]=int(raw_input("Enter x"+str(s+1)+str(w+1)+": "))


	i=n-1
	while i>0:
		j=i-1
		while j>=0:
			
				temp=1.0*x[j][i]/x[i][i]
				k=n-1
				while k>=0:
				
					x[j][k]-=(temp)*x[i][k]
					k-=1
				j-=1
		i-=1
				

	print x

ltm()
				
