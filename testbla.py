import numpy as np
import matplotlib.pyplot as plt
import sys
import time

def specSolTriDi(d, b):
	bs = np.empty(len(d))
	bs[0] = b[0]
	
	for i in range(1,len(d),1):
		bs[i] = b[i] + float(bs[i-1])/d[i-1]
	s = np.empty(len(bs))
	s[-1] = s[0] = bs[-1]/d[-1]
	for i in range(len(d)-2, 0, -1):
		s[i] = (bs[i]+s[i+1])/d[i]
	
	return s
	
	
n = int(sys.argv[1])

x = np.linspace(0,1,n+1)

h = 1./(n+1)
f = 100*np.exp(-10*x)

b = h**2*f

#Computing analytical solution for the diagonal entries in our spescial matrix
d = np.empty(n+1)
d[0] = 2

for i in range(1,n+1,1):
	d[i] = (i+2)/float(i+1)	



#Computing CPU time for solving algorythm	
t0 = time.clock()
solution = specSolTriDi(d, b)
t1 = time.clock()
time = t1-t0
print time

#Computing realtive error
error = 0
u = 1-(1-np.exp(-10))*x-np.exp(-10*x)

for i in range(1,int(n)-1):
	new_error = np.log10(abs((solution[i]-u[i])/u[i]))
	if new_error>error:
		error = new_error
print error



#Plotting numerical solution vs. analytical
plt.plot(x, solution, x, u)
plt.legend(["v", "u"])
plt.grid()
plt.show()
		
