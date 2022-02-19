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
    

def Q2():
    for a in [1597, 51749]:
        for seed in [3, 61, 791, 2931, 244940]:
            
            freq = [0 for i in range(20)]
            sequence = FOOBAR(244944, a, 0, seed)
            
            #Populating the intervals
            for u in sequence:
                for i in range(19, -1, -1):
                    if i*.05 <= u:
                        freq[i] += 1
                        break
            
            #Declaring values and labels for the bar graph
            tick_label = ["{}-{}".format(round(i/100, 2), round(i/100+.05, 2)) for i in range(0, 100, 5)]
            left = [i for i in range(1, 21)]
            
            plt.bar(left, freq, tick_label = tick_label, 
                    color = "pink")
            plt.xticks(rotation=90)
            plt.title("a={}, seed={}, b={}, m={}"
                      .format(a, seed, 0, 244944))
            
            plt.show()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'*2)
        
    

Q2()
