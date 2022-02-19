# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 14:57:31 2020

@author: Mridul Garg
"""
import matplotlib.pyplot as plt
import time
import numpy as np
import math

def PLOT(sequence, text):
    plt.hist(sequence, bins = 40, color = "pink")
    plt.xlabel("Bins")
    plt.ylabel("Count")
    plt.title(text)
    plt.show()


def Normal_0_5(result, text):
    n = len(result)
    sigma = 5**0.5
    mu = 0
    for i in range(n):
        result[i] = result[i]*5**0.5
     
    count, bins, ignored = plt.hist(result, bins = 40, color = "lightblue", density = True)
    plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
    np.exp( - (bins - mu)**2 / (2 * sigma**2) ), color='darkgreen')
    
    plt.xlabel("Bins")
    plt.ylabel("Frequency")
    plt.title(text + "- N(0, 5)")
    
    plt.show()

def Normal_5_5(result, text):
    n = len(result)
    sigma = 5**0.5
    mu = 5
    for i in range(n):
        result[i] = result[i]*5**0.5 + 5 
     
    count, bins, ignored = plt.hist(result, bins = 40, color = "lightblue", density = True)
    plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
    np.exp( - (bins - mu)**2 / (2 * sigma**2) ), color='darkgreen')
    
    plt.xlabel("Bins")
    plt.ylabel("Frequency")
    plt.title(text + "- N(5, 5)")
    
    plt.show()

def BOX_MULLER(n):
    start = time.time()*10000
    result = []
    
    for i in range(n):
        u1 = np.random.uniform(0.0, 1.0)
        u2 = np.random.uniform(0.0, 1.0)
        
        R = -2*np.log(u1)
        V = 2*np.pi*u2
        z1 = (R**0.5)*math.cos(V)
        z2 = (R**0.5)*math.sin(V)
        
        result.append(z1)
        result.append(z2)
    end = time.time()*10000
    print("Time elapsed for BOX_MULLER:", end - start)
    print("Elements Generated:", n*2)
    print("Mean:", np.mean(result), ", Variance:", np.var(result))
    PLOT(result, "BOX_MULLER Plot, n = " + str(2*n))
    
    Normal_5_5(result[:], "BOX_MULLER")
    Normal_0_5(result[:], "BOX_MULLER")
    
def MARSAGLIA_BRAY(n):
    start = time.time()*10000
    result = []
    rejected = 0
    
    for i in range(n):
#        X = 2
        while True:
            u1 = np.random.uniform(0.0, 1.0)
            u2 = np.random.uniform(0.0, 1.0)
            u1 = 2*u1 - 1
            u2 = 2*u2 - 1
            
            X = u1**2 + u2**2
            
            if X > 1:
                rejected += 1
            else:
                break
            
        Y = (-2*np.log(X)/X)**0.5
        z1 = u1*Y
        z2 = u2*Y
        
        result.append(z1)
        result.append(z2)
    
    end = time.time()*10000
    print("Time elapsed for MARSAGLIA_BRAY:", end - start)
    print("Elements Generated:", n*2)
    print("Mean:", np.mean(result), ", Variance:", np.var(result))
    print("rejected:", rejected/(n+rejected), 1 - np.pi/4)
    PLOT(result, "MARSAGLIA_BRAY Plot, n = " + str(2*n))
        
    Normal_5_5(result[:], "MARSAGLIA_BRAY")
    Normal_0_5(result[:], "MARSAGLIA_BRAY")    
    
for n in [50, 5000]:
    BOX_MULLER(n)
    print("-------------------------------")
#    MARSAGLIA_BRAY(n)

print("*******************************")
print("*******************************")

for n in [50, 5000]:
    print("-------------------------------")
    MARSAGLIA_BRAY(n)
















