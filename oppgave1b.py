import numpy as np
import matplotlib.pyplot as plt
import sys
import time


#Algorithm for solving tridiagonal matrix

def genSolution(a, b, c, b_tilde):
	
#Forward substitution
	for i in range(len(a)-1):
		faktor =  a[i]/b[i]
		b[i+1] -= faktor*c[i]
		b_tilde[i+1] -= faktor*b_tilde[i]

#Backwards substitution
	for i in range(len(a)-1,0,-1):
		faktor = c[i-1]/b[i]
		b_tilde[i-1] -= faktor*b_tilde[i]

#Factoring main diagonal to 1
	for i in range(len(b_tilde)):
		b_tilde[i] = b_tilde[i]/b[i]
	return b_tilde


n = float(sys.argv[1])	#number of points

h = float(1)/(n+1)  #stepsize

#Initiating 3 diagonal non-zero diagonals as vectors

a = np.empty(n)
a.fill(-1)
b = np.empty(n)
b.fill(2)
c = np.empty(n)
c.fill(-1)


#Computing right-hand side

x = np.linspace(0,1,n)
f = 100*np.exp(-10*x)
b_tilde = h**2*f


#Computing CPU time

t0 = time.clock()
solution = genSolution(a,b,c, b_tilde)
t1 = time.clock()
print t1-t0

#Computing maximum relative error

error = 0
u = 1-(1-np.exp(-10))*x-np.exp(-10*x)

for i in range(1,int(n)-1):
	new_error = np.log10(abs((solution[i]-u[i])/u[i]))
	if new_error>error:
		error = new_error
print error



plt.figure()
plt.plot(x, solution, x, u)
plt.legend(["v", "u"])
plt.grid()
plt.show()
