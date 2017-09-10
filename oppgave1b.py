import numpy as np
import matplotlib.pyplot as plt
import sys
import time


#Algorithm for solving tridiagonal matrix

def genSolution(n, a, b, c, b_tilde):
	
#Forward substitution
	for i in range(n-1):
		faktor =  a[i]/b[i]
		b[i+1] -= faktor*c[i]
		b_tilde[i+1] -= faktor*b_tilde[i]

#Backwards substitution
	for i in range(n-1,1,-1):
		faktor = c[i-1]/b[i]
		b_tilde[i-1] -= faktor*b_tilde[i]

#Factoring main diagonal to 1
	for i in range(1,n):
		b_tilde[i] = b_tilde[i]/b[i]
	return b_tilde


n = int(sys.argv[1])	#number of points

h = float(1)/(n+1)  #stepsize

#Initiating 3 diagonal non-zero diagonals as vectors

a = np.empty(n+1)
a.fill(-1)
b = np.empty(n+1)
b.fill(2)
c = np.empty(n+1)
c.fill(-1)


#Computing right-hand side

x = np.linspace(0,1,n+1)
f = 100*np.exp(-10*x)
b_tilde = h**2*f

b_tilde[0] = b_tilde[n] = 0

#Computing CPU time

t0 = time.clock()
solution = genSolution(n,a,b,c, b_tilde)
t1 = time.clock()
print "CPU time: %4.2f" %(t1-t0)

#Computing maximum relative error

error = 0
u = 1-(1-np.exp(-10))*x-np.exp(-10*x)

for i in range(1,int(n)-1):
	new_error = abs((solution[i]-u[i])/u[i])
	if new_error>error:
		error = new_error
print "Maximum relative error :%f" %(abs(1-error))



plt.figure()
plt.plot(x, solution, x, u)
plt.xlabel("x")
plt.legend(["v - numerical solution", "u - analytical solutions"])
plt.title("n=%d" %(n))
plt.grid()
plt.show()
