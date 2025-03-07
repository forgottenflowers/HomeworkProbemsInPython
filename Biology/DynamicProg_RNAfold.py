# Compute the RNA folding using dynamic programming calculations

def max(n1,n2,n3,n4):
	n=n1
	if n2>n:
		n=n2
	if n3>n:
		n=n3
	if n4>n:
		n=n4
	return n

def wax(a,b):
	w=0
	if a=='A':
		if b=='U':
			w=2
	elif a=='U':
		if b=='A':
			w=2
		elif b=='G':
			w=1
	elif a=='G':
		if b=='U':
			w=1
		elif b=='C':
			w=3
	elif a=='C':
		if b=='G':
			w=3
	return w


def maxy(m,x,y):
	mu=0
	for k in range(x+1,y):
		if m[x][k]+m[k+1][y]>mu:
			mu=m[x][k]+m[k+1][y]
	return mu
		

def run():
	seq=raw_input("Enter RNA sequence in capital letters: ")
	l=len(seq)
	s=[[0]*l for _ in [0]*l]
	for j in range(1,l):
		for i in range(j-1,-1,-1):
			s[i][j]=max(s[i+1][j-1]+wax(seq[i],seq[j]),s[i+1][j],s[i][j-1],maxy(s,i,j))
	print s
	i=0
	j=l-1
	while i<j:
		if s[i][j]==s[i+1][j]:
			i,j=i+1,j
		elif s[i][j]==s[i][j-1]:
			i,j=i,j-1
		elif s[i][j]==s[i+1][j-1]+wax(seq[i],seq[j]):
			print i,seq[i],',',j,seq[j]
			i,j=i+1,j-1
