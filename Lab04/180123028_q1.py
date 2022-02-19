# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 03:51:09 2020

@author: Mridul Garg
"""
from math import gamma
import matplotlib.pyplot as plt
import numpy as np

def f(a1, a2, x):
    X = (x**(a1-1))*((1-x)**(a2-1))
    return X

n = 100000
for A in [(1, 2), (2, 2), (3, 2), (4, 2), (3, 4)]:
    a1, a2 = A
    B = (gamma(a1+a2))/gamma(a1)*gamma(a2)
    
    x_ = (a1 - 1)/(a1+a2 - 2)
    
    c = f(a1, a2, x_)*B
    
    result = []
    count = []
    for i in range(n):
        steps = 1
        
        while True:
            u1 = np.random.uniform(0.0, 1.0)
            u2 = np.random.uniform(0.0, 1.0)
            
            if c*u2 <= f(a1, a2, u1):
                result.append(u1)
                count.append(steps)
                break
            else:
                steps += 1

    plt.hist(result, bins = 40, 
                    color = "pink", 
                    density = False, 
                    stacked = False)
    
    freq = [0]*40
    mid = [0]*40
    for i in range(40):
        mid[i] = round(0.025/2 + .025*i, 5)
    for u in result:
        for i in range(39, -1, -1):
            if i*0.025 <= u:
                freq[i] += 1
                break
    
    plt.xlabel("Bins")
    plt.ylabel("Count")
    plt.title("Histogram for a1={}, a2={}".format(a1, a2))
    plt.plot(mid, freq, color = "red")
    
    plt.show()
    
    
    
    