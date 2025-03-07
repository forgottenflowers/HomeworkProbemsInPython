# This code calculates the frequency of the nucleotides 'A', 'G', 'C', 'T', and 'N' (representing unknown nucleotides). 
# Then it prints the fraction of each nucleotide type.

strfreq=raw_input("enter neucleotide seq: ")

l=len(strfreq)

frequency=[0,0,0,0,0]                  #{in the order AGCTN}

for p in strfreq :
         if p =='A':
                 frequency[0]=frequency[0]+1
         elif p =='G':
                 frequency[1]=frequency[1]+1
         elif p =='C':
                 frequency[2]=frequency[2]+1
         elif p =='T':
                 frequency[3]=frequency[3]+1
         else:
                 frequency[4]=frequency[4]+1

print "length of the seq. is:",l
print "A:",frequency[0],"G:",frequency[1],"C:",frequency[2],"T:",frequency[3],"N:",frequency[4]
           
l = float(l)  
print  "frac of A:",[frequency[0]]/float(l),"frac of G:",[frequency[1]]/float(l),"frac of C:",[frequency[2]]/float(l),"frac of T:",[frequency[3]]/float(l),"frac of N:",[frequency[4]]/float(l)
