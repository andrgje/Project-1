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

d = np.empty(n+1)

d[0] = 2

for i in range(1,n+1,1):
	d[i] = (i+2)/float(i+1)	
	
t0 = time.clock()

solution = specSolTriDi(d, b)

t1 = time.clock()

time = t1-t0
print time


plt.plot(x, specSolTriDi(d, b), x, 1-(1-np.exp(-10))*x-np.exp(-10*x))
plt.legend(["v", "u"])
plt.grid()
plt.show()
		
