# Sort list in ascending order

def s(seq):
	for i in range(0,len(seq)):

  		for j in range(i+1,len(seq)):

   			if seq[i]>seq[j]:

    				seq[i],seq[j]=seq[j],seq[i]
	print seq


s([6,3,8,4,1,6,67,35])
