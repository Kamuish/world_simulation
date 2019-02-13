from matplotlib import pyplot as plt 
import numpy as np 

def plot_carnivores(Map):
	positions = np.zeros([Map.cells.shape[0],Map.cells.shape[0]])
	print(positions.shape)
	for j in range(Map.cells.shape[0]):
		for i in range(Map.cells.shape[0]):
			positions[i,j] = Map.cells[i,j].get_carnivores()

	fig, ax = plt.subplots()
	img = ax.pcolor(positions)
	plt.show()
