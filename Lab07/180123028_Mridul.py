import csv
import numpy
import math
import random
import pandas as pd

def BOX_MULLER(n):
    Z1= []
    for _ in range(n):
        u1 = random.uniform(0.0,1.0)
        u2 = random.uniform(0.0,1.0)

        R = -2*math.log(u1)
        V = 2*math.pi*u2

        z1 = math.sqrt(R)*math.cos(V)
        z2 = math.sqrt(R)*math.sin(V)
        
        Z1.append(z1)
        Z1.append(z2)
    return Z1


with open('SBIN.NS.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    stockPrices = []
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            continue
            # print(f'Column names are {", ".join(row)}')
            
        else:
            stockPrices.append(row[5])
            # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            # line_count += 1
    # print(f'Processed {line_count} lines.')
stockPrices = list(map(float, stockPrices))

n = len(stockPrices)
logReturns = []
for i in range(1, n):
    u = math.log(stockPrices[i]/stockPrices[i-1])
    logReturns.append(u)

n = len(logReturns)
# Calculating the Expected value of the log returns
Eu = sum(logReturns)/n


# Variance of log returns
variance = 0
for i in range(n):
    variance += (logReturns[i] - Eu)**2
variance /= (n-1)

# Calculating mu and sigma
mu = Eu + variance/2
sigma = variance**0.5
print()
print("Eu = ", round(Eu, 6))
print("mu = ", round(mu, 6))
print("sigma = ", round(sigma, 6))
print()

# Calculating the number of working days between 30th Sept and the given dates
septDate = '2020-09-30'

# Getting only the business days 
days = pd.bdate_range(start = '7/1/2020', periods= 200,  freq ='B')

# Getting the total business days till oct__
oct17 = days.get_loc('2020-10-07') - days.get_loc(septDate) 
oct14 = days.get_loc('2020-10-14') - days.get_loc(septDate) 
oct21 = days.get_loc('2020-10-21') - days.get_loc(septDate) 

# print(days)

# Getting 2m random samples with the standard normal distribution using Box-Muller Method
m = 500
Z = BOX_MULLER(m)

s0 = stockPrices[-1]

# Calculating the Mean value of a 1000 possible values for the 3 desired dates
mean = []
for working_days in [oct17, oct14, oct21]:
    x = 0
    for i in range(2*m):
        x += math.exp(Eu*working_days + sigma * (working_days**0.5) * Z[i])

    temp = (s0*x) / (2*m)
    mean.append(temp)

print("Obtained value for 7th Oct 2020: {}".format(round(mean[0], 2)))
print("Obtained value for 14th Oct 2020: {}".format(round(mean[1], 2)))
print("Obtained value for 21th Oct 2020: {}".format(round(mean[2], 2)))
print()
# Calculating percentage error
actual_values = [190.70, 200.05, 203.75]
errors = []
for i in range(3):
    error = abs(mean[i] - actual_values[i]) * 100 / actual_values[i]
    errors.append(error)

print("Percentage error for 7th Oct 2020: {}".format(round(errors[0], 2)))
print("Percentage error for 14th Oct 2020: {}".format(round(errors[1], 2)))
print("Percentage error for 21th Oct 2020: {}".format(round(errors[2], 2)))










