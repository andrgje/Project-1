import numpy as np
import sys
import time


n = int(sys.argv[1])


A = np.zeros([n,n])

A[0][0] = 2
A[n-1][n-1] = 2
A[0][1] = -1
A[n-1][n-2] = -1
for i in range(1, n-1):
	A[i][i] = 2
	A[i][i-1] = -1
	A[i][i+1] = -1

x = np.linspace(0,1,n)

h = 1./(n)
f = 100*np.exp(-10*x)

b = h**2*f

#CPU time
t0 = time.clock()
solution = np.linalg.solve(A,b) #Bruker Gauss, treigere enn LU, men funker fint som sjekk, dette er ikke noe problem :D
t1 = time.clock()

time = t1-t0
print time


#Relative error

error = 0
u = 1-(1-np.exp(-10))*x-np.exp(-10*x)

for i in range(1,int(n)-2):
	new_error = np.log10(abs((solution[i]-u[i])/u[i]))
	if new_error>error:
		error = new_error
print error




