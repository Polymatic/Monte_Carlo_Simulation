# -*- coding: utf-8 -*-
"""
func Q2(): run to get the desired output
func FOOBAR(): generates the sequence Ui

@author: Mridul Garg
"""

import matplotlib.pyplot as plt 

def FOOBAR(m, a, b, seed):
    ans = []
    x = seed
    for i in range(2*(m-1)):
        x = (a*x)%m
        u = x/m
        ans.append(u)
        
    return ans
    

def Q3():
    a = 1229
    b = 1
    m = 2048
    seed = 1119
    
    sequence = FOOBAR(m, a, b, seed)

    n = len(sequence)
    x = sequence[:n-1]
    y = sequence[1:]
    
    #Declaring values and generating a Scatter Graph
    plt.scatter(x, y,color = "pink", marker = "o", s = 8)
    plt.title("a={}, seed={}, b={}, m={}"
                      .format(a, seed, b, m))
    plt.xlabel("Ui+1")
    plt.ylabel("Ui")
    plt.show()
    
   
Q3()