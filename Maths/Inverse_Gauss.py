# Compute inverse matrix via Gauss elimination

def Gauss():
	temp1=0
	temp2=0
	n=int(raw_input("Enter number of dimensions in the square matrix "))
	print "Enter the elements of the matrix",n,"X",n
	x=[[0]*n for _ in [0]*n]
	for s in range(0,n):
		for w in range(0,n):
			x[s][w]=int(raw_input("Enter x"+str(s+1)+str(w+1)+": "))
	
	y=[]
	z=[[0]*n for _ in [0]*n]
	
	for s in range(0,n):
		temp1=x[s][s]
		y.append(temp1)
		for w in range(0,n):
			x[s][w]=(1.0*x[s][w])/temp1
				
		for w in range(0,n):
			if s!=w:
				temp2=x[w][s]
				z[w][s]=temp2
				for q in range(s,n):
					x[w][q]-=temp2*x[s][q]

	for s in range(0,n):
		
		for w in range(0,n):
			x[s][w]=(1.0*x[s][w])/y[s]
    	
		for w in range(0,n):
			if s!=w:
				
				for q in range(0,n):
					x[w][q]-=z[w][s]*x[s][q]
						
	print x
	
Gauss()					
