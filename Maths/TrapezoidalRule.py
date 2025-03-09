# Approximate the integration of any function using Trapezoidal rule with desired accuracy

from math import *

def f(x):    # You can change this depending on which function you want to integrate, here f(x)=e^(-x^2)
	p=(-1)*x*x
	y=exp(p)
	return y


def TrapInt(f,a,b,n):    # a = start, b = stop, n = subintervals
	h=(a+b)/n
	t=(f(a)+f(b))/2
	i=1
	temp=a

	while i<n:
		i=i+1
		temp+=h
		t+=f(temp)

	ans=h*t
	print ans

# approximate the integral of the function f(x)=e^(-x^2) from 0 to 1 with n=60 subintervals.
TrapInt(f,0,1.0,60)
