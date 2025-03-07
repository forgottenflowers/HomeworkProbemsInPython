# This program implements the Merge Sort algorithm, which is a divide-and-conquer algorithm for sorting a list.
# It also has a global counter to track the number of calls to the merging function (fuse).
# It prints the sorted list and the total number of times fuse is called, which is an important metric for understanding the merge process.

steps=0
g=0
def fuse_sort(L, p, r):
   if len(L)<=1:
       print L
   if p < r:
       q = (p+r)/2
       fuse_sort(L, p, q)
       fuse_sort(L, q+1, r)
       fuse(L, p, q, r)


def fuse(L, p, q, r):
    global steps
    global g
    i=p
    j=q+1
    R=[]
    while i<=q and j<=r:
        if L[i]<L[j]:
            R.append(L[i])
            i=i+1           
        else:
            R.append(L[j])
            j=j+1
    
    while i<=q:
        R.append(L[i])
        i=i+1
    
    while j<=r:
        R.append(L[j])
        j=j+1
    
    for k in range(0, (r-p)+ 1):
        L[p + k] = R[k]
    
    g=R
    steps = steps + 1
    
    
    
L=[55,78,40,21,9,43,31]
d=fuse_sort(L,0,len(L)-1)

print "sorted list : ",g
print "Total times the func. fuse(L,p,q,r) used is : ",steps


#"The total no. of times func. Fuse(l, p,q,r) called for list of 64 elements is 63. This can be calculated by modyfing the list L as counter step is already used for counting it."


#T(n) = 2T(n/2) + n
#T(n) = 2(2T(n/4) + n/2) + n
#T(n) = 4T(n/4) + 2n
#T(n) = 2**iT(n/2**i) + n*i
#n/2**i = 1 since T(1) is known
#2**i = n
#i = log(n) :its base is 2 
#T(1) = 2
#T(n) = 2*n*T(1) + n*log(n)
#T(n) = 4*n + n*log(n) = n*(4+log(n))
#The highest upper bound is : (n*n)
