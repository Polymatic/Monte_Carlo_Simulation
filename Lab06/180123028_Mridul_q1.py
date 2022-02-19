import numpy as np
import matplotlib.pyplot as plt 
import random
import plotly.graph_objects as go
import math

# For Plotting the Marginal Distribution Curves
def PLOT(result, mu, sigma, text = ""):
    
    text += " ∼ N (µ , σ) \n a = {} \n mean = {}  variance = {} ".format(a, round(np.mean(result), 4), round(np.var(result), 4))
    result = list(result)
    count, bins, ignored = plt.hist(result, bins = 40, color = "lightblue", density = True)
    plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
    np.exp( - (bins - mu)**2 / (2 * sigma**2) ), color='red')
    
    plt.xlabel("Bins")
    plt.ylabel("Frequency")
    plt.title(text)
    
    plt.show()

# PDF function of Multivariate Normal Distribution
def pdf_multivariate_norm(X, mean, var):
    d = len(X)
    X = np.array(X)
    
    det = np.linalg.det(var)
    inv = np.linalg.inv(var)

    x = X
    x_mu = x-mean
    norm_const = 1.0/(((2*np.pi)**(d/2)) * (det**0.5))
    result = np.exp(-np.matmul(np.transpose(x_mu), np.matmul(inv, x_mu))/2)
    return (norm_const*result)
   
# Box Muller method to produce Bivariate Standard Normal Distribution
def BOX_MULLER(n):

    Z1, Z2 = [], []

    for _ in range(n):

        u1 = random.uniform(0.0,1.0)
        u2 = random.uniform(0.0,1.0)

        R = -2*math.log(u1)
        V = 2*math.pi*u2

        z1 = math.sqrt(R)*math.cos(V)
        z2 = math.sqrt(R)*math.sin(V)
        
        Z1.append(z1)
        Z2.append(z2)
    
    Z1 = np.array(Z1)
    Z2 = np.array(Z2)
    return Z1, Z2


# Main Function Body
n = 1000
for a in [-0.5, 0, 0.5, 1]:

    mu_vector = np.array([5,8])
    covariance_matrix = np.array([[1 , 2*a] , [2*a, 4]])

    Z1, Z2 = BOX_MULLER(n)
    X1 = mu_vector[0] + Z1
    X2 = mu_vector[1] + a*Z1*2 + ((1-a*a)**0.5)*2*Z2

    X = np.array([X1, X2])
    mean = np.round(np.mean(X, axis = 1),3)
    var =  np.round(np.cov(X, bias = True), 3)

    print(min(X1), max(X1))
    print(min(X2), max(X2))



# Plotting Simulated Graphs
    n = len(X1)
    intervals = 25
    xinterval, yinterval = np.linspace(-5, 20, intervals), np.linspace(-5, 20, intervals)

    z = [[0 for i in range(intervals)] for i in range(intervals)]
    for i in range(n):
        x, y = X1[i], X2[i]

        for k in range(intervals):
            if x <= xinterval[k]:
                xint = k
                break
        for k in range(intervals):
            if y <= yinterval[k]:
                yint = k
                break

        z[xint][yint] += 1

    text = 'a = {} <br> SIMULATED Multivariate Distribution Curve <br> Mean = {} Variance  = {}'.format(a, mean, var)
    fig = go.Figure(data=[go.Surface(z=z, x=xinterval, y=yinterval)])
    fig.update_layout(title=text, autosize=False,
                  scene = dict(
                    xaxis_title='X1',
                    yaxis_title='X2',
                    zaxis_title='Count'),
                  width=700, height=700,
                  margin=dict(l=65, r=50, b=65, t=90))
    fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                  highlightcolor="limegreen", project_z=True))
    fig.show()



# Plotting Actual Graphs
    if a != 1:
        intervals = 100
        Xact, Yact = np.linspace(-5, 20, intervals), np.linspace(-5, 20, intervals)

        z = [[0 for i in range(intervals)] for i in range(intervals)]

        for i in range(intervals):
            for j in range(intervals):
                z[i][j] = pdf_multivariate_norm([Xact[i], Yact[j]], mu_vector, covariance_matrix)

        mean = mu_vector
        var = covariance_matrix
        text = 'a = {} <br> Actual Multivariate Distribution Curve <br> Mean = {} Variance  = {}'.format(a, mean, var)
        fig = go.Figure(data=[go.Surface(z=z, x=Xact, y=Yact)])
        fig.update_layout(title=text, autosize=False,
                    scene = dict(
                    xaxis_title='X1',
                    yaxis_title='X2',
                    zaxis_title='Frequency'),
        
                      width=700, height=700,
                      margin=dict(l=65, r=50, b=65, t=90))
        fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                      highlightcolor="limegreen", project_z=True))
        fig.show()

# Plotting marginal Distribution Graphs

    PLOT(X1, 5, 1, "X1")
    PLOT(X2, 8, 2, "X2")


