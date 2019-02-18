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

	def pass_time(self):
		"""
		Passes time for all cells
			- Have to find a better way to do this -> IT'S UGLY
		"""
		for j in range(self.cells.shape[0]):
			for i in range(self.cells.shape[0]):
			
				self.cells[i,j].pass_time()

	def get_cell(self, x,y):
		return self.cells[x,y]

	def place_animal(self, xx,yy, animal):
		self.cells[xx,yy].new_animal(animal)

	def place_plant(self, xx,yy, plant):
		self.cells[xx,yy].new_plant(plant)