# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 14:50:25 2018
@author: ville
"""

import numpy as np
import sympy as sp
from sympy.abc import x
from scipy import *
import matplotlib.pyplot as plt


h = 1 / 10000  # By replacing zero with a small number we can avoid dividing by zero.
n = 25
N = 100  # Decides the size of Y
Y = np.linspace(-1, 1, N)


def ts_points(n):
    u = np.zeros(n)
    for k in range(0, n - 1):
        u[k] = np.cos(((2 * k + 1) / (2 * n)) * np.pi)
    return u


#X = np.array(ts_points(n))
#print('X = ', X)
X = np.linspace(-1, 1, n)
n = len(X) - 1
# This seems to work (badly) when X is a equidistant grid but not when X is the zeros for the Tsch. polynomials

def f(x):
    return 1 / (1 + 25 * x ** 2)  # this function is for the use of the derivative function
    # sp.sin is needed for the packages to work together


def divdiff(X):
    L = []
    L.append(list(f(X)))
    for j in range(n):
        C = []
        for i in range(0, n - j):
            if abs(X[i + j + 1] - X[i]) < 1.e-15:  # If the differences of the Xi's are close to zero
                t = sp.diff(f(x), x, j + 1)  # We create the j+1'th derivative
                C.append(t.subs(x, X[i]))  # subs() evaluates t att x = X[i]
            else:
                C.append((L[j][i + 1] - L[j][i]) / (X[i + j + 1] - X[i]))
        L.append(C)
    return L


def pn(X, x):
    L = divdiff(X)
    p = 0
    for j in range(n + 1):
        xterm = 1
        for i in range(j):
            xterm = xterm * (x - X[i])
        p = p + L[j][0] * xterm
    return p


plt.plot(Y, pn(X, Y), label='interpolation polynomial', linewidth=2)
plt.plot(X, pn(X, X), 'o', color='m', label='interpolating points')
plt.plot(Y, f(Y), label='f(x)')
plt.plot(Y, f(Y) - pn(X, Y), label='error function')
plt.legend()
plt.show()
