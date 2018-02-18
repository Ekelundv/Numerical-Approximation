# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 21:48:45 2018

@author: Christian
"""
import numpy as np
import sympy as sp
from sympy.abc import x, y
from scipy import *
import matplotlib.pyplot as plt

a = -1  # left bound for x
b = 1  # right bound for x
Y = linspace(a, b, 100)
X = linspace(a, b, 25)  #
n = len(X) - 1


def T(x):  # Tschebychev polynomial
    return (cos(n * arccos(x)))


X = []  # making X an empty list to fill up with the Tschebychev points.
for i in range(n):
    X.append(cos(((2 * i + 1) / (2 * n)) * pi))  # The Tschebychev points. (The Zeros of T(x)).

X = array(X)  # redefining X so we get the X based on Zeros from the Tschebychev polynomial.
# making it an array so it works in the functions.

n = len(X) - 1  # redefining n based on the new X.
print(X)


def f(x):
    return (1 / (1 + 25 * x ** 2))


def divdiff(X):
    L = []
    L.append(list(f(X)))  # making g(X) a list, since we would otherwise have an array.
    for j in range(n):
        C = []  # creating an empty list we will fill with the divided differences of the x:es up to x_j
        for i in range(0, n - j):
            if abs(X[i + j + 1] - X[i]) < 1.e-15:  # If the differences of the Xi's are close to zero
                t = sp.diff(f(x), x, j + 1)  # We create the j+1'th derivative (depending on which list we're in)
                C.append(t.subs(x, X[i]))  # subs() evaluates t att x = X[i]
            else:
                C.append((L[j][i + 1] - L[j][i]) / (X[i + j + 1] - X[i]))
        L.append(C)
    return (L)


def pn(X, x):
    L = divdiff(X)
    p = 0
    for j in range(n + 1):
        xterm = 1
        for i in range(j):
            xterm = xterm * (x - X[i])
        p = p + L[j][0] * xterm
    return (p)


from pylab import plot, legend

plt.plot(Y, pn(X, Y), label='interpolation polynomial', linewidth=2)
plt.plot(X, pn(X, X), 'o', color='m', label='interpolating points')
plt.plot(Y, f(Y), label='f(x)')
plt.plot(Y, f(Y) - pn(X, Y), label='error function')
plt.legend()
plt.show()
