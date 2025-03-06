# NOTE: This code runs on Python 2 IDE

from math import *

def euler():
	
	print "This program solves for the function values of the differential equation (dy/dt)=Ay"

	A= float(raw_input("Enter the value of A:"))
	h= float(raw_input("Enter the step size:"))
	
	t= float(raw_input("Enter the value of 't' where you want to find y(t):"))

	f=exp(A*t)


	y=1
	
	i=0

	while ((i+h)<=t):

		y*=1+(h*A)

		i+=h


	print "The solution is:",y


	error=y-f

	print "The error is:",error


	eperc=(error/f)*100

	print "The percentage error is:",eperc


euler()
