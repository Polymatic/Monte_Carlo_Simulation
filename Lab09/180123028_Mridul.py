import numpy as np
import math
import random
import matplotlib.pyplot as plt

# Used to generate standard normal random samples
def BOX_MULLER(n):
    u1 = random.uniform(0.0,1.0)
    u2 = random.uniform(0.0,1.0)

    R = -2*math.log(u1)
    V = 2*math.pi*u2
    if random.uniform(0, 1) < 0.5 :
        Z = math.sqrt(R)*math.cos(V)
    else:
        Z = math.sqrt(R)*math.sin(V)
    
    return Z

# Used to generate Poisson random samples
def POISSON(l):
    check = math.exp(-l)
    k = -1
    p = 1

    while p > check:
        k += 1
        u = random.uniform(0.0,1.0)
        p *= u
    return k

# Function takes the n as the no. of Poisson arrivals, with mu and sigma, to generate n random samples from N(mu, sigma)
def M(n, mu, sigma):
    M = 0
    for _ in range(n):
        lY = BOX_MULLER(1)
        lY = mu + sigma*lY

        M += lY
    return M


sigma, mu = 0.022282, 0.000298
K = 185.33333*1.1
l = 0.1
T = 1
N = 30

asianOption = []
euroOption = []

for _ in range(1000):
    stockValue = []
    X = math.log(185.33333)

    for i in range(N):
        Z = BOX_MULLER(1) 
        temp = POISSON(l)
        
        # Obtaining the log of the next day's simulated closing price 
        X = X + (mu - (sigma**2)/2)*(T) + sigma*Z*((T)**0.5) + M(temp, mu, sigma)
        stockValue.append(math.exp(X))

    euroOption.append(max(K - stockValue[-1], 0))
    asianOption.append(max(K - sum(stockValue)/len(stockValue), 0))   


euroOption = np.array(euroOption)
asianOption = np.array(asianOption)

avgPrice = np.mean(asianOption)
sampleVar = np.var(asianOption)
euroMean = np.mean(euroOption)
euroVar = np.var(euroOption)

confidenceInterval = [round((avgPrice-(1.96*sampleVar/math.sqrt(1000))), 3), (round((avgPrice+(1.96*sampleVar/math.sqrt(1000))), 3))]
print("Method Used", "\t\t", "Average Price", "\t\t\t", "Variance", "\t\t", "95% Confidence Interval")
print("Normal Method", "\t\t", avgPrice, "\t\t", sampleVar, "\t", confidenceInterval)

# Calculating Value of b
b = 0
for i in range(len(asianOption)):
    b += (asianOption[i] - avgPrice)*(euroOption[i] - euroMean)
b /= (1000*euroVar)

# Using Control Variate
for i in range(len(asianOption)):
    asianOption[i] = asianOption[i] - b*(euroOption[i] - euroMean)

avgPrice = np.mean(asianOption)
sampleVar = np.var(asianOption)
confidenceInterval = [round((avgPrice-(1.96*sampleVar/math.sqrt(1000))), 3), (round((avgPrice+(1.96*sampleVar/math.sqrt(1000))), 3))]
print("Control Variate", "\t", avgPrice, "\t\t", sampleVar, "\t", confidenceInterval)



    

        







