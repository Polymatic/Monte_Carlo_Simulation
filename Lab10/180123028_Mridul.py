import numpy as np 
import pandas as pd 
import random
import math 

# Generating the Yi's using the given estimator
def generate_Y(m):

    U = np.random.uniform(0.0, 1.0, m)
    
    return np.exp(np.sqrt(U))

# Generating the Yi_hat's using the given estimator
def generate_Y_hat(m):

    U = np.random.uniform(0.0, 1.0, m)

    return (np.exp(np.sqrt(U)) + np.exp(np.sqrt(1-U)))/2


# Helper function to print the 95% confidence Interval and the length of that Interval
def confidence_interval(Y, m):

    mean, std = np.mean(Y), np.std(Y)

    temp = 1.96 * std / math.sqrt(m)

    lhl = round(mean-temp, 6) # left hand limit of the interval
    rhl = round(mean+temp, 6) # right hand limit of the interval
    
    length = round(2*temp, 6) # length = rhl - lhl

    return "["+ str(lhl) +", " + str(rhl) + "]", length


np.random.seed(50)

# The list of values of M to be considered
M = [100, 1000, 10000, 100000]

# numpy array to store data for tabulation
data = np.array([])

for m in M:

    Y = generate_Y(m)
    Y_hat = generate_Y_hat(m)

    # Obtaining values of I_M and I_M_hat using the given formula
    I_M = round(np.sum(Y)/m, 6)
    I_M_hat = round(np.sum(Y_hat)/m , 6)

    # Using the above defined function to find out confidence interval and its lenght corresponding to both cases 
    cf, length = confidence_interval(Y, m)
    cf_hat, length_hat = confidence_interval(Y_hat, m)

    ratio = round(length/length_hat, 6)
    
    data = np.append(data, np.array([I_M, I_M_hat, cf, cf_hat, ratio]))

# tabulating the data in a pandas DataFrame
data = np.reshape(data, (4,5))
columns = ["I_M" ,  "I_M_hat" , "Confidence Interval I_M" , " Confidence Interval I_M_hat" , "Ratio of lengths of Intervals"]

df = pd.DataFrame(data = data, index = M, columns = columns)
# print(df)
print()
print(df)