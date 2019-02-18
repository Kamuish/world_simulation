from matplotlib import pyplot as plt 
import numpy as np

def plot_all(Map, which = 'alive'):
	f, (ax1, ax2,ax3) = plt.subplots(1,3, sharey=True)

	positions_carn = np.zeros([Map.cells.shape[0],Map.cells.shape[0]])
	positions_herb = np.zeros([Map.cells.shape[0],Map.cells.shape[0]])
	positions_plant = np.zeros([Map.cells.shape[0],Map.cells.shape[0]])

	for j in range(Map.cells.shape[0]): # very inneficient 
		for i in range(Map.cells.shape[0]):
			positions_carn[i,j] = Map.cells[i,j].get_carnivores(which)

			positions_herb[i,j] = Map.cells[i,j].get_herbivores(which)
			positions_plant[i,j] = Map.cells[i,j].number_plants

	if which == 'alive':
		c = 'Greens'
	else:
		c = 'Reds'

	f.suptitle("Animal state: {}".format(which), fontsize=14)
	ax1.pcolor(positions_plant, cmap = c,edgecolors='gray', linewidths= 1)
	ax1.set_title('Plants')

	ax2.pcolor(positions_herb, cmap = c,edgecolors='gray', linewidths= 1)
	ax2.set_title('Herbivores')

	ax3.pcolor(positions_carn, cmap = c,edgecolors='gray', linewidths= 1)
	ax3.set_title('Carnivores')

	
	plt.show()
