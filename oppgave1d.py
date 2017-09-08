import sys
import numpy as np

def genSolution(a, b, c, b_tilde):
	for i in range(len(a)-1):
		faktor =  a[i]/b[i]
		b[i+1] -= faktor*c[i]
		b_tilde[i+1] -= faktor*b_tilde[i]

	for i in range(len(a)-1,0,-1):
		faktor = c[i-1]/b[i]
		b_tilde[i-1] -= faktor*b_tilde[i]


	for i in range(len(b_tilde)):
		b_tilde[i] = b_tilde[i]/b[i]
	return b_tilde

n = float(sys.argv[1])
j = float(sys.argv[2])
h = 1.0/j
x = np.linspace(0,1,n)
u = 1-(1-np.exp(-10))*x-np.exp(-10*x)

a = np.empty(n)
a.fill(-1)
b = np.empty(n)
b.fill(2)
c = np.empty(n)
c.fill(-1)
f = 100*np.exp(-10*x)
b_tilde = h**2*f
RelativError
RelativError += log10(np.abs(genSolution(a,b,c,b_tilde) - u)/u)
print RelativError
