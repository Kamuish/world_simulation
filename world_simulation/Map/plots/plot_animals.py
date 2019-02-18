from matplotlib import pyplot as plt 
import numpy as np 

def plot_carnivores(Map, which):
	positions = np.zeros([Map.cells.shape[0],Map.cells.shape[0]])
	for j in range(Map.cells.shape[0]): # very inneficient 
		for i in range(Map.cells.shape[0]):
			positions[i,j] = Map.cells[i,j].get_carnivores(which)


	fig, ax = plt.subplots()
	plt.title("Carnivores: {}".format(which))
	if which == 'alive':
		c = 'Greens'
	else:
		c = 'Reds'
	img = ax.pcolor(positions, cmap = c,edgecolors='gray', linewidths= 1)
	plt.show()
