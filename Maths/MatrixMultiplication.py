def go(n):

	a=[[0]*n for _ in [0]*n]
	b=[[0]*n for _ in [0]*n]
	c=[[0]*n for _ in [0]*n]

	print "enter the elements of the matrix a"
	for i in range(0,n):
		for j in range(0,n):
			a[i][j]=float(raw_input("a"+str(i+1)+str(j+1)+":"))
	

	print "enter the elements of the matrix b"
	for i in range(0,n):
		for j in range(0,n):
			b[i][j]=float(raw_input("b"+str(i+1)+str(j+1)+":"))

	for i in range(0,n):
		for j in range(0,n):
			for k in range(0,n):
				c[i][j]+=a[i][k]*b[k][j]

	
	print "Matrix Product:"
	for i in range(0, n):
	    row = ""
	    for j in range(0, n):
	        row += str(c[i][j]) + "   "  # Concatenate each element in the row
	    print row.strip()  # Remove the trailing space
		

go(2) # Change parameter
