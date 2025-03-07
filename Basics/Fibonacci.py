# Generate Fibonacci sequence up to a given upper limit

x=int(raw_input("enter length of series"))

lst=[0,1]

while len(lst)<x:
 lst.append(lst[-1]+lst[-2])
  
print lst
