# -*- coding: utf-8 -*-
"""
func Q1() : Run to get the desired output
func FOO(): Generates the sequence Xi

@author: Mridul Garg
"""

def FOO(m, a, b, seed):
    
    ans = []
    x = seed
    for i in range(2*(m-1)):
        x = (a*x)%m        
        ans.append(x)
        
    return (ans)
    
def Q1():
    for a in [6, 3]:
        for seed in range(11):
            sequence = FOO(11, a, 0, seed)
            dic = {}
            for i in range(len(sequence)):
                if sequence[i] in dic:
                    period = i - dic[sequence[i]]
                    break
                else:
                    dic[sequence[i]] = i
            
            print("seed =", seed, ", period =", period, sequence)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'*2)
        
       
Q1() 
