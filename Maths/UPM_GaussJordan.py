# Transform a square matrix into a upper triangular form, with diagonal elements = 1 (normalized)

def Gauss():

	n=int(raw_input("Enter number of dimensions in the square matrix "))

	print "Enter the elements of the matrix",n,"X",n

	x=[[0]*n for _ in [0]*n]

	for s in range(0,n):

		for w in range(0,n):

			x[s][w]=int(raw_input("Enter x"+str(s+1)+str(w+1)+": "))



	for s in range(0,n):

		temp1=x[s][s]

		for w in range(0,n):

			x[s][w]=(1.0*x[s][w])/temp1

		for w in range(0,n):

			if s!=w:

				temp2=x[w][s]

				for q in range(s,n):

					x[w][q]-=temp2*x[s][q]

	print x


Gauss()					
	
