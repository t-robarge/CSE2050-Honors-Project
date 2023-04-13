from are_you_the_one import Contestant, Simulation
import matplotlib.pyplot as plt
import numpy as np
from statistics import mean, median
n = 1000
#Naive
freq_list = []
for sim in range(n):
    simulation = Simulation()
    #add amt of rounds to freq list
    freq_list.append(simulation.play_game('Naive'))

#plot
fig,graph = plt.subplots(1,1)
graph.hist(freq_list, bins=[0,10,20,30,40,50,60,70,80,90,100,], range=(0,10),color='cyan',edgecolor='k',label=None)
graph.set_title('Histogram of Naive Algorithm')
graph.set_xticks([0,10,20,30,40,50,60,70,80,90,100])
graph.set_yticks([0,50,100,150,200,250,300,350,400])
graph.set_xlabel('Amount of Rounds to Win')
graph.set_ylabel('Number of Occurences')
graph.axvline(mean(freq_list), color='red',linestyle='dashed',linewidth=1)
legend = ['Mean']
graph.legend(legend)
graph.text(mean(freq_list)*1.1,400,'Mean: {:.2f}'.format(mean(freq_list)))
#plt.show()

#Random
freq_list_random = []
for sim in range(n):
    simulation = Simulation()
    freq_list_random.append(simulation.play_game('Random'))
#plot
fig, graph2 = plt.subplots(1,1)
graph2.hist(freq_list_random, bins=[80,90,100,110,120,130,140,150,160,170], range=(0,10),color='red',edgecolor='k',label=None)
graph2.set_title('Histogram of Random Algorithm')
graph2.set_xticks([80,90,100,110,120,130,140,150,160,170])
graph2.set_xlabel('Amount of Rounds to Win')
graph2.set_ylabel('Number of Occurences')
graph2.axvline(mean(freq_list_random), color='cyan',linestyle='dashed',linewidth=1)
legend = ['Mean']
graph2.legend(legend)
graph2.text(mean(freq_list_random)*1.025,325,'Mean: {:.2f}'.format(mean(freq_list_random)))
#plt.show()
#Optimized
freq_list_optimized = []
for sim in range(n):
    simulation = Simulation()
    freq_list_optimized.append(simulation.play_game('Optimized'))
#Plot
fig,graph3 = plt.subplots(1,1)
graph3.hist(freq_list_optimized, bins=[0,10,20,30,40,50,60,70,80,90,100,], range=(0,10),color='green',edgecolor='k',label=None)
graph3.set_title('Histogram of Optimized Algorithm')
graph3.set_xticks([0,10,20,30,40,50,60,70,80,90,100])
graph3.set_yticks([0,50,100,150,200,250,300,350,400])
graph3.set_xlabel('Amount of Rounds to Win')
graph3.set_ylabel('Number of Occurences')
graph3.axvline(mean(freq_list_optimized), color='red',linestyle='dashed',linewidth=1)
legend = ['Mean']
graph3.legend(legend)
graph3.text(mean(freq_list_optimized)*1.1,400,'Mean: {:.2f}'.format(mean(freq_list_optimized)))
plt.show()