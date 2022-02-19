import matplotlib.pyplot as plt 

#Generating first 17 elements using Linear Congruence Generator
a = 1597
seed = 2931
b = 1
m = 244944

seq = []
x = seed 
for i in range(17):
    x = (a*x + b)%m
    u = x/m
    seq.append(round(u, 4))
    
print(seq)
#Generating the remaining elements
for limit in [1000, 10000, 100000]:
    sequence = seq[:]
    for i in range(17, limit):
        u = sequence[i-17] - sequence[i-5]
        u = u if u>0 else u+1
        sequence.append(round(u, 4))
    
    #Populating intervals for the Bar Graph
    freq = [0]*20
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
    plt.title("Total elements: {}".format(limit))
    
    plt.show()

    
    #Plotting a (Ui, Ui+1) Graph
    n = len(sequence)
    x = sequence[:n-1]
    y = sequence[1:]
    
    #Declaring values and generating a Scatter Graph
    plt.scatter(x, y,color = "pink", marker = "o", s = .3)
    plt.title("Total elements: {}".format(limit))
    plt.xlabel("Ui")
    plt.ylabel("Ui+1")
    plt.show()

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        
    
        

    