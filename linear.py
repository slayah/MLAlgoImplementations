# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 18:07:26 2015

@author: smroiti
"""

from numpy import loadtxt, zeros, ones, array, linspace, logspace, gradient
from pylab import scatter, show, title, xlabel, ylabel, plot, contour

#literals
alpha=0.01
theta0=3
theta1=50
iterations=10000
'''
m=number of training examples
hx=hypothesis function
derivative0=derivative of J wrt theta0
derivative1=derivative of J wrt theta1
J=cost function
'''
data = loadtxt('data/ex2x.dat')
values = loadtxt('data/ex2y.dat')
m=len(data)
noi=0
#finding theta0,theta1
for i in range(iterations):
    s0=0
    s1=0
    J=0
    for k in range(m):
        x=data[k]
        hx=theta0+(theta1*x)
        y=values[k]
        derivative0=(hx-y)
        derivative1=(hx-y)*x
        s0=s0+derivative0
        s1=s1+derivative1
        J=J+(hx-y)**2
    s0=s0/m
    s1=s1/m
    J=J/2
    J=J/m
    '''
    if(noi>9990):
        print J
    '''
    temp0=theta0-(alpha*s0)
    temp1=theta1-(alpha*s1)
    theta0=temp0
    theta1=temp1
    noi=noi+1    
    
print theta0,theta1

for i in range(m):
    x=data[i]
    y=theta0+(theta1*x)
    #print y    
    
'''
scatter(data,values, marker='o', c='b')
title('Profits distribution')
xlabel('Population of City in 10,000s')
ylabel('Profit in $10,000s')
show()
'''