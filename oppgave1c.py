import numpy as np
import matplotlib.pyplot as plt
import sys
import time

def specSolTriDi(d, b):
	bs = np.empty(len(d))
	bs[0] = b[0]
	
	for i in range(1,len(d),1):
		bs[i] = b[i] + float(bs[i-1])/d[i-1]
	s = np.empty(len(bs)+1)
	s[-2]= bs[-1]/d[-1]
	s[0] = s[-1]= 0
	for i in range(len(d)-2, 0, -1):
		s[i] = (bs[i]+s[i+1])/d[i]
	
	return s
	
	
n = int(sys.argv[1])

x = np.linspace(0,1,n+1)

h = 1./(n+1)
f = 100*np.exp(-10*x)

b = h**2*f

#Computing analytical solution for the diagonal entries in our spescial matrix
d = np.empty(n)
d[0] = 2

for i in range(1,n,1):
	d[i] = (i+2)/float(i+1)	



#Computing CPU time for solving algorythm	
t0 = time.clock()
solution = specSolTriDi(d, b)
t1 = time.clock()
time = t1-t0
print "CPU time usage(n=%d): %f" %(n, time)


u = 1-(1-np.exp(-10))*x-np.exp(-10*x) #Analytical solution


"""#Computing relative error
error = 0


for i in range(1,int(n)-2):
	new_error = abs((solution[i]-u[i])/u[i])
	if new_error>error:
		error = new_error
print "Maximum relative error(n=%d): %f" %(n, abs(1-error))

"""
#Plotting numerical solution vs. analytical
plt.figure()
plt.plot(x, solution, x, u)
plt.xlabel("x")
plt.legend(["v - numerical solution", "u - analytical solutions"])
plt.title("Spesifikk algoritme for vaart tilfelle,  n=%d" %(n))
plt.grid()
plt.show()

