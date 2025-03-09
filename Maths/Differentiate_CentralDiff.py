# Approximate the derivative of a function at a given point using the central difference method.

from math import *

def a(y):

	ans=sin(y);    # define the function you want to differentiate here
	return ans


def diff(f,x):

	e=0.00000000000001
  	# To increase accuracy, e should be small. But an extremely small e (10⁻¹⁴) could possibly lead to floating-point precision errors.
  	# You may use 10^(⁻7) instead. It's more stable.
	
 	x1=x+e
	x0=x-e

	diffR=(f(x1)-f(x))/e    # Forward difference
	diffL=(f(x)-f(x0))/e    # Backward difference

	result=(diffR+diffL)/2

	print result


diff(a,3.141)
