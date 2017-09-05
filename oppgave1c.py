import numpy as np
import matplotlib.pyplot as plt
import sys


def specSolution(n, b_tilde):
	d_tilde = np.zeros(n)
	d_tilde[0] = 2
	for i in range(1,n,1):
		d_tilde[i] = float(i+1)/i
		b_tilde[i] = b_tilde[i] + float(b_tilde[i-1])/d_tilde[i-1]
		
		
	b_tilde[n-1] = float(b_tilde[n-1])/d_tilde[n-1]
	for i in range(n-1):
		b_tilde[i] =  (b_tilde[i]+float(b_tilde[i+1])/d_tilde[i+1])/float(d_tilde[i])
		
	return b_tilde
	
n = int(sys.argv[1])

h = 1.0/(n+1)

x = np.linspace(0,1,n)

f= 100*np.exp(-10*x)

b_tilde = h**2*f

plt.plot(x,specSolution(n, b_tilde), x, 1-(1-np.exp(-10))*x-np.exp(-10*x))
plt.legend(["v", "u"])
plt.show()
