# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 20:18:52 2020

@author: Mridul Garg
"""

import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

def FOO(n):
    return np.random.uniform(0.0, 1.0, n)

#For finding the appropriate value of k
def BS(cdf, x):
    l, r = 0, len(cdf)-1
    
    while l < r:
        mid = l + (r-l)//2
        
        if x <= cdf[mid]:
            r = mid
        else:
            l = mid + 1
            
    return l

n = 10000
const = 100.2
for const in [1.2, 10.2, 102.0]:
    c = []
    for i in range(1, 11):
        c.append(i)
    
    prob = 1/len(c)
    cdf = [prob*i for i in range(1, len(c)+1)]
    
    g = lambda x: 1/len(c)
    f = {}
    P = [0.11, 0.12, 0.09, 0.08, 0.12, 0.10, 0.09, 0.09, 0.10, 0.10]
    for i in range(1, 11):
        f[i] = P[i-1]
        
    ans = []
    for i in range(n):
        
        while True:
            u = np.random.uniform(0.0, 1.0)
            k = BS(cdf, u)
            x = c[k]
            
            rhs = f[x]/(const*g(x))
            u = np.random.uniform(0.0, 1.0)
            if u <= rhs:
                ans.append(x)
                break
            
    x = [i for i in range(1, 11)]
    y = [0]*10
    for i in ans:
        y[i-1] += 1
        
    for i in range(10):
        y[i] /= len(ans)
    
    print(round((np.var(np.array(P) - np.array(y)))**0.5, 5))
    
    
    plt.plot(x, P, color = "red", label = "Actual Distribution")
    plt.plot(x, y, color = "green", label = "Obtained Distribution")
    plt.legend()
    plt.show()
