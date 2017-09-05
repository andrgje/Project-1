import numpy as np
import matplotlib.pyplot as plt
import sys

# legger inn en liten endring her jeg
# hilsen synne

#Algoritme for loesning av tridiagonal matrise
#6n floating point operations
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

h = float(1)/(n+1)

a = np.empty(n)
a.fill(-1)
b = np.empty(n)
b.fill(2)
c = np.empty(n)
c.fill(-1)



x = np.linspace(0,1,n)

f = 100*np.exp(-10*x)

b_tilde = h**2*f

plt.figure()
plt.plot(x, genSolution(a,b,c,b_tilde), x, 1-(1-np.exp(-10))*x-np.exp(-10*x))
plt.legend(["v", "u"])
plt.show()
