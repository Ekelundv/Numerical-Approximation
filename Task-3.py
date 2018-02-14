# -*- coding: utf-8 -*-
from numpy import *
from pylab import *

n = 2
X = linspace(0, 2*pi, n+1)

def f(x):
    return cos(x)


def divdiff(x):
    L = []
    L.append(list(f(x)))
    for j in range(n):
        C=[]
        for i in range(0, n-j):
            C.append((L[j][i+1]-L[j][i])/(X[j+i+1]-X[i]))
        L.append(C)
    return L

Y = linspace(0,2*pi, 100)

def pn(X, x):
    L = divdiff(X)
    p = 0
    for j in range(n+1):
        xterm = 1
        for i in range(j):
            xterm = xterm*(x - X[i])
        p = p + xterm*L[j][0]
    return p


plot(Y, pn(X, Y))
plot(X, pn(X, X), color='red', marker='o', linestyle="None")
legend()
ylabel('Interpolating polynomial')
xlabel('n = 2')




