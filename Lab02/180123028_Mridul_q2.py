# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 13:54:18 2020

@author: Mridul Garg
"""

import matplotlib.pyplot as plt
import math
import numpy as np

#Using a Linear Congruence and a Lagged Fibonacci Generator
a = 1597
seed = 2931
b = 1
m = 244944

sequence = []
x = seed 
for i in range(17):
    x = (a*x + b)%m
    u = x/m
    sequence.append(round(u, 4))


theta = 0.2
for n in [100, 1000, 10000, 1000000]:
    seq = sequence[:]
    
    for i in range(17, n):
        u = seq[i-17] - seq[i-5]
        u = u if u>0 else u+1
        seq.append(round(u, 4))
    
    #Transforming the Uniform Distribution to Exponential Distribution
    seq = list(np.log(seq))
    for i in range(n):
        seq[i] = -1*theta*seq[i]
    
    freq = [0]*40
    mid = [0]*40
    
    #Populating the intervals and calculating the CDF
    for i in range(40):
        mid[i] = round(0.025/2 + .025*i, 5)
    for u in seq:
        for i in range(39, -1, -1):
            if i*0.025 <= u:
                freq[i] += 1
                break
    for i in range(1, 40):
        freq[i] += freq[i-1]
    for i in range(40):
        freq[i] /= n
        
        
    #Declaring values and labels for the graph
    plt.plot(mid, freq, label= "obtained", color = "red")
    
    mean, var = round(np.mean(seq), 4), round(np.var(seq), 4)
    print(mean, var)
    print(round(abs(mean-0.2), 4), round(abs(var-0.04), 4))
    
    x = np.arange(0, 1, .001)
    foo = lambda x: 1 - math.exp(-x/theta)
    y = list(map(foo, x))
    plt.plot(x, y, color = "pink", label = "expected")
    plt.ylabel("CDF")
    plt.legend()
    plt.show()


