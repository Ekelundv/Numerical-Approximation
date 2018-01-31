import numpy as np


n = 3
X = np.linspace(0, 2*np.pi, n+1)

f = np.sin(X)

P = np.ones((n+1, n+1))
P[:, 0] = f
#print(P)

for i in range(n):
    P = P[:-i, :]
print(P)


#P= P[:-1,:-1]
#print(P)