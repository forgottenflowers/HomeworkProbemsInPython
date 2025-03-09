# This program implements the Regula Falsi Method to approximate a root of f(y).
# We need 2 initial guesses, one a lower bound and one an upper bound from the User.
# The user also inputs the desired number of iterations.

def f(x):
	a=x*x*x-x*3+1
	return a

def RF(f,a,b,m):
	while m>0:
		m=m-1
		c=(a*f(b)-b*f(a))/(f(b)-f(a))    # Note: beware of possible div0 error, can add something like if abs(f(b) - f(a)) < 1e-10: break
		if f(a)*f(c)<0:
			b=c
		elif f(a)*f(c)>0:
			a=c
		else:
			break
	print c

RF(f,0,1.0,3)
	
