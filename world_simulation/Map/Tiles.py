
class Tile():
	def __init__(self, tile_type):
		"""
			Tile in the game map

			Arguments
			=========

			tile_type:
				water/land
		"""
		
		self.coords = None

		self.plants = []
		self.animals = []
		self.dead_animals = []
		self.tile_type = tile_type


	@property
	def is_land(self):
		return self.tile_type == 'Land'
	
	def place(self,X,Y):
		self.coords = (X,Y)

	def new_animal(self, animal):
		"""
			Adds an animal to the tile
		"""
		self.animals.append(animal)

	def new_plant(self, plant):
		"""
			Adds an plant to the tile
		"""
		self.plants.append(plant)

	def __repr__(self):
		return "Tile in position {} with {} animals and {} plants".format(self.coords, len(self.animals), len(self.plants))

class Water_Tile(Tile):
	def __init__(self):
		super().__init__(tile_type = 'Water')

	
class Terrain_Tile(Tile):
	def __init__(self):
		super().__init__(tile_type = 'Land')
