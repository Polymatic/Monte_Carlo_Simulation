# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 19:12:36 2020

@author: Mridul Garg
"""

import numpy as np
import matplotlib.pyplot as plt

def FOO(n):
    return np.random.uniform(0.0, 1.0, n)
    
n = 1000000
f = lambda x : 20*x*(1-x)**3
g = lambda x : 1
t = 5*27/64 
for c in [t, t+10, t+40]:
    
    count = []
    result = []
    for i in range(n):
        steps = 1
        while True:
            x = np.random.uniform(0.0, 1.0)
            u = np.random.uniform(0.0, 1.0)
            
            k = f(x)/(c*g(x))
            if u <= k:
                result.append(x)
                count.append(steps)
                break
            else:
                steps += 1
    
    
    
        
    x = result
    
    freq = [0]*40
    mid = [0]*40
    for i in range(40):
        mid[i] = round(0.025/2 + .025*i, 5)
    for u in result:
        for i in range(39, -1, -1):
            if i*0.025 <= u:
                freq[i] += 1
                break
    for i in range(40):
        freq[i] /= len(result)
    
    print(c, np.mean(count), np.mean(result))
    
    plt.plot(mid, freq)
    plt.title("Obtained Graph")
    plt.show()
    
    x = np.arange(0, 1, .001)
    foo = f
    y = list(map(foo, x))
    
    plt.plot(x, y, color = "pink")
    plt.title("Graph of the Function")
    plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


