import numpy
import math
import random
import matplotlib.pyplot as plt

# Used to generate standard normal random samples
def BOX_MULLER(n):
    u1 = random.uniform(0.0,1.0)
    u2 = random.uniform(0.0,1.0)

    R = -2*math.log(u1)
    V = 2*math.pi*u2

    z1 = math.sqrt(R)*math.cos(V)
    return z1

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

for l in [0.01, 0.05, 0.1, 0.2]:
    stockValue = []
    time = []
    X = math.log(185.33333)
    t = 0
    dic = {}
    for i in range(1000):
        Z = BOX_MULLER(1) 
        temp = POISSON(l)
        # Maintaining a dictionary DS to find the number of jumps
        if temp not in dic:
            dic[temp] = 1
        else:
            dic[temp] += 1
        
        # Obtaining the log of the next day's simulated closing price 
        X = X + (mu - (sigma**2)/2) + sigma*BOX_MULLER(1) + M(temp, mu, sigma)

        stockValue.append(math.exp(X))
        time.append(t)
        t += 1

    print("No of Jumps:", sum(dic.values())-dic[0])

    # Plotting the sample path
    plt.plot(time, stockValue)
    plt.title("Jump Diffusion Process \n lambda = {}".format(l))
    plt.ylabel("Adjusted Closing Price")
    plt.xlabel("Time Points")
    plt.show()
    



    

        







