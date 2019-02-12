from .Tiles import Terrain_Tile, Water_Tile
import numpy as np

class Map():
	def __init__(self, size):
		self.cells = np.empty( (size,size), dtype=object)
		for j in range(size):
			for i in range(size):
				plate = Terrain_Tile()
				plate.place(i,j)

				self.cells[i,j] = plate


	def place_animal(self, xx,yy, animal):
		self.cells[xx,yy].new_animal(animal)