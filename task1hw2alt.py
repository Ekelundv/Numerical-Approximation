# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 14:49:28 2018

@author: ville
"""

import numpy as np
import sympy as sp
from sympy.abc import x,y
from scipy import *
h=1/10000 #I replace 0 with h (a small number) so we wont divide by zero
X=array([h,h,1,np.pi,np.pi,np.pi,5.5,5.5,2*pi])
n=len(X)-1 


def f(x):
    return(sp.sin(x)/x) #this function is for the use of the derivative function
                        #sp.sin is needed for the packages to work together

def g(x):               #this function is to create the first list in divdiff(X)
    return(sin(x)/x)

def divdiff(X):
    
    L=[]
    L.append(list(g(X))) #making g(X) a list, since we would otherwise have an array.
    for j in range(n):
        C=[]    #creating an empty list we will fill with the divided differences of the x:es up to x_j
        for i in range(0,n-j):
            if abs(X[i+j+1]-X[i])<1.e-15: #If the differences of the Xi's are close to zero
                t = sp.diff(f(x),x,j+1)   #We create the j+1'th derivative (depending on which list we're in)
                C.append(t.subs(x,X[i]))  #subs() evaluates t att x = X[i]
            else:
                C.append((L[j][i+1]-L[j][i])/(X[i+j+1]-X[i]))
        L.append(C)
    return(L)

def pn(X,x):
    L=divdiff(X)
    p=0
    for j in range(n+1):
        xterm=1
        for i in range(j):
            xterm=xterm*(x-X[i])
        p=p+L[j][0]*xterm
    return(p)
    
from pylab import plot, legend

Y=linspace(h,2*pi,100)
plot(Y,pn(X,Y), label='interpolation polynomial', linewidth=2)
plot(X,pn(X,X), 'o', color='m', label='interpolating points')
plot(Y,g(Y),label='f(x)')
legend()