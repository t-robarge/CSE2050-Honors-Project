from are_you_the_one import Contestant, Simulation
import matplotlib.pyplot as plt
import numpy as np
n = 1000
freq_list = []
for sim in range(n):
    simulation = Simulation()
    freq_list.append(simulation.play_game())
plt.hist(freq_list,5)


avg = sum(freq_list) / len(freq_list)
print(avg)


#plt.text(avg,)
plt.show()