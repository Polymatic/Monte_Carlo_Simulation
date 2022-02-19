# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 19:46:57 2020

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

n = 1000000
c = []
for i in range(1, 10000, 2):
    c.append(i)

prob = 1/len(c)
cdf = [prob*i for i in range(1, len(c)+1)]

U = FOO(n)
result = []
for i in U:
    k = BS(cdf, i)
    result.append(c[k])

plt.hist(result, bins = 5000)
plt.show()




