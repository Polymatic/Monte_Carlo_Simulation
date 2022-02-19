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

for n in [100, 1000, 10000, 1000000]:
    seq = sequence[:]
    
    for i in range(17, n):
        u = seq[i-17] - seq[i-5]
        u = u if u>0 else u+1
        seq.append(round(u, 4))


    #Transforming the Uniform Distribution to ArcSine Distribution
    for i in range(n):
        x = seq[i]
        x = math.sin(x*np.pi/2)
        seq[i] = x**2
    
    #Populating the intervals, calculating frequency
    freq = [0]*40
    mid = [0]*40
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
        
    #Calculating Mean and Variance and the absolute differences
    mean, var = round(np.mean(seq), 4), round(np.var(seq), 4)
    print(mean, var)
    print(round(abs(mean-0.5), 4), round(abs(var-0.125), 4))
    
        
    #Declaring values and labels for the graph
    x = np.arange(0, 1, .001)
    foo = lambda x: (2/np.pi)*math.asin(x**0.5)
    y = list(map(foo, x))
    plt.plot(mid, freq, color = "red")
    plt.plot(x, y, color = "pink")
    plt.show()


